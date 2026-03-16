---
layout: post
title: "Ka0s: Reporte diario de Lead Time"
subtitle: "Medir el flujo: del Inspector a MongoDB y a Metabase"
cover-img: /assets/img/ka0s-leadtime.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/ka0s-leadtime.png
tags: [post, ka0s, metrics, lead-time, metabase, mongo]
author: Ka0s
---

En Ka0s, el lead time se mide para entender el flujo real del trabajo.

`core/docs/ka0s_reports/00_main.md` describe el sistema:

- ingesta desde `audit/inspector` hacia MongoDB,
- cálculo de `lead_time_minutes`,
- generación diaria de reporte en `audit/lead_time/`,
- visualización en Metabase (mapa de calor).

Métrica útil cuando sirve para tomar decisiones, no para decorar.
