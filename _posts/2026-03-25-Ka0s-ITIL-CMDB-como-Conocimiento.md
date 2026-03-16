---
layout: post
title: "Ka0s: ITIL y CMDB como conocimiento"
subtitle: "Cuando los tickets y los CIs dejan de ser histórico y se vuelven contexto"
cover-img: /assets/img/kaos-issue.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-issue.png
tags: [post, ka0s, itil, cmdb, ai, operations]
author: Ka0s
---

Las plataformas ITSM suelen ser “archivos”.

Ka0s las trata como un **motor de contexto**.

## Por qué es vital

Cuando un agente responde a un incidente, lo que necesita no es solo manuales:

- necesita historial de incidentes similares,
- cambios recientes,
- relaciones CMDB,
- y patrones de resolución.

## Cómo lo aterrizamos

La ingesta desde MySQL ITIL y el trabajo con CMDB están documentados en:

- `core/docs/ka0s_itil_sync/`
- `core/docs/ka0s_cmdb_ingest/`
- `core/docs/ka0s_cmdb_sync/`

La idea: convertir entidades (incidente/cambio/problema/CI) en chunks, vectorizarlos y dejarlos disponibles para retrieval.

## La clave de calidad

En ITIL no gana quien ingiere más, gana quien ingiere mejor:

- allowlist por entidad,
- redacción de campos sensibles,
- incrementalidad por `updated_at`,
- y `record_id` estable por PK.

Con esto, la memoria deja de ser un “backup vectorial” y se convierte en una ventaja operativa.

