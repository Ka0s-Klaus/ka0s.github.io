---
layout: post
title: "Concepto y Arquitectura: CI/CD para Kubernetes"
subtitle: "Documento: core/docs/ka0s_ci_cd_k8s/01_concept.md"
cover-img: /assets/img/open_code.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/open_code.png
tags: [post, ka0s, docs, source, ka0s_ci_cd_k8s]
author: Ka0s
---

El sistema de CI/CD de Ka0s para Kubernetes se basa en el principio de **"GitOps Simplificado"** y **"Auditoría Continua"**.
No utilizamos un operador GitOps complejo (como ArgoCD) en esta fase, sino que aprovechamos GitHub Actions como orquestador central para mantener la simplicidad y el control total sobre el proceso de validación y notificación.

---

Fuente: `core/docs/ka0s_ci_cd_k8s/01_concept.md`

