---
layout: post
title: "Ka0s: MySQL centralizado"
subtitle: "Consolidación, backups y operación simple"
cover-img: /assets/img/centralizacion.jpeg
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/centralizacion.jpeg
tags: [post, ka0s, mysql, data, operations]
author: Ka0s
---

Cuando cada aplicación trae su propia base de datos, el resultado es fragmentación: más backups, más credenciales, más puntos de fallo.

Ka0s propone un servicio MySQL centralizado (ver `core/docs/ka0s_db_admin/05_mysql_central.md`) para consolidar bases de datos de aplicaciones como iTop.

## Especificaciones de operación

- MySQL 8.0.
- Namespace: `mysql`.
- DNS interno: `mysql.mysql.svc.cluster.local:3306`.
- Persistencia en NFS (`storage-system`).

## Diseño realista (hardware realista)

El documento recuerda una realidad importante: los recursos no son infinitos.

Por eso se configura de forma conservadora:

- buffer pool 256MB,
- límites Kubernetes 1Gi RAM / 1 CPU,
- y un máximo de conexiones razonable.

## Buenas prácticas

- crear un usuario y una base de datos por aplicación,
- evitar que las apps conecten como `root`.

