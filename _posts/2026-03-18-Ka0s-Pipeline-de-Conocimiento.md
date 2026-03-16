---
layout: post
title: "Ka0s: Pipeline de Conocimiento"
subtitle: "Por qué desacoplamos la ingesta offline del plano online"
cover-img: /assets/img/ka0s-ecosistema.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/ka0s-ecosistema.png
tags: [post, ka0s, ai, rag, kubernetes, knowledge]
author: Ka0s
---

En una plataforma operativa real, **responder** y **aprender** son dos verbos distintos.

- Responder (online) exige **latencia baja** y disponibilidad.
- Aprender (offline) exige **throughput**, tiempo, CPU/IO y, a veces, horas de procesamiento.

En Ka0s lo convertimos en arquitectura: un **Knowledge Pipeline desacoplado**.

## El problema (cuando todo comparte lo mismo)

Vectorizar bases de datos completas (MongoDB, PostgreSQL, MySQL) implica:

- muchas lecturas,
- mucha CPU,
- muchas llamadas a embeddings,
- y mucha escritura en la Vector DB.

Si el mismo servicio de modelos atiende embeddings e inferencia interactiva, el agente sufre: colas, timeouts y respuestas lentas.

## La solución (3 planos)

El diseño en `core/docs/ka0s_agent_knowledge_pipeline/01_concept.md` propone separar explícitamente:

1. **Plano Online (Query)**
   - embeddings de la pregunta + búsqueda en pgvector + generación.
2. **Plano Offline (Ingesta)**
   - extracción/normalización/chunking + embeddings masivos.
3. **Plano Offline (Carga)**
   - UPSERT por lotes a PostgreSQL-IA (pgvector), con idempotencia.

Esta separación es el corazón del sistema: aunque haya un “batch” corriendo durante horas, el agente sigue respondiendo.

## Los componentes que lo hacen posible

- `ollama-gen` (generación, GPU, online)
- `ollama-embed` (embeddings, CPU, offline)
- `ka0s-knowledge` (extractores/normalizadores + spool + loader)
- `postgresql-ia` (Vector DB, pgvector)

La idea clave: **embeddings no compiten con la generación**.

## Qué te llevas como operador

- Prioridades claras (online primero).
- Ingesta controlable (batch, límites, retención en spool).
- Trazabilidad: `source`, `record_id`, `chunk_id`, `embedding_model`, `embedding_dim`.

Mañana: cómo pasamos de “spool” a “vector store” sin duplicados, y por qué el loader es tan importante.

