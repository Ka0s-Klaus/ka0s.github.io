---
layout: post
title: "Ka0s: Watchdog (salud del cluster)"
subtitle: "Self-healing con patrón Monitor-Actuator"
cover-img: /assets/img/kaos-summary.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-summary.png
tags: [post, ka0s, kubernetes, self-healing, operations, watchdog]
author: Ka0s
---

En Ka0s, no esperamos a que alguien “se dé cuenta” del problema.

El sistema vigila invariantes y actúa.

El Watchdog (`core/docs/ka0s_watchdog_node_health/01_concept.md`) implementa el patrón **Monitor-Actuator**:

- Monitor: comprueba invariantes (por ejemplo, espacio en disco).
- Actuator: ejecuta acciones idempotentes cuando se rompen.

## Por qué DiskPressure es crítico

Si un nodo se queda sin disco:

- el runtime puede fallar,
- los logs dejan de escribirse,
- kubelet puede degradarse.

La reacción recomendada es contener el radio de explosión: `cordon` del nodo y auditoría del cluster.

