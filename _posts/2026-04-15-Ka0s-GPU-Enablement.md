---
layout: post
title: "Ka0s: GPU Enablement (Intel)"
subtitle: "Habilitar iGPU en Kubernetes para workloads acelerados"
cover-img: /assets/img/kaos-core.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-core.png
tags: [post, ka0s, kubernetes, gpu, intel, openvino]
author: Ka0s
---

En Ka0s, el nodo manager no solo coordina: también puede acelerar.

El módulo `core/docs/ka0s_gpu_enablement/01_concept.md` describe cómo habilitamos la iGPU Intel (HD 520) para que Kubernetes pueda asignarla a Pods.

## Casos de uso

- transcodificación (FFmpeg, Jellyfin),
- inferencia ligera (OpenVINO),
- render acelerado.

## La pieza técnica

Se usa el **Intel GPU Device Plugin**:

- detecta GPUs,
- expone el recurso `gpu.intel.com/i915`,
- y permite compartir la GPU mediante time-slicing.

Esto abre la puerta a workloads de IA y multimedia sin exigir una GPU dedicada.

