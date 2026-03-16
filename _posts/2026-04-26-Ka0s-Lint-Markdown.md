---
layout: post
title: "Ka0s: Lint Markdown"
subtitle: "Docs as Code sin degradación: reglas, estilo y autocorrección"
cover-img: /assets/img/open_code.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/open_code.png
tags: [post, ka0s, markdown, docs, quality, prettier]
author: Ka0s
---

Si la documentación es parte del sistema, su calidad no puede depender de “quién la escribió”.

**Ka0s Lint Markdown** (`core/docs/ka0s_md/01_concept.md`) asegura consistencia en `.md` con dos capas:

- hard check con `markdownlint-cli` (estructura/reglas),
- soft check con `prettier` (formato y consistencia visual).

Con `fix: true`, puede autocorregir problemas comunes (`markdownlint --fix` + `prettier --write`).

Resultado: docs legibles, PRs más limpios y menos deuda invisible.

