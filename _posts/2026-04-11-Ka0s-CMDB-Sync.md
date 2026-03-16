---
layout: post
title: "Ka0s: CMDB Sync"
subtitle: "Upsert desde CD: que la CMDB refleje la realidad del despliegue"
cover-img: /assets/img/ka0s-actividad.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/ka0s-actividad.png
tags: [post, ka0s, cmdb, itop, cd, automation]
author: Ka0s
---

La CMDB solo sirve si describe lo que **existe de verdad**.

El módulo **CMDB Sync** (`core/docs/ka0s_cmdb_sync/01_concept.md`) automatiza el ciclo de vida de CIs para que cada despliegue exitoso quede reflejado en iTop.

## La estrategia: Upsert por eventos

- Fuente de verdad: repo + pipelines.
- Trigger: despliegue exitoso.
- Acción: `itop-cmdb-sync.py` decide si crea o actualiza.
- Modelo: `ApplicationSolution` para representar microservicios.

## Auditoría nativa

Cada ejecución genera un JSON en `audit/cmdb/` con:

- operaciones realizadas,
- cambios aplicados,
- y errores.

Así, la CMDB no es “lo que alguien dijo”, es evidencia automatizada.

