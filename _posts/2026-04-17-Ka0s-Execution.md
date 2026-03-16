---
layout: post
title: "Ka0s: Execution"
subtitle: "El orquestador que decide qué se ejecuta, cuándo y en qué orden"
cover-img: /assets/img/kaos-execution.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-execution.png
tags: [post, ka0s, automation, orchestration, workflows]
author: Ka0s
---

En Ka0s, la automatización no es una colección de workflows sueltos.

Necesitas un motor que entienda dependencias, orden y contexto.

Eso es **Ka0s Execution** (`core/docs/ka0s_execution/01_concept.md`): el orquestador de tareas.

## Responsabilidades

- Gestión de dependencias: primero prerrequisitos, luego dependientes.
- Paralelismo: tareas independientes en simultáneo.
- Contexto: variables y estado entre jobs/workflows.

Cuando Execution está bien diseñado, el sistema se comporta como un pipeline coherente, no como scripts desperdigados.

