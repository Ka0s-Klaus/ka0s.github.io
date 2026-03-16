---
layout: post
title: "Ka0s: Delete Namespace (seguro)"
subtitle: "Borrar con evidencia: inventario, purgado y finalizers"
cover-img: /assets/img/kaos-yamllint.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-yamllint.png
tags: [post, ka0s, kubernetes, cleanup, automation, safety]
author: Ka0s
---

Borrar un namespace en Kubernetes puede ser trivial… o puede quedarse eternamente en `Terminating`.

Ka0s lo trata como una operación **peligrosa** que debe ser:

- confirmada,
- auditada,
- y forzada solo cuando hay bloqueo real.

El módulo `core/docs/ka0s_delete_ns/01_concept.md` define el flujo:

- workflow con confirmación explícita ("DELETE"),
- conexión segura al cluster,
- script robusto (`force-delete-namespace.sh`) que:
  - inventaría recursos,
  - elimina recursivamente,
  - y parchea finalizers atascados vía API raw.

Además, deja evidencia en `audit/trash/` y dispara una auditoría del cluster al final.

