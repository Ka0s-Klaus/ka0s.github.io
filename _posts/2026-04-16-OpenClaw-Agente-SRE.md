---
layout: post
title: "OpenClaw: Agente SRE dedicado"
subtitle: "Un asistente con permisos reales sobre el cluster"
cover-img: /assets/img/AI2.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/AI2.png
tags: [post, ka0s, sre, agent, kubernetes, automation]
author: Ka0s
---

OpenClaw (ver `core/docs/openclaw/01_concept.md`) es un agente de IA pensado para ejecutar tareas SRE con lenguaje natural.

## Cómo se despliega

- StatefulSet para persistir memoria.
- Namespace `openclaw`.
- RBAC con permisos elevados (en base a diagnóstico).
- Skills inyectadas vía ConfigMap.

## Por qué encaja con Ka0s

Ka0s no busca un chatbot simpático.

Busca un operador automatizado con protocolos:

- diagnósticos repetibles,
- herramientas reales (`kubectl`, `helm`),
- y capacidad de entrenarse con `core/docs/`.
