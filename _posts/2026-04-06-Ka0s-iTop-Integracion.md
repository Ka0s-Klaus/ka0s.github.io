---
layout: post
title: "Ka0s: Integración iTop"
subtitle: "ITSM que dispara automatización: del ticket al workflow"
cover-img: /assets/img/kaos-heidi.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-heidi.png
tags: [post, ka0s, itop, itsm, automation, github-actions]
author: Ka0s
---

ITSM no es un lugar donde archivar tickets.

Es un lugar donde se decide qué debe ocurrir.

La integración iTop de Ka0s (`core/docs/ka0s_itop/01_concept.md`) conecta eventos de servicio con automatización:

1. Un ticket cambia de estado o se crea una solicitud.
2. iTop dispara un webhook/API.
3. GitHub Actions ejecuta workflows de Ka0s.
4. El resultado vuelve al ticket.

## Por qué es potente

- El proceso vive donde el negocio ya trabaja (ITSM).
- La ejecución vive en workflows reproducibles.
- El feedback queda trazado (en el ticket y en el repo).

Cuando esto se hace bien, el ticket deja de ser un “chat” y se convierte en un **contrato de ejecución**.

