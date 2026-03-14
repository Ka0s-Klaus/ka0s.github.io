# ka0s.github.io - Reglas de Proyecto (Main)

Este repositorio publica el **blog** de Ka0s en GitHub Pages.

## Dominios del Repo

- **Sitio**: Jekyll (contenido en `_posts/`, configuración en `_config.yml`).
- **Despliegue**: GitHub Pages vía workflow `.github/workflows/deploy-jekyll.yml`.
- **Contenido**: cada post debe respetar formato y coherencia editorial.

## Reglas Clave

- Todo cambio entra por PR.
- Los posts se versionan en `_posts/` y deben seguir nomenclatura `YYYY-MM-DD-titulo.md`.
- No introducir dependencias ni scripts sin justificar impacto (performance, seguridad).
- Si se cambia la estructura de documentación interna, ejecutar `.github/scripts/update-docs-index.py`.

