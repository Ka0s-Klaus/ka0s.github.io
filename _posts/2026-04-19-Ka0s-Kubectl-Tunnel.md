---
layout: post
title: "Ka0s: Kubectl Tunnel"
subtitle: "Kubernetes privado, CI/CD público: el puente seguro"
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-secrets.png
cover-img: /assets/img/kaos-secrets.png
tags: [post, ka0s, kubernetes, github-actions, ssh, security]
author: Ka0s
---

En entornos serios, la API de Kubernetes no está expuesta a internet.

Pero los runners de CI/CD necesitan ejecutar `kubectl`.

El módulo `ka0s_kubectl_tunnel` (`core/docs/ka0s_kubectl_tunnel/01_concept.md`) resuelve esto con un patrón claro: **túnel SSH con port forwarding**.

## Qué hace la acción

1. Crea un túnel SSH al bastión/manager.
2. Mapea `localhost:6443` al API server remoto.
3. Genera un kubeconfig temporal apuntando a `127.0.0.1`.
4. Instala `kubectl` oficial automáticamente.

Resultado: `kubectl` cree que el cluster es local, pero en realidad viaja cifrado por SSH.
