---
layout: post
title: "Ka0s: GitOps para IA en Kubernetes"
subtitle: "Reproducibilidad, control de cambios y operación predecible"
cover-img: /assets/img/workflow-ka0s.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/workflow-ka0s.png
tags: [post, ka0s, gitops, kubernetes, ci-cd, ai]
author: Ka0s
---

Cuando tu IA controla operación, la pregunta no es si funciona hoy. La pregunta es si **puedes reproducirla mañana**.

## Qué significa GitOps aquí

- Infraestructura declarativa (manifiestos Kubernetes).
- Cambios revisables (PRs, diffs claros).
- Entornos repetibles.

En Ka0s, esto se refleja en:

- `core/b2b/core-services/*` (servicios del cluster)
- `.github/workflows/*` (automatización)
- `core/docs/*` (la “verdad” del sistema)

## Por qué importa para el knowledge pipeline

- Cambiar el modelo de embeddings o la dimensión afecta a la base de conocimiento.
- Separar `ollama-gen`/`ollama-embed` es una decisión operativa.
- Ajustar límites o watermarks es un control de riesgo.

GitOps permite que todo eso sea:

- auditado,
- versionado,
- y reversible.

Mañana: observabilidad. Sin métricas, la IA es solo “fe”.

