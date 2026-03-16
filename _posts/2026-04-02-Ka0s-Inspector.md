---
layout: post
title: "Ka0s: Inspector"
subtitle: "Trazabilidad real de GitHub Actions: logs, informes y evidencia"
cover-img: /assets/img/kaos-inspector.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-inspector.png
tags: [post, ka0s, inspector, audit, github-actions, observability]
author: Ka0s
---

En Ka0s no basta con que un workflow “pase” o “falle”.

Lo que necesitamos es:

- saber **qué ocurrió**,
- poder **revisarlo después**,
- y convertirlo en evidencia operativa.

Ahí entra **Ka0s Inspector**: el módulo que transforma ejecuciones de GitHub Actions en trazabilidad.

## ¿Qué hace realmente?

Según `core/docs/ka0s_inspector/01_concept.md`, Inspector:

1. Recupera logs crudos de ejecuciones.
2. Genera un JSON procesable.
3. Notifica con contexto (Issue técnica si falla, actualización si OK).
4. Persiste resultados en `audit/inspector/` dentro del repo.

El punto clave es el 4: **historial inmutable**.

## Por qué importa

Sin un “ojo que todo lo ve”, la automatización se convierte en:

- mensajes sueltos,
- capturas de pantalla,
- y decisiones sin evidencia.

Inspector convierte CI/CD en algo auditable y “operable”.

