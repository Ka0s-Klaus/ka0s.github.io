---
layout: post
title: "Ka0s: CMDB Ingestion"
subtitle: "CIs como código: definir infraestructura en JSON y sincronizar con iTop"
cover-img: /assets/img/kaos-json.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-json.png
tags: [post, ka0s, cmdb, itop, gitops, configuration-as-code]
author: Ka0s
---

Una CMDB útil no se “rellena”: se gobierna.

El módulo **CMDB Ingestion** (`core/docs/ka0s_cmdb_ingest/01_concept.md`) aplica IaC a la CMDB: definimos CIs en archivos del repositorio y sincronizamos automáticamente con iTop.

## Qué resuelve

- Centralización: los CIs viven en Git.
- Automatización: no dependes de clicks en una UI.
- Trazabilidad: cada cambio de CI tiene historial.
- Relaciones inteligentes: resolución de claves foráneas por nombre.

## Cómo se modela

Los CIs se describen en JSON (por ejemplo un `Server`) y se almacenan en `devops/core/cmdb` siguiendo plantillas de `core/templates/cmdb`.

El resultado es simple: la CMDB deja de ser un “catálogo manual” y se convierte en una extensión operable del repositorio.

