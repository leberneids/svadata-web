#!/usr/bin/env python3
"""Capture the portal's real UI for the public site.

Same convention as build_hero_iso.py: a committed generator that sits next to
the asset it produces, so the picture on svadata.com can always be rebuilt
rather than remembered.

What it captures is the REAL portal — same code a client runs — pointed at the
synthetic `taller-demo` floor seeded by sva_repo/scripts/demo_seed.py. Nothing
here touches a client's data, and nothing here draws a fake UI.

Prerequisites (see the runbook in 02_Projects/00_Guias/):

    cd ../../02_Projects/sva/sva_repo
    docker compose -f docker-compose.yml -f docker-compose.override.yml \
                   -f demo/docker-compose.demo.yml up -d timescaledb portal caddy
    SVA_DEMO=1 python3 scripts/demo_seed.py --days 21 --seed 7
    make tool-backfill DAYS=21
    SVA_DEMO=1 python3 scripts/demo_seed.py --topup     # <- immediately before this

Run:

    ~/.venvs/web-fetch/bin/python assets/build_shots.py

ALWAYS capture through caddy (http://localhost/), never the :8080 debug door:
on 8080 the portal's is_sva_local() predicate is true and the SVA-only "Mi Edge"
nav item renders into every screenshot.
"""

import argparse
import io
import sys
from pathlib import Path

try:
    from PIL import Image
    from playwright.sync_api import sync_playwright
except ImportError:
    sys.exit("run with ~/.venvs/web-fetch/bin/python (needs playwright + Pillow)")

OUT = Path(__file__).resolve().parent / "img"
VIEWPORT = {"width": 1600, "height": 1000}
SCALE = 2                 # capture at 2x, downscale to 1600 -> crisp on retina
TARGET_W = 1600           # display slot is 1144px (.wrap 1200 - 56 padding)
WEBP_QUALITY = 72
BUDGET_BYTES = 800_000    # total for assets/img — the page must stay light

# name, path, locator (None = full page), extra wait
SHOTS = [
    ("portal-planta",       "/planta",                              ".page",   "floor"),
    ("portal-analisis",     "/analisis?p=mes",                      None,      "charts"),
    ("portal-alarmas",      "/alarmas",                             ".page",   None),
    ("portal-herramientas", "/maquinas/cnc-01?vista=herramientas&p=30",  "tabla",   None),
    ("portal-informe",      "/informes",                            ".page",   None),
]

# Kill anything that makes two runs differ byte-for-byte, and anything that is
# internal-only. The live clock is the obvious one; without hiding it every
# rebuild produces a "changed" file for no visible reason.
STABILISE_CSS = """
#upd { visibility: hidden !important; }
*, *::before, *::after { animation: none !important; transition: none !important; }
"""


def wait_ready(page, kind):
    """Wait on the app's own signals, never a sleep."""
    page.wait_for_load_state("networkidle")
    if kind == "floor":
        # refresh() writes "actualizado ..." only after a successful /api/planta
        # round-trip, so this proves the tiles hold live data.
        page.wait_for_function(
            "() => { const e = document.getElementById('upd');"
            " return e && e.textContent.trim().startsWith('actualizado'); }",
            timeout=30_000)
    elif kind == "charts":
        # ECharts canvases are sized on init; width 0 means not drawn yet.
        page.wait_for_function(
            "() => { const c = [...document.querySelectorAll('canvas')];"
            " return c.length > 0 && c.every(x => x.width > 0); }",
            timeout=30_000)
    page.wait_for_timeout(700)   # paint settle


def save(png_bytes, name, crop_to=None):
    im = Image.open(io.BytesIO(png_bytes)).convert("RGB")
    if crop_to:
        im = im.crop((0, 0, min(crop_to[0], im.width), min(crop_to[1], im.height)))
    if im.width > TARGET_W:
        h = round(im.height * TARGET_W / im.width)
        im = im.resize((TARGET_W, h), Image.LANCZOS)
    path = OUT / f"{name}.webp"
    # No EXIF/ICC is carried over: Image.save on a fresh RGB image writes none.
    im.save(path, "WEBP", quality=WEBP_QUALITY, method=6)
    return path, im.size


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="http://localhost")
    ap.add_argument("--only", help="capture just this one (by name)")
    args = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    shots = [s for s in SHOTS if not args.only or s[0] == args.only]

    with sync_playwright() as pw:
        browser = pw.chromium.launch(args=["--force-color-profile=srgb",
                                           "--hide-scrollbars"])
        ctx = browser.new_context(
            viewport=VIEWPORT, device_scale_factor=SCALE,
            locale="es-ES", timezone_id="Europe/Madrid",
            color_scheme="light", reduced_motion="reduce")
        page = ctx.new_page()

        for name, path, locator, kind in shots:
            page.goto(args.base + path, wait_until="domcontentloaded", timeout=45_000)
            page.add_style_tag(content=STABILISE_CSS)
            wait_ready(page, kind)

            if locator == "tabla":
                # Panel top through the end of the table: keeps the panel's
                # heading (which states the period and the load threshold) and
                # drops the legend prose below it.
                panel = page.locator("section.area.panel").first
                table = panel.locator("table").first
                pb, tb = panel.bounding_box(), table.bounding_box()
                png = page.screenshot(clip={
                    "x": pb["x"], "y": pb["y"],
                    "width": pb["width"],
                    "height": tb["y"] + tb["height"] - pb["y"] + 18})
            elif locator:
                png = page.locator(locator).first.screenshot()
            else:
                png = page.screenshot(full_page=True)

            p, size = save(png, name)
            print(f"  {name:22s} {size[0]}x{size[1]:<5d} {p.stat().st_size/1024:6.1f} KB")

        # Open Graph card: the floor, cropped to 1200x630. PNG — WhatsApp and
        # LinkedIn still treat WebP previews inconsistently.
        page.goto(args.base + "/planta", wait_until="domcontentloaded")
        page.add_style_tag(content=STABILISE_CSS)
        wait_ready(page, "floor")
        og = Image.open(io.BytesIO(page.screenshot())).convert("RGB")
        og = og.resize((1600, round(og.height * 1600 / og.width)), Image.LANCZOS)
        og = og.crop((0, 0, 1200, min(630, og.height)))
        og.save(OUT / "og-planta.png", "PNG", optimize=True)
        print(f"  {'og-planta':22s} {og.size[0]}x{og.size[1]:<5d} "
              f"{(OUT / 'og-planta.png').stat().st_size/1024:6.1f} KB")

        browser.close()

    total = sum(f.stat().st_size for f in OUT.iterdir() if f.is_file())
    print(f"\n  total {total/1024:.1f} KB / budget {BUDGET_BYTES/1024:.0f} KB")
    if total > BUDGET_BYTES:
        sys.exit(f"OVER BUDGET by {(total - BUDGET_BYTES)/1024:.1f} KB — "
                 f"drop a shot or lower WEBP_QUALITY")


if __name__ == "__main__":
    main()
