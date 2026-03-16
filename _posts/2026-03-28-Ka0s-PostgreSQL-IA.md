---
layout: post
title: "Ka0s: PostgreSQL-IA (la memoria a largo plazo)"
subtitle: "Embeddings, metadatos y aislamiento del core"
cover-img: /assets/img/kaos-core.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-core.png
tags: [post, ka0s, postgresql, pgvector, ai, memory]
author: Ka0s
---

Una IA operativa sin memoria termina improvisando. Y la improvisación es cara.

En Ka0s, `postgresql-ia` es la pieza que actúa como **memoria a largo plazo** del sistema de IA.

Según `core/docs/ka0s_postgresql_ia/01_concept.md`, esta base almacena:

1. Embeddings.
2. Metadatos (fuente, fechas, hashes).
3. Historial (opcional).

## Aislamiento por diseño

Un punto clave es que `postgresql-ia` está **separado** de la base principal (`ka0s_core`).

¿Por qué?

- rendimiento: el vector store tiene patrones de IO y de índices distintos,
- operación: dimensionas memoria/CPU según búsqueda vectorial,
- seguridad: credenciales rotadas y scope claro.

## Qué gana el sistema

- Recuperación de contexto basada en datos reales.
- Consistencia: `source` + `record_id` + `chunk_id`.
- Evolución: puedes reingestar por versiones sin romper la operación.

