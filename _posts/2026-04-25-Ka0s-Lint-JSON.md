---
layout: post
title: "Ka0s: Lint JSON"
subtitle: "Validación dual y self-healing para configuración como código"
cover-img: /assets/img/kaos-json.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-json.png
tags: [post, ka0s, json, quality, github-actions, automation]
author: Ka0s
---

Si configuras tu plataforma con JSON, validar es operar.

**Ka0s Lint JSON** (`core/docs/ka0s_json/01_concept.md`) es una composite action que estandariza la calidad de los `.json`.

## Validación dual

1. Hard check: `jsonlint`
   - la sintaxis rota no se negocia.
2. Soft check: `prettier`
   - estilo consistente para PRs limpios.

## Self-healing

Con `fix: true`, si el JSON es válido pero está mal formateado, el workflow puede auto-corrigir con `prettier --write`.

