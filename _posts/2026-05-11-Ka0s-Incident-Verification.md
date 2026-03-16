---
layout: post
title: "Ka0s: Protocolo de Verificación de Incidencias"
subtitle: "Nunca asumas: valida primero la realidad del cluster"
cover-img: /assets/img/kaos-summary.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-summary.png
tags: [post, ka0s, incident-response, sop, kubernetes, operations]
author: Ka0s
---

Un pipeline en rojo no siempre significa servicio caído.

El SOP en `core/docs/ka0s_incident_response/01_issue_verification.md` define el procedimiento:

- analizar contexto (Issue, run ID, commit),
- verificar estado real del servicio en Kubernetes,
- hacer prueba de humo,
- y solo entonces decidir si cerrar o remediar.

Regla de oro:

> “Nunca asumas que un pipeline rojo significa servicio caído. Verifica siempre la realidad del clúster.”

