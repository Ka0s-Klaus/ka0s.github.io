---
layout: post
title: "Ka0s: Audit Failed Pods"
subtitle: "Detectar pods anómalos y registrar evidencia con trazabilidad"
cover-img: /assets/img/kaos-summary.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-summary.png
tags: [post, ka0s, kubernetes, audit, troubleshooting, itop]
author: Ka0s
---

Los pods fallan. Lo importante es no perder la evidencia.

El módulo `core/docs/ka0s_audit_pods/00_main.md` automatiza:

- detección de pods en estados anómalos,
- generación de resultados (JSON),
- y trazabilidad (opcional integración con iTop).

El valor real es operativo: no te enteras “por sorpresa”, y queda registro en `audit/`.

