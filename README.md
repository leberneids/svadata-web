# svadata.com

Web pública de **SVA Data**. Sitio estático, sin build: lo que hay en el repo es
exactamente lo que se sirve.

```
index.html          portada
servicios.html      servicios
assets/styles.css   estilos (único CSS)
assets/sva-favicon.svg
assets/build_hero_iso.py   genera la ilustración isométrica del hero
assets/build_shots.py      captura el portal real (datos sintéticos) -> assets/img/
assets/img/                capturas de producto + la imagen de Open Graph
CNAME               dominio principal para GitHub Pages — no borrar
robots.txt · sitemap.xml
contenido_web.md    copy en markdown, fuente de los textos
```

## Desplegar

`git push` a `main`. GitHub Pages reconstruye en ~1 minuto y publica en
<https://svadata.com>. No hay panel que tocar.

## Regenerar las capturas

Las imágenes de `assets/img/` son capturas del portal real corriendo contra un
taller sintético (CNC-01…CNC-08), nunca contra un cliente. Se rehacen con:

```bash
~/.venvs/web-fetch/bin/python assets/build_shots.py
```

Antes hay que levantar el portal con los datos de demo — el procedimiento completo
está en el runbook del vault, `02_Projects/00_Guias/03_desplegar_web_svadata.md`.

## Desarrollo local

Abrir `index.html` en el navegador, o servir la carpeta:

```bash
python3 -m http.server 8000
```

## Notas

- Dos dependencias externas: Fontshare (Switzer) y Google Fonts (Source Serif 4).
- El fichero `CNAME` es lo que ata el dominio al sitio. Si se borra, Pages deja de
  servir en `svadata.com`.
- Sitio estático: no procesa formularios y no debe contener nunca claves ni tokens
  (el navegador los descargaría, quedando públicos).
