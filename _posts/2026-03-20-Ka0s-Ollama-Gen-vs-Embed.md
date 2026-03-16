---
layout: post
title: "Ka0s: Ollama dividido (Gen vs Embed)"
subtitle: "Aislar el tráfico masivo de embeddings del tráfico interactivo"
cover-img: /assets/img/AI2.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/AI2.png
tags: [post, ka0s, ollama, ai, kubernetes, performance]
author: Ka0s
---

El error más común cuando montas un sistema RAG en producción es asumir que “un solo endpoint de modelos” lo resuelve todo.

En cuanto metes ingesta real (bases de datos, miles/millones de chunks), **embeddings se comen la cola** y la generación se degrada.

## Separar para proteger la experiencia

En Ka0s lo resolvemos con dos servicios:

- `ollama-gen`: generación (GPU, online)
- `ollama-embed`: embeddings (CPU, offline)

Rationale documentado: `core/docs/ka0s_agent_knowledge_pipeline/01_concept.md`.

## Qué cambia en la práctica

Online (Query):

- el agente usa `ollama-gen` para `/api/generate`.

Offline (Ingesta):

- los jobs de ingesta llaman a `ollama-embed` para `/api/embeddings`.

## Resultado

- Latencia estable para el usuario.
- Throughput alto para ingesta.
- Menos riesgo de “todo va lento” cuando el batch corre de madrugada.

Mañana: cómo hacemos incrementalidad sin depender de “magia”: estado persistente, watermarks y control de volumen.

