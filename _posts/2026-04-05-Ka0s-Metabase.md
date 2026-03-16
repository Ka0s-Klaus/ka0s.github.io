---
layout: post
title: "Ka0s: Metabase"
subtitle: "BI operativo: datos accesibles, dashboards y contexto de negocio"
cover-img: /assets/img/graficos.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/graficos.png
tags: [post, ka0s, metabase, analytics, postgresql, observability]
author: Ka0s
---

Una plataforma madura no solo automatiza: **mide**.

Metabase es la capa de BI del ecosistema Ka0s (`core/docs/ka0s_metabase/01_concept.md`):

- consultas y dashboards,
- exploración por equipos no técnicos,
- y un acceso sencillo a los datos.

## Despliegue pensado para operación

La doc define:

- deployment en `metabase` namespace,
- DB de backend en PostgreSQL centralizado,
- acceso por Ingress con TLS.

## Qué cambia para el día a día

- las decisiones se apoyan en datos,
- el crecimiento del sistema se visualiza,
- y la operación puede detectar tendencias antes de que exploten.

