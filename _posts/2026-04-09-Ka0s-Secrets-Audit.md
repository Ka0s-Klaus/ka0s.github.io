---
layout: post
title: "Ka0s: Auditoría de Secretos"
subtitle: "Detectar secretos usados, definidos y huérfanos en workflows"
cover-img: /assets/img/kaos-secrets.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-secrets.png
tags: [post, ka0s, security, secrets, github-actions, compliance]
author: Ka0s
---

Los secretos son una deuda silenciosa.

No duelen hasta que:

- caducan,
- se filtran,
- o se quedan “colgados” (definidos pero ya nadie los usa).

Ka0s incluye una auditoría automática (`core/docs/ka0s/secrets.md`):

- lista secretos definidos en GitHub,
- detecta secretos referenciados en `.github/workflows`,
- y muestra los secretos definidos sin uso detectado.

## Por qué es importante

- Menos superficie de ataque.
- Menos rotaciones “a ciegas”.
- Más coherencia entre repositorio y configuración.

En sistemas que automatizan operación, la seguridad no puede depender de memoria humana.

