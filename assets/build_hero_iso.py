#!/usr/bin/env python3
"""Genera la ilustración isométrica del hero (línea navy) y la inyecta en index.html.

Escena: 5 tornos CNC + CMM conectados a un mini-PC industrial central (edge);
el mini-PC envía los datos al disco SVA, a la derecha; el MES se conecta al
disco. Chips de estado anclados a máquinas. Colores vía var(--*) del CSS
compartido. Uso: python3 build_hero_iso.py
"""
import math, re, pathlib

U = 32.0
CX = math.cos(math.radians(30)) * U
CY = math.sin(math.radians(30)) * U
CZ = 0.95 * U

STROKE = 'var(--icon)'
SW = '1.6'

_all_pts = []

def P(x, y, z=0.0):
    p = ((x - y) * CX, (x + y) * CY - z * CZ)
    _all_pts.append(p)
    return p

def pts(coords):
    return ' '.join(f'{px:.1f},{py:.1f}' for px, py in (P(*c) for c in coords))

def poly(coords, fill='var(--card)', w=SW, extra=''):
    return (f'<polygon points="{pts(coords)}" fill="{fill}" stroke="{STROKE}" '
            f'stroke-width="{w}" stroke-linejoin="round" {extra}/>')

def fpath(segs, fill, w=SW):
    d = []
    for seg in segs:
        if seg[0] == 'M':
            p = P(*seg[1]); d.append(f'M{p[0]:.1f},{p[1]:.1f}')
        elif seg[0] == 'L':
            p = P(*seg[1]); d.append(f'L{p[0]:.1f},{p[1]:.1f}')
        elif seg[0] == 'Q':
            c = P(*seg[1]); p = P(*seg[2])
            d.append(f'Q{c[0]:.1f},{c[1]:.1f} {p[0]:.1f},{p[1]:.1f}')
        else:
            d.append('Z')
    return (f'<path d="{" ".join(d)}" fill="{fill}" stroke="{STROKE}" '
            f'stroke-width="{w}" stroke-linejoin="round"/>')

def box(x, y, z, dx, dy, dz, top='var(--card)', right='var(--card)', front='var(--tint)'):
    return ''.join([
        poly([(x, y, z + dz), (x + dx, y, z + dz), (x + dx, y + dy, z + dz), (x, y + dy, z + dz)], top),
        poly([(x + dx, y, z), (x + dx, y + dy, z), (x + dx, y + dy, z + dz), (x + dx, y, z + dz)], right),
        poly([(x, y + dy, z), (x + dx, y + dy, z), (x + dx, y + dy, z + dz), (x, y + dy, z + dz)], front),
    ])

def shadow(cx, cy, rx, ry):
    c = P(cx, cy, -0.06)
    return f'<ellipse cx="{c[0]:.1f}" cy="{c[1]:.1f}" rx="{rx:.0f}" ry="{ry:.0f}" fill="var(--tint)"/>'

def dotted(coords, op=0.8, w=2.5):
    d = 'M ' + ' L '.join(f'{px:.1f} {py:.1f}' for px, py in (P(*c) for c in coords))
    return (f'<path d="{d}" fill="none" stroke="var(--line)" stroke-width="{w}" '
            f'stroke-opacity="{op}" stroke-linecap="round" stroke-dasharray="0.1 8"/>')

def chip(sx, sy):
    return (f'<g><rect x="{sx:.0f}" y="{sy:.0f}" width="112" height="32" rx="16" fill="var(--card)" '
            f'stroke="var(--border)" stroke-width="1.5"/>'
            f'<circle cx="{sx + 20:.0f}" cy="{sy + 16:.0f}" r="9" fill="var(--band)"/>'
            f'<path d="M{sx + 15.8:.0f},{sy + 16:.0f} l3,3 l5.5,-6" fill="none" stroke="var(--band-text)" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<rect x="{sx + 36:.0f}" y="{sy + 9:.0f}" width="55" height="5" rx="2.5" fill="var(--line)"/>'
            f'<rect x="{sx + 36:.0f}" y="{sy + 19:.0f}" width="36" height="5" rx="2.5" fill="var(--tint)" '
            f'stroke="var(--border)" stroke-width="1"/></g>')

