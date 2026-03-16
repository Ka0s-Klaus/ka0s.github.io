---
layout: post
title: "Ka0s: Ingesta incremental (sin dolor)"
subtitle: "Estado persistente, watermarks y modo auto"
cover-img: /assets/img/kaos-version.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-version.png
tags: [post, ka0s, data, incremental, kubernetes, automation]
author: Ka0s
---

Ingerir “todo” está bien… **una vez**. Hacerlo cada día es quemar CPU, IO y paciencia.

## El objetivo

Después del primer bootstrap, cada ejecución debería procesar:

- solo registros nuevos,
- o registros modificados,
- sin re-embedir lo mismo.

## Cómo lo hacemos

### 1) Estado persistente en el spool

Guardamos estado por fuente en el PVC del spool:

- Mongo: último `_id` visto por colección.
- PostgreSQL/MySQL: watermark `updated_at` (configurable) por tabla.

### 2) `MODE=auto`

Cuando quieres “todo” y no quieres pelearte con el arranque:

- Primera ejecución: `full`.
- Siguientes: `incremental` automáticamente.

### 3) Tablas sin watermark

Si una tabla no tiene `updated_at` (o el campo definido), se procesa una vez y se marca para no re-fullscan en modo incremental.

### 4) Guardarraíles (cuando el bootstrap es enorme)

Puedes limitar temporalmente:

- Mongo: `MAX_DOCS_PER_RUN`, `MAX_CHUNKS_PER_RUN`
- SQL: `MAX_ROWS_PER_TABLE`, `MAX_ROWS_PER_RUN`, `MAX_CHUNKS_PER_RUN`

## Por qué es importante

Incrementalidad no es “optimización”: es supervivencia operativa.

Mañana: seguridad. Cómo evitamos que la memoria vectorial se convierta en un vertedero de secretos.

