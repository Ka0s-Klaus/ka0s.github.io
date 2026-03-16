---
layout: post
title: "Ka0s: Actualización del cluster (OS)"
subtitle: "Automatizar mantenimiento con un patrón bastion"
cover-img: /assets/img/ka0s-landingzone.jpg
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/ka0s-landingzone.jpg
tags: [post, ka0s, kubernetes, automation, ssh, operations]
author: Ka0s
---

Actualizar nodos a mano funciona… hasta que tienes que hacerlo de verdad, con consistencia y sin romper producción.

El módulo `core/docs/ka0s_cluster_update/01_concept.md` describe un enfoque práctico: patrón **bastion host**.

## El patrón

- El runner conecta por SSH solo al manager (`k8-manager`).
- Desde el manager se salta a los workers con SSH interno.
- Resultado: menos superficie de ataque (un punto de entrada controlado).

## Flujo

`Runner` → `SSH` → `Manager` → `SSH interno` → `Workers`

## Por qué encaja con Ka0s

- Identidad y trazabilidad (`KAOS_MODULE`).
- Gestión de errores estandarizada.
- Auditoría al finalizar.
- Seguridad por permisos mínimos.

Esto no es “hacer updates”: es convertir mantenimiento en un proceso repetible.

