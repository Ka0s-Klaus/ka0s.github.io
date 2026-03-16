---
layout: post
title: "Ka0s: Checklist de Seguridad Kubernetes"
subtitle: "De recomendaciones sueltas a tareas automatizables"
cover-img: /assets/img/kaos-secrets.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-secrets.png
tags: [post, ka0s, security, kubernetes, rbac, devsecops]
author: Ka0s
---

La seguridad no es un documento: es una lista de tareas que se ejecutan.

En `core/docs/ka0s_security/01_security_checklist.md` hay una idea potente: convertir controles de Kubernetes en verificaciones automatizables.

## Qué se audita

- Pod Security: privilegiados, root, hostPath, capabilities.
- RBAC: roles con `*`, serviceaccounts con cluster-admin, tokens automontados.
- Control plane: anonymous auth, cifrado de secretos, audit logging.
- Red: namespaces sin NetworkPolicy.
- Imágenes: tags `latest`, registros no confiables.

## Endurecimiento de GitHub Actions

La checklist incluye controles claros:

- permisos mínimos (`contents: read` por defecto),
- pinning de acciones,
- evitar inyección de comandos,
- runners controlados.

El objetivo es simple: que el sistema sea seguro por defecto, y que desviarse sea explícito y revisable.

