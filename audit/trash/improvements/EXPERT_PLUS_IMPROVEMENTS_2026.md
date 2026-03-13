# Ka0s Blog (`ka0s.github.io`) — Expert Plus Improvements 2026

**Fecha:** 2026-03-13  
**Objetivo:** reforzar el blog como “Knowledge Base” pública: SEO sólido, reproducibilidad del build, performance real y DX editorial.

## Resumen ejecutivo

- P0: URLs/canonical consistentes (`url/baseurl`), preservación de dominio custom (CNAME) y build reproducible en CI.
- P1: CI de calidad en PR (build + links + HTML), y media web-friendly (mp4/webm + posters).
- P2: búsqueda, SEO avanzado, optimización de imágenes y dependencia controlada.

## Mejoras recomendadas (Expert+)

### P0 — SEO/URLs (sin esto el sitio “miente” a Google)

- **Config única y consistente**: asegurar `url: https://blog.ka0s.io` y `baseurl: ""`.
- **Canonical/OG/Twitter correctos**: evitar meta tags inválidas si faltan handles; asegurar `og:image` estable.
- **Dominio custom**: garantizar que `CNAME` llega a `_site/` en el deploy.

### P1 — CI editorial (calidad antes de publicar)

- **Workflow PR**: `bundle exec jekyll build` + link checker + validación front matter.
- **Dependabot**: actualizaciones de actions y dependencias del build.

### P1 — Media y performance

- **Vídeos**: migrar `.mov` a `mp4 (h264)` + `webm`; usar tipos MIME correctos; `preload="metadata"` y `poster`.
- **Imágenes**: generar `webp/avif`, thumbnails dedicados para listados, y lazy-loading para contenido largo.

### P2 — Búsqueda y DX

- **Fijar dependencias externas** (evitar `@latest`) o servir local.
- **Include reutilizable para vídeo** (evita HTML duplicado en posts).
- **Guía editorial**: convenciones de posts, assets, naming y tamaño máximo recomendado.

## Plan de ejecución sugerido (3 PRs)

1) **SEO & Domain Safety**: `url/baseurl` + canonical/OG + CNAME.
2) **CI de PR**: build + links + dependabot.
3) **Media Modernization**: transcodificación vídeos + includes + optimización imágenes.

## Métricas de éxito

- 0 enlaces absolutos al dominio incorrecto
- Build reproducible y validado en PR
- Reducción de peso medio por post (imágenes/vídeo) y mejora Lighthouse

