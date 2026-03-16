---
layout: post
title: "Ka0s: Project Routing (nativo)"
subtitle: "Asignar issues a Projects sin workflows ni tokens"
cover-img: /assets/img/kaos-version.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-version.png
tags: [post, ka0s, github, projects, issues, automation]
author: Ka0s
---

La mejor automatización es la que **no ejecutas**.

Ka0s documenta en `core/docs/ka0s_project_routing/01_concept.md` un cambio elegante: enrutamiento de Issues a Projects usando capacidades nativas.

## Antes

Un workflow (`project-routing.yml`) con scripts y llamadas a API:

- latencia,
- fallos por runners/tokens,
- mantenimiento extra.

## Ahora

GitHub Issue Forms permite definir el Project en el front matter de la plantilla:

```yaml
projects: ["Ka0s-Klaus/4"]
```

Resultado:

- el issue entra al proyecto en el momento de crearse,
- sin depender de ejecución asíncrona,
- y con menos superficie de ataque.
