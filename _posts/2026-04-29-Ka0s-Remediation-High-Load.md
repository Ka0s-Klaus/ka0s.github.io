---
layout: post
title: "Ka0s: Remediation (High Load)"
subtitle: "Diagnosticar y documentar saturación con evidencia en la Issue"
cover-img: /assets/img/kaos-execution.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-execution.png
tags: [post, ka0s, remediation, incident, github-actions, sre]
author: Ka0s
---

Cuando un nodo está saturado, improvisar es perder tiempo.

El workflow `remediation-high-load.yml` (`core/docs/ka0s_remediation_high_load/01_concept.md`) ejecuta una respuesta táctica:

- conecta por SSH,
- ejecuta `check-high-load.sh`,
- genera un log con nomenclatura estable,
- lo descarga y lo comitea en `audit/incidents/`,
- y comenta un resumen en la Issue.

La clave no es solo “diagnosticar”: es dejar evidencia persistente y vinculada al ticket.