def cnc(x, y):
    """Torno CNC calcado de la referencia: cabina con ventana inclinada (extremo
    up-right), bancada inclinada oscura con tapa del husillo, armario con panel
    de control, rejilla de ventilación y chimenea trasera."""
    L, D = 5.4, 2.1
    H = 2.8
    zb = 0.28
    yc = 2.0                 # fin de la cabina
    ys = 3.3                 # fin de la bancada inclinada / inicio del armario
    X = x + D
    ZT = zb + H

    s = shadow(x + D / 2, y + L / 2, (D + L) * CX * 0.5, (D + L) * CY * 0.5)
    s += box(x - 0.13, y - 0.50, 0, D + 0.26, L + 0.68, zb, 'var(--tint)')

    # --- cabina (ventana inclinada) ---
    tw = 0.50
    zw = zb + 1.35
    def wt(t, yy):
        return (X - tw * t, yy, zw + (ZT - zw) * t)
    s += fpath([('M', (x, y + yc, zb)), ('L', (x, y + yc, ZT)),
                ('L', (X - tw, y + yc, ZT)), ('L', (X, y + yc, zw)),
                ('L', (X, y + yc, zb)), ('Z',)], 'var(--tint)')
    s += poly([(X, y, zb), (X, y + yc, zb), (X, y + yc, zw), (X, y, zw)], 'var(--card)')
    s += poly([wt(0, y), wt(0, y + yc), wt(1, y + yc), wt(1, y)], 'var(--card)')
    s += poly([wt(0.10, y + 0.20), wt(0.10, y + yc - 0.18),
               wt(0.88, y + yc - 0.18), wt(0.88, y + 0.20)], 'var(--glass)', '1.2')
    a, b = P(*wt(0.30, y + 0.12)), P(*wt(0.62, y + 0.12))
    s += (f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
          f'stroke="{STROKE}" stroke-width="3" stroke-linecap="round"/>')
    s += poly([(x, y, ZT), (X - tw, y, ZT), (X - tw, y + yc, ZT), (x, y + yc, ZT)], 'var(--card)')

    # --- bancada inclinada oscura ---
    xr = 0.70
    zr = zb + 2.15
    zf = zb + 0.85
    s += poly([(x, y + yc, zr), (x + xr, y + yc, zr), (x + xr, y + ys, zr), (x, y + ys, zr)],
              'var(--card)')
    s += poly([(x + xr, y + yc, zr), (x + xr, y + ys, zr), (X, y + ys, zf), (X, y + yc, zf)],
              'var(--line)')
    cq = [P(x + xr, y + yc, zr), P(x + xr, y + ys, zr), P(X, y + ys, zf), P(X, y + yc, zf)]
    ex = sum(q[0] for q in cq) / 4; ey = sum(q[1] for q in cq) / 4
    s += (f'<ellipse cx="0" cy="0" rx="21" ry="14" fill="var(--tint)" opacity=".9" '
          f'transform="translate({ex:.1f},{ey:.1f}) rotate(-30)"/>')
    s += poly([(X, y + yc, zb), (X, y + ys, zb), (X, y + ys, zf), (X, y + yc, zf)],
              'var(--card)')
    s += box(x + 0.06, y + yc + 0.12, zr, 0.55, 0.70, 0.75)                  # chimenea

    # --- armario ---
    s += poly([(x, y + L, zb), (X, y + L, zb), (X, y + L, ZT), (x, y + L, ZT)], 'var(--tint)')
    s += poly([(X, y + ys, zb), (X, y + L, zb), (X, y + L, ZT), (X, y + ys, ZT)], 'var(--card)')
    s += poly([(x, y + ys, ZT), (X, y + ys, ZT), (X, y + L, ZT), (x, y + L, ZT)], 'var(--card)')

    def fq(y0, z0, w, h, fill, sw=SW):
        return poly([(X, y0, z0), (X, y0 + w, z0), (X, y0 + w, z0 + h), (X, y0, z0 + h)], fill, sw)

    py0, pz0 = y + 3.72, zb + 0.88
    s += fq(py0, pz0, 1.10, 1.18, 'var(--card)')
    s += fq(py0 + 0.09, pz0 + 0.58, 0.50, 0.42, 'var(--band)', '1')          # pantalla
    for k in range(2):
        d0 = P(X, py0 + 0.72 + k * 0.19, pz0 + 0.96)
        s += f'<circle cx="{d0[0]:.1f}" cy="{d0[1]:.1f}" r="1.7" fill="{STROKE}"/>'
    d0 = P(X, py0 + 0.79, pz0 + 0.66)                                        # botón de marcha
    s += (f'<circle cx="{d0[0]:.1f}" cy="{d0[1]:.1f}" r="3.2" fill="var(--band)"/>'
          f'<circle cx="{d0[0]:.1f}" cy="{d0[1]:.1f}" r="1.2" fill="var(--band-text)"/>')
    for j in range(2):
        for k in range(4):
            d0 = P(X, py0 + 0.13 + k * 0.19, pz0 + 0.36 - j * 0.19)
            s += f'<circle cx="{d0[0]:.1f}" cy="{d0[1]:.1f}" r="1.4" fill="{STROKE}"/>'
    for j in range(4):                                                        # ventilación lateral
        for k in range(5):
            d0 = P(x + 0.32 + k * 0.28, y + L, zb + 0.36 + j * 0.24)
            s += f'<circle cx="{d0[0]:.1f}" cy="{d0[1]:.1f}" r="1.3" fill="var(--line)"/>'
    return s

