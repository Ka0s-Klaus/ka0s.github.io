---
layout: post
title: "Ka0s: Self Service Portal"
subtitle: "Catálogo dinámico, RBAC y autoservicio seguro"
cover-img: /assets/img/ka0s-ecosistema.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/ka0s-ecosistema.png
tags: [post, ka0s, portal, rbac, automation, product]
author: Ka0s
---

El autoservicio no es una moda: es la única forma de escalar operaciones.

El **Self Service Portal** (`core/docs/ka0s_self_service_portal/01_concept.md`) plantea una interfaz unificada para que usuarios y operadores ejecuten tareas predefinidas sin intervención manual.

## Principios

- Catálogo dinámico: servicios visibles según config/permisos.
- Seguridad: RBAC estricto (ves y ejecutas solo lo permitido).
- API first: frontend desacoplado.
- Stateless: sesiones con JWT.
- Extensible: añadir acciones como añadir entradas, no redeploys.

## Qué habilita

- crear namespaces,
- reiniciar pods,
- solicitar accesos,
- consultar estado.

Con trazabilidad, el portal no sustituye procesos: los vuelve consumibles.
