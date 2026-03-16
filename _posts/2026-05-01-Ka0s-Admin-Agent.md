---
layout: post
title: "Ka0s: Admin Agent"
subtitle: "Un agente de administración con memoria y capacidad de acción"
cover-img: /assets/img/AI2.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/AI2.png
tags: [post, ka0s, agent, ai, kubernetes, operations]
author: Ka0s
---

El **Admin Agent** es la visión de un operador automatizado: aprende de auditorías y ejecuta acciones con contexto.

El diseño técnico vive en `core/docs/admin-agent/design.md`.

## Qué integra

- Ingesta de logs de auditoría.
- Motor IA local (Ollama) + memoria vectorial (PostgreSQL/pgvector).
- Contexto histórico (MongoDB).
- Ejecución de acciones (API de Kubernetes) y notificaciones.

La idea clave: **no solo responde**, también **actúa** y deja evidencia.

