---
layout: post
title: "Ka0s: CI/CD para Kubernetes"
subtitle: "GitOps simplificado con auditoría continua"
cover-img: /assets/img/workflow-ka0s.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/workflow-ka0s.png
tags: [post, ka0s, kubernetes, ci-cd, gitops, security]
author: Ka0s
---

En Ka0s, el CI/CD para Kubernetes no se plantea como “otro operador más”, sino como un flujo **simple**, **auditado** y **controlable**.

La idea está descrita en `core/docs/ka0s_ci_cd_k8s/01_concept.md`: **GitOps simplificado** + **auditoría continua**.

## Dos fases, dos objetivos

### 1) CI (validación) en ramas de desarrollo

- Trigger: cambios en `core/b2b/core-services/**` fuera de `main`.
- Objetivo: bloquear vulnerabilidades críticas antes del merge.
- Herramienta: Trivy.
- Evidencia: informe en `audit/kube/validation-report-<branch>-<id>.md`.

### 2) CD (despliegue) en `main`

- Trigger: push/merge a `main`.
- Objetivo: aplicar cambios reales al cluster.
- Motor: `kubectl` + `kustomize`.
- Inteligencia: detectar qué servicios cambiaron y aplicar solo lo necesario.
- Evidencia: `audit/deploy/deployment-report-<service>-<id>.md`.

## Verificación avanzada (evitar falsos OK)

Kubernetes puede marcar un rollout como “OK”, y aun así dejar un servicio inservible.

Por eso el flujo incluye verificaciones post-despliegue:

- Pods en estado esperado.
- Endpoints activos.
- Validación opcional de IP externa si aplica.

En resumen: no es CI/CD “por fe”, es CI/CD con pruebas operativas y trazabilidad.

