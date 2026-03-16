---
layout: post
title: "Ka0s: Autoremediación"
subtitle: "De una etiqueta en GitHub a una corrección ejecutada"
cover-img: /assets/img/kaos-issue.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-issue.png
tags: [post, ka0s, remediation, incident-response, github-actions]
author: Ka0s
---

En operaciones, lo más caro no es el fallo: es el tiempo entre detectar y corregir.

La autoremediación de Ka0s (documentada en `core/docs/ka0s_remediation/04_autoremediation.md`) convierte una señal en un flujo reproducible.

## Cómo funciona

1. Se detecta el problema (monitorización o humano).
2. Se crea/actualiza una Issue y se etiqueta con `auto-remediate:<tipo>`.
3. GitHub Actions dispara el workflow de autoremediación.
4. Se enruta al workflow específico (por ejemplo, high-load).
5. Se ejecuta la corrección (SSH, kubectl, etc.).
6. El bot comenta el resultado en la Issue.

## Lo importante no es la magia, es el contrato

- **Entrada**: una etiqueta estandarizada.
- **Ejecución**: un workflow reproducible.
- **Salida**: evidencia y feedback en el mismo ticket.

Así la operación deja de depender de “quién estaba de guardia” y pasa a depender de un proceso controlado.

