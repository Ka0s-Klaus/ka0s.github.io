---
layout: post
title: "Ka0s: Del Spool a pgvector"
subtitle: "UPSERT, idempotencia y por qué el loader es un servicio en sí"
cover-img: /assets/img/kaos-json.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-json.png
tags: [post, ka0s, pgvector, postgresql, rag, data]
author: Ka0s
---

Una ingesta masiva no falla “a lo grande”: falla en detalles pequeños.

Por eso en Ka0s la ingesta no escribe directo en la Vector DB. Primero pasa por un **spool** y después por un **loader**.

## Spool: un buffer operativo, no un “tmp”

El spool es un volumen persistente sobre NFS (StorageClass `nfs-client`) y sirve para:

- desacoplar etapas (extraer/embedir ≠ cargar),
- permitir reintentos,
- y conservar evidencias (`manifest.json`) para auditoría.

Formato mínimo viable:

- `manifest.json` (run_id, source, métricas)
- `vectors.jsonl` (una línea por chunk)

Referencia: `core/docs/ka0s_agent_knowledge_pipeline/03_technical.md`.

## Loader: el guardián de la idempotencia

Un loader serio hace 3 cosas:

1. **Crea/valida el esquema** (pgvector, tabla, claves).
2. **Hace UPSERT** para que reintentar no duplique.
3. **Marca el run como cargado** para no repetir trabajo.

La idempotencia se basa en una clave única como:

`(source, record_id, chunk_id, embedding_model)`

Si ejecutas dos veces el mismo run, **actualiza**, no duplica.

## Por qué esto importa

- Operación: puedes pausar, retomar, reintentar.
- Coste: no pagas embeddings dos veces por el mismo chunk.
- Calidad: puedes versionar normalización/chunking sin “ensuciar” la memoria.

Mañana: el motivo real por el que dividimos Ollama en dos servicios, y cómo eso protege la experiencia del agente.

