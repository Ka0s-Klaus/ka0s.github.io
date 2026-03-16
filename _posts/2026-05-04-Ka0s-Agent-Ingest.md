---
layout: post
title: "Ka0s: Agent Ingest (modular)"
subtitle: "Vectorizar el repo sin timeouts: módulos, triggers y optimización"
cover-img: /assets/img/kaos-secrets.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-secrets.png
tags: [post, ka0s, ai, ingest, pgvector, github-actions]
author: Ka0s
---

Ingerir “todo el repo” de una vez es la receta perfecta para timeouts.

Por eso `core/docs/ka0s_agent_ingest/00_main.md` define una **estrategia modular**:

- `skills`, `docs`, `infra`, `audit`, `compliance`, `devops`, `github`, `code`.

Cada módulo se activa por cambios en rutas específicas y permite refrescar solo lo que cambió, manteniendo la memoria del agente actualizada sin castigar recursos.

