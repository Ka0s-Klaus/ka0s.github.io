---
layout: post
title: "Ka0s: Version Manager"
subtitle: "SemVer sin fricción: de la rama a la versión"
cover-img: /assets/img/kaos-version.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/kaos-version.png
tags: [post, ka0s, semver, release, automation, ci-cd]
author: Ka0s
---

Versionar a mano funciona hasta que no funciona.

En Ka0s, el versionado semántico se automatiza con **Ka0s Version Manager** (`core/docs/ka0s_version/01_concept.md`).

## La regla de negocio

- `fix/` → PATCH (+0.0.1)
- `feat/` → MINOR (+0.1.0)
- `release/` → MAJOR (+1.0.0)

Esto convierte el versionado en un proceso repetible y reduce errores humanos en tags y releases.

