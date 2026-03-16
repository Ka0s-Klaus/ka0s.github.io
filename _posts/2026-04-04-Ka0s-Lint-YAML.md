---
layout: post
title: "Ka0s: Lint YAML"
subtitle: "Evitar caídas por un espacio: validación dual y self-healing"
cover-img: /assets/img/kaos-yamllint.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-yamllint.png
tags: [post, ka0s, yaml, github-actions, kubernetes, quality]
author: Ka0s
---

YAML es el pegamento de Kubernetes y GitHub Actions.

Y también es un campo minado: un error de indentación puede romper despliegues enteros.

Por eso existe **Ka0s Lint YAML** (`core/docs/ka0s_yaml/01_concept.md`).

## Validación dual

La acción aplica dos capas:

1. **Hard check** con `yamllint`
   - detecta errores estructurales.
2. **Soft check** con `prettier`
   - normaliza estilo para consistencia.

## Self-healing

Si el YAML es válido pero no cumple estilo, el sistema puede **autocorregir** con `fix: true`.

No es “cosmético”: reduce ruido en PRs y evita drift en manifiestos.

