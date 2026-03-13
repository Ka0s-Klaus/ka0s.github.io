---
title: "Incident: GitHub Pages publish failure"
date: 2026-03-13
service: "ka0s.github.io"
severity: "high"
status: "mitigated"
---

## Síntomas

- Fallo del job de publicación (GitHub Pages) con errores de Bundler/Jekyll.
- Error de Git: `fatal: detected dubious ownership in repository at '/github/workspace'`.
- Error de Jekyll: `The beautiful-jekyll theme could not be found`.

## Causa raíz

- `_config.yml` referenciaba `theme: beautiful-jekyll`, pero el gem del tema es `beautiful-jekyll-theme` (gemspec local). Jekyll buscaba un gem inexistente (`beautiful-jekyll`).
- El runner ejecutaba comandos `git` y Git bloqueaba el workspace por safe.directory.

## Mitigación aplicada

- Cambiado `_config.yml` a `theme: beautiful-jekyll-theme`.
- Se evitó `actions/jekyll-build-pages@v1` (Docker), ya que el `safe.directory` se aplica fuera del contenedor.
- Build actualizado a Bundler (`ruby/setup-ruby` + `bundle exec jekyll build`) para que instale el gem local del tema (via `gemspec`).
- Se mantiene `git config --global --add safe.directory "$GITHUB_WORKSPACE"` antes del build.

## Notas

- El workflow usa GitHub Actions para build+deploy, lo que permite controlar dependencias frente al entorno restringido de GitHub Pages.
