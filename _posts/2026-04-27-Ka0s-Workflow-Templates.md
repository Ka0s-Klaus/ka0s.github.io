---
layout: post
title: "Ka0s: Workflow Templates (Golden Path)"
subtitle: "Plantillas opinadas para seguridad, observabilidad y consistencia"
cover-img: /assets/img/kaos-summary.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-summary.png
tags: [post, ka0s, workflows, standards, security, observability]
author: Ka0s
---

El “Golden Path” de Ka0s (`core/docs/ka0s_template/01_concept.md`) no busca limitar.

Busca que lo correcto sea lo fácil.

## Estructura canónica

Todo workflow debería seguir 3 fases:

1. Inicialización (triggers, permisos mínimos, trazabilidad).
2. Job core (lógica de negocio, idempotencia, outputs).
3. Ciclo de vida y auditoría (`handle-success`, `handle-failure`, `end-workflow`).

## Beneficios

- Observabilidad uniforme.
- Seguridad por defecto (least privilege, anti-inyección).
- Mantenibilidad: mejoras en plantillas se propagan.
