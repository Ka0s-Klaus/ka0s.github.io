---
layout: post
title: "Ka0s: MongoDB (workflows de datos)"
subtitle: "Gestionar contenido y mantenimiento sin tocar el despliegue"
cover-img: /assets/img/kaos-json.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-json.png
tags: [post, ka0s, mongodb, data, automation, maintenance]
author: Ka0s
---

En Ka0s distinguimos dos responsabilidades:

- desplegar la base de datos,
- y **operar su contenido**.

El módulo `core/docs/ka0s_mongo/01_concept.md` no despliega MongoDB: automatiza mantenimiento y cambios de datos.

## Capacidades

- Cron jobs para mantenimiento.
- Inserción/actualización controlada vía scripts Python.
- Rollback si algo sale mal.

Esto permite tratar datos operativos como un activo gestionado, no como “algo que alguien tocó en prod”.

