---
layout: post
title: "Ka0s: Windows Nodes"
subtitle: "Unir nodos Windows al cluster con un script template"
cover-img: /assets/img/kaos-core.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-core.png
tags: [post, ka0s, kubernetes, windows, nodes, powershell]
author: Ka0s
---

Ka0s incluye guías para incorporar Windows Server como nodo del cluster.

En `core/docs/windows_nodes/03_technical.md` hay un script PowerShell template que automatiza:

- prerrequisitos (Containers/Hyper-V),
- descarga de binarios (`kubelet`, `kube-proxy`, `kubectl`),
- estructura de directorios,
- y arranque inicial (pendiente de CNI).

Es un punto de partida controlado para escenarios híbridos.
