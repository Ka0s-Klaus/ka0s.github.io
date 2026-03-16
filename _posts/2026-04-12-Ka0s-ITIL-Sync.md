---
layout: post
title: "Ka0s: ITIL Sync"
subtitle: "Configuration as Code para catálogo, equipos y personas en iTop"
cover-img: /assets/img/ka0s-ecosistema.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/ka0s-ecosistema.png
tags: [post, ka0s, itil, itop, gitops, configuration]
author: Ka0s
---

No puedes operar un ITSM serio si su configuración vive en una UI sin control de cambios.

**ITIL Sync** (`core/docs/ka0s_itil_sync/01_concept.md`) sincroniza configuración ITIL desde YAML del repositorio hacia iTop:

- equipos (`Team`) y personas (`Person`),
- servicios (`Service`) y subcategorías,
- y, en roadmap, SLAs.

## La idea clave

La CMDB sigue siendo la “single source of truth”, pero se gestiona como **Configuration as Code**.

Resultado: cambios revisables, versionados y reproducibles.