def minipc(x, y):
    """Mini-PC industrial (edge): caja con aletas de refrigeración y 2 antenas."""
    w, d, h = 2.4, 1.5, 0.85
    s = shadow(x + w / 2, y + d / 2, (w + d) * CX * 0.62, (w + d) * CY * 0.62)
    s += box(x, y, 0, w, d, h, 'var(--card)', 'var(--card)', 'var(--tint)')
    for i in range(7):                                                        # aletas
        s += box(x + 0.14 + i * 0.31, y + 0.14, h, 0.16, d - 0.28, 0.42,
                 'var(--card)', 'var(--tint)', 'var(--tint)')
    for ax, ay in ((x + w - 0.18, y + 0.22), (x + w - 0.18, y + 0.62)):       # antenas
        a, b = P(ax, ay, h + 0.42), P(ax, ay, h + 1.75)
        s += (f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
              f'stroke="{STROKE}" stroke-width="3.4" stroke-linecap="round"/>'
              f'<circle cx="{b[0]:.1f}" cy="{b[1]:.1f}" r="3.2" fill="{STROKE}"/>')
    for k in range(2):                                                        # LEDs frontales
        d0 = P(x + 0.28 + k * 0.28, y + d, 0.42)
        s += f'<circle cx="{d0[0]:.1f}" cy="{d0[1]:.1f}" r="1.9" fill="var(--band)"/>'
    s += poly([(x + w - 0.85, y + d, 0.30), (x + w - 0.25, y + d, 0.30),
               (x + w - 0.25, y + d, 0.52), (x + w - 0.85, y + d, 0.52)], 'var(--tint)', '1.2')
    return s

def mes(x, y):
    s = shadow(x + 1.6, y + 0.7, 3.2 * CX, 3.2 * CY)
    s += box(x + 0.5, y, 0, 2.1, 1.3, 0.21)
    s += box(x + 1.28, y + 0.48, 0.21, 0.44, 0.34, 1.04)
    s += box(x, y + 0.36, 1.25, 3.1, 0.18, 2.05)
    fy = y + 0.54
    def fq(x0, z0, w, h, fill, sw=SW):
        return poly([(x0, fy, z0), (x0 + w, fy, z0), (x0 + w, fy, z0 + h), (x0, fy, z0 + h)], fill, sw)
    s += fq(x + 0.14, 3.02, 2.82, 0.27, 'var(--band)', '0')
    s += fq(x + 0.14, 1.39, 2.82, 1.52, 'var(--card)', '1.2')
    for i, w in enumerate((2.3, 1.35, 1.85, 1.0)):
        s += fq(x + 0.32, 2.62 - i * 0.35, w, 0.19, 'var(--tint)', '1')
    a = P(x + 0.44, fy, 3.11)
    s += (f'<text x="{a[0]:.1f}" y="{a[1]:.1f}" font-size="12" font-weight="600" fill="var(--band-text)" '
          f'transform="matrix(0.866,0.5,0,1,0,0)" transform-origin="{a[0]:.1f} {a[1]:.1f}" '
          f'style="font-family: var(--sans);">MES</text>')
    return s

def cmm(x, y):
    s = shadow(x + 1.45, y + 1.1, 3.6 * CX, 3.6 * CY)
    s += box(x, y, 0, 2.9, 2.2, 0.80)
    s += box(x + 1.22, y + 0.86, 0.80, 0.61, 0.49, 0.37)
    s += box(x + 0.14, y + 0.92, 0.80, 0.30, 0.30, 1.94)
    s += box(x + 2.43, y + 0.92, 0.80, 0.30, 0.30, 1.94)
    s += box(x + 0.01, y + 0.88, 2.74, 2.85, 0.39, 0.33)
    a, b = P(x + 1.52, y + 1.07, 2.74), P(x + 1.52, y + 1.07, 1.30)
    s += (f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" '
          f'stroke="{STROKE}" stroke-width="2.4"/>')
    s += f'<circle cx="{b[0]:.1f}" cy="{b[1]:.1f}" r="3.8" fill="{STROKE}"/>'
    return s

