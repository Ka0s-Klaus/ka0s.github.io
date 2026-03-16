---
layout: post
title: "Ka0s: Kubernetes Audits"
subtitle: "Auditoría exhaustiva, inspección de servicios y recolección de logs"
cover-img: /assets/img/kaos-summary.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-summary.png
tags: [post, ka0s, kubernetes, audit, observability, automation]
author: Ka0s
---

El módulo `core/docs/k8s-audits/00_main.md` agrupa workflows para auditar el clúster con periodicidad y evidencia.

## Tres flujos principales

- Full Infrastructure Audit (semanal).
- Service Audit (manual, por servicio).
- Log Collection (horaria, para trazabilidad).

El objetivo no es “mirar por mirar”: es construir un historial auditable del estado del cluster.

