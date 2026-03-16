---
layout: post
title: "Ka0s: Hardware y viabilidad"
subtitle: "Diseñar automatización según recursos reales"
cover-img: /assets/img/kaos-summary.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-summary.png
tags: [post, ka0s, hardware, capacity, finops, operations]
author: Ka0s
---

Ka0s se diseña para entornos reales, no ideales.

En `core/docs/hardware/` y en el análisis de viabilidad del Admin Agent (`core/docs/admin-agent/design.md`) aparece una idea recurrente:

- asignar roles por nodo según CPU/RAM,
- separar servicios intensivos (IA/embeddings) de los críticos,
- y dimensionar almacenamiento según evidencias y auditorías.

Operar bien es, primero, respetar los límites físicos.

