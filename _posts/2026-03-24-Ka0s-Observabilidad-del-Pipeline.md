---
layout: post
title: "Ka0s: Observabilidad del Pipeline"
subtitle: "Métricas y señales para operar una ingesta continua"
cover-img: /assets/img/kaos-summary.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-summary.png
tags: [post, ka0s, observability, zabbix, kubernetes, data]
author: Ka0s
---

Si el pipeline de conocimiento corre cada noche, tarde o temprano fallará.

La diferencia entre “fallo controlado” y “misterio” es observabilidad.

## Qué señales hay que vigilar

En Ka0s, un pipeline sano debería exponer (mínimo):

- número de registros procesados (`docs/rows`),
- número de chunks (`chunks`),
- latencia por embeddings,
- tamaño del spool,
- tiempo del loader,
- y crecimiento de `postgresql-ia`.

## Dónde viven esas señales hoy

- `manifest.json` por `run_id` en el spool.
- logs de Jobs/CronJobs.
- métricas del propio cluster (CPU/IO).

Y, cuando toque, lo natural es conectarlo con:

- `core/docs/ka0s_zabbix_iac/`
- o dashboards (Metabase) para entender el crecimiento del vector store.

Mañana: cómo convertimos ITIL/CMDB en conocimiento accionable.

