---
layout: post
title: "Ka0s: Dashboard"
subtitle: "Kanban, estado del trabajo y transparencia operativa"
cover-img: /assets/img/kaos-init.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-init.png
tags: [post, ka0s, dashboard, kanban, operations]
author: Ka0s
---

Una plataforma sin visibilidad termina siendo “una caja negra con scripts”.

El Dashboard de Ka0s (ver `core/docs/ka0s_dashboard/01_concept.md`) nace con una idea sencilla:

- representar el trabajo como estados claros (`backlog`, `in_progress`, `done`),
- y exponerlo de forma visual siguiendo Kanban.

## Arquitectura deliberadamente simple

La documentación define un enfoque pragmático:

- Frontend estático o apoyado en visualización de GitHub Projects.
- Backend basado en JSON que representa el estado del flujo.

Esto tiene una ventaja brutal en operaciones: menos complejidad, menos puntos de fallo.

## Qué cambia para el equipo

- Transparencia: todos ven el estado real.
- Trazabilidad: el trabajo se conecta con Issues, workflows y auditorías.
- Ritmo: el sistema favorece flujo continuo (Kaizen), no “big bangs”.