def disc(ix, iy):
    """Disco SVA (más pequeño), colocado en coordenadas iso (ix, iy)."""
    r, h = 1.55, 0.55
    rx, ry = r * math.sqrt(2) * CX, r * math.sqrt(2) * CY
    top = -h * CZ
    c = P(ix, iy)
    for ddx, ddy in ((2.6, 0), (-2.6, 0), (0, 2.6), (0, -2.6)):   # extiende los límites
        P(ix + ddx, iy + ddy, 1.2)
    s = f'<g transform="translate({c[0]:.1f},{c[1]:.1f})">'
    s += f'<ellipse cx="0" cy="0" rx="{rx + 22:.0f}" ry="{ry + 13:.0f}" fill="var(--tint)" opacity=".55"/>'
    s += (f'<path d="M{-rx:.1f},{top:.1f} L{-rx:.1f},0 A{rx:.1f},{ry:.1f} 0 0 0 {rx:.1f},0 '
          f'L{rx:.1f},{top:.1f}" fill="var(--band)"/>')
    s += f'<ellipse cx="0" cy="{top:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="var(--band)" stroke="var(--band)"/>'
    s += (f'<g transform="translate(0,{top:.1f}) scale(0.82,0.47) translate(-52,-49)">'
          f'<g fill="var(--band-text)"><rect x="-80" y="-80" width="260" height="260" mask="url(#ma)"/>'
          f'<g transform="translate(15.32 -12.86) translate(50 50) rotate(-40) scale(1 -1) rotate(40) translate(-50 -50)">'
          f'<rect x="-80" y="-80" width="260" height="260" mask="url(#mb)"/></g></g></g>')
    s += '</g>'
    return s

parts = []
# pasillo central (dirección y) con el mini-PC; tronco grueso hacia el disco SVA
parts.append(dotted([(0, -8.2), (0, 7.2)]))
parts.append(dotted([(0, -1.8), (0, -8.0)], op=1.0, w=2.9))
# conexiones cortas de cada elemento al pasillo (simétricas)
parts.append(dotted([(-4.35, -7.7), (0, -7.7)]))   # CMM
parts.append(dotted([(-4.35, -2.4), (0, -2.4)]))   # m1
parts.append(dotted([(-4.35, 5.4), (0, 5.4)]))     # m2
parts.append(dotted([(4.35, -6.4), (0, -6.4)]))    # MES
parts.append(dotted([(4.35, -0.6), (0, -0.6)]))    # m3
parts.append(dotted([(4.35, 7.2), (0, 7.2)]))      # m4
# elementos, de atrás hacia delante
parts.append(cmm(-7.3, -8.8))    # CMM (cabeza de la fila trasera)
parts.append(disc(-0.8, -8.8))   # disco SVA (final del pasillo)
parts.append(cnc(-6.5, -5.2))    # m1 (fila trasera)
parts.append(mes(4.4, -7.2))     # pantalla (cabeza de la fila delantera)
parts.append(minipc(-1.2, -1.2)) # mini-PC (centro del pasillo)
parts.append(cnc(-6.5, 2.6))     # m2 (fila trasera)
parts.append(cnc(4.4, -3.4))     # m3 (fila delantera)
parts.append(cnc(4.4, 4.4))      # m4 (fila delantera)

body = ''.join(parts)

chip_boxes = []
chips_svg = ""

xs = [p[0] for p in _all_pts] + [c[0] + o for c in chip_boxes for o in (0, 112)]
ys = [p[1] for p in _all_pts] + [c[1] + o for c in chip_boxes for o in (0, 32)]
x0, x1 = min(xs) - 24, max(xs) + 24
y0, y1 = min(ys) - 30, max(ys) + 42

svg = (f'<svg viewBox="{x0:.0f} {y0:.0f} {x1 - x0:.0f} {y1 - y0:.0f}" role="img" '
       f'aria-label="Planta isométrica: tornos CNC y control de calidad conectados a un '
       f'mini-PC industrial que envía los datos al hub SVA; el MES se conecta al hub">'
       f'\n{body}\n{chips_svg}\n</svg>')

p = pathlib.Path(__file__).resolve().parent.parent / 'index.html'
html = p.read_text(encoding='utf-8')
new, n = re.subn(r'(?s)<div class="diagram[^"]*hero-dia">.*?</svg>\s*</div>',
                 '<div class="diagram hero-dia">\n      ' + svg + '\n    </div>', html)
assert n == 1, f'hero-dia block matches: {n}'
p.write_text(new, encoding='utf-8')
print(f'ok — viewBox {x0:.0f} {y0:.0f} {x1 - x0:.0f} {y1 - y0:.0f}')
