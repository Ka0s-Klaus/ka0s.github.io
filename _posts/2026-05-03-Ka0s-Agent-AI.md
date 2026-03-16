---
layout: post
title: "Ka0s: Agent AI"
subtitle: "RAG en producción: Issues como interfaz y memoria vectorial"
cover-img: /assets/img/ka0s-ecosistema.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/ka0s-ecosistema.png
tags: [post, ka0s, ai, rag, github, automation]
author: Ka0s
---

El módulo **Ka0s Agent AI** (`core/docs/ka0s_agent_ai/00_main.md`) es la capa cognitiva del framework.

## Arquitectura

- Memoria vectorial: PostgreSQL + `pgvector`.
- Inferencia local: modelos ligeros en Kubernetes (Ollama).
- GitOps: workflows en GitHub Actions.

## La interfaz es GitHub

El usuario pregunta en una Issue y el agente responde en el mismo hilo, apoyándose en retrieval (RAG) sobre el repositorio.

