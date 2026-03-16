---
layout: post
title: "4. Troubleshooting: CloudBeaver"
subtitle: "Documento: core/docs/ka0s_db_admin/04_troubleshooting.md"
cover-img: /assets/img/open_code.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/open_code.png
tags: [post, ka0s, docs, source, ka0s_db_admin]
author: Ka0s
---

*   El pod `cloudbeaver-0` o similar se queda en estado `Pending` o `ContainerCreating`.
*   En `kubectl describe pod`, se observan eventos relacionados con **"MountVolume.SetUp failed"** o **"Stale NFS file handle"**.
*   El pod no puede montar el volumen persistente (PVC).

---

Fuente: `core/docs/ka0s_db_admin/04_troubleshooting.md`

