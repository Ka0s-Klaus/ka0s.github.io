---
layout: post
title: "Ka0s: Seguridad en la Memoria"
subtitle: "Denylist, allowlist y reducción del riesgo"
cover-img: /assets/img/kaos-secrets.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-secrets.png
tags: [post, ka0s, security, data, rag, compliance]
author: Ka0s
---

Un RAG sin gobernanza puede convertirse en un problema: si la fuente contiene tokens, passwords o datos sensibles, los embeddings no “olvidan”.

## La regla

Antes de chunking/embeddings, **normalizamos** y filtramos campos.

- `*_ALLOW_FIELDS`: si existe, solo pasan esos.
- `*_DENY_FIELDS`: siempre se eliminan.

Esto es especialmente importante en ITIL (MySQL), donde es habitual encontrar campos con:

- credenciales, claves API,
- datos personales,
- notas internas.

## Estrategia práctica

1. Empezar con una denylist fuerte (tokens/secret/api_key/etc.).
2. Para entidades ITIL, ir a allowlist por tabla (incidentes, cambios, problemas).
3. Mantener el spool sin credenciales (las credenciales viven en Secrets de Kubernetes).

El enfoque está alineado con `core/docs/ka0s_security/` y con el diseño del pipeline.

Mañana: GitOps. Cómo encaja todo esto en un flujo de despliegue reproducible.

