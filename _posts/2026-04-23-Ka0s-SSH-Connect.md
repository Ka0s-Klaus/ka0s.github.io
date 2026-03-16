---
layout: post
title: "Ka0s: SSH Connect"
subtitle: "Una sola forma segura de ejecutar scripts remotos desde GitHub Actions"
cover-img: /assets/img/kaos-secrets.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-secrets.png
tags: [post, ka0s, ssh, github-actions, security, automation]
author: Ka0s
---

En automatización, repetir lógica es crear errores.

Conectar por SSH desde workflows suele implicar siempre lo mismo:

- instalar herramientas,
- gestionar host keys,
- ejecutar comandos,
- recopilar resultados.

**Ka0s SSH Connect** (`core/docs/ka0s_ssh_connect/01_concept.md`) encapsula todo eso como meta-workflow y composite action.

## Qué gana el sistema

- no duplicas scripts de conexión en cada workflow,
- centralizas seguridad y manejo de errores,
- y estandarizas cómo se ejecuta y cómo se recupera evidencia.

El patrón es claro: inyectar scripts locales en el servidor remoto, ejecutarlos y traer logs/artefactos de vuelta al runner.

