---
layout: post
title: "Módulo Ka0s Inspector - Integración"
subtitle: "Documento: core/docs/ka0s_inspector/03_technical.md"
cover-img: /assets/img/open_code.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/open_code.png
tags: [post, ka0s, docs, source, ka0s_inspector]
author: Ka0s
---

El Inspector maneja información sensible (logs), por lo que aplica políticas estrictas:
*   **Token Scope**: Usa `KAOS_REPO_TOKEN` con permisos mínimos necesarios.
*   **Sanitización**: Filtra secretos conocidos antes de guardar logs en disco (aunque GitHub Actions ya hace esto, el Inspector añade una capa extra).
*   **Identidad**: Los commits de auditoría se firman con una identidad de bot específica para distinguirlos de cambios humanos.

---

Fuente: `core/docs/ka0s_inspector/03_technical.md`

