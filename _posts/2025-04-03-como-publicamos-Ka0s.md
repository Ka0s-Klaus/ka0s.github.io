---
layout: post
title: Publicando el Código de Ka0s
subtitle: La transparencia como eje fundamental del proceso
cover-img: /assets/img/atajo.png
thumbnail-img: /assets/img/open_code.png
share-img: /assets/img/path.jpg
tags: [dashboard, architecture]
author: Alejandro Peso Buendía
---

Nuestro proceso de publicación

En Ka0s hemos invertido el flujo tradicional de desarrollo. En lugar de seguir el camino habitual (desarrollo → pruebas → producción), nosotros comenzamos por el final:

1. **Publicación inmediata**: Cada módulo se publica en nuestro repositorio público desde el primer commit.
2. **Desarrollo continuo**: El código evoluciona a la vista de todos, con cada cambio reflejado en tiempo real.
3. **Pruebas en público**: Nuestras pruebas son transparentes y visibles para cualquiera que quiera seguir el proceso.

## ¿Por qué publicamos primero?

Esta filosofía de "publicar primero" tiene varias ventajas:

- Fomenta la **transparencia total** en nuestro proceso de desarrollo
- Permite la **colaboración temprana** con la comunidad
- Nos obliga a mantener un **alto estándar de calidad** desde el primer momento
- Reduce la **curva de aprendizaje** para nuevos colaboradores

## Cómo lo hacemos técnicamente

Nuestro proceso de publicación se basa en GitHub Actions y está completamente automatizado:

1. Cada commit en main dispara un workflow de GitHub Actions
2. El código se compila y se ejecutan pruebas básicas
3. Si pasa las pruebas, se despliega automáticamente en nuestro servidor público
4. El dashboard se actualiza con la información del nuevo módulo o actualización


[Ka0s DashBoard v0.0.0](https://www.ka0s.io/dashboard/Index.html)
