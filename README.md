# svadata.com

Web pública de **SVA Data**. Sitio estático, sin build: lo que hay en el repo es
exactamente lo que se sirve.

```
index.html          portada
servicios.html      servicios
assets/styles.css   estilos (único CSS)
assets/sva-favicon.svg
assets/build_hero_iso.py   genera la ilustración isométrica del hero
CNAME               dominio principal para GitHub Pages — no borrar
robots.txt · sitemap.xml
contenido_web.md    copy en markdown, fuente de los textos
```

## Desplegar

`git push` a `main`. GitHub Pages reconstruye en ~1 minuto y publica en
<https://svadata.com>. No hay panel que tocar.

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
