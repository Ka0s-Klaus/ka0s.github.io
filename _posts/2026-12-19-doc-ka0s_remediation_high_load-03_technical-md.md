---
layout: post
title: "Estrategia de Mitigación de Carga Alta (High Load) en Control Plane"
subtitle: "Documento: core/docs/ka0s_remediation_high_load/03_technical.md"
cover-img: /assets/img/open_code.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/open_code.png
tags: [post, ka0s, docs, source, ka0s_remediation_high_load]
author: Ka0s
---

El nodo `k8-manager` está sufriendo incidentes recurrentes de "High Load" (Load Average > Cores).
- **Diagnóstico**: Workloads de aplicación (ej: Metabase, Java Apps) están siendo programados en el nodo Control Plane, compitiendo por recursos con `kube-apiserver` y `etcd`.
- **Causa Raíz**: Falta de aislamiento del Control Plane (Taints) o falta de reglas de afinidad en los Deployments.

---

Fuente: `core/docs/ka0s_remediation_high_load/03_technical.md`

