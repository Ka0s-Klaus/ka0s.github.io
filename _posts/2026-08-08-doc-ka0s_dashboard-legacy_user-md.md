---
layout: post
title: "docs/ka0s_dashboard/legacy_user.md"
subtitle: "Documento: core/docs/ka0s_dashboard/legacy_user.md"
cover-img: /assets/img/open_code.png
thumbnail-img: /assets/img/kaos-daavid-2.png
share-img: /assets/img/open_code.png
tags: [post, ka0s, docs, source, ka0s_dashboard]
author: Ka0s
---

![Ka0S](../imgs/Portada_Documentacion_Ka0s_Dashboard.png)
El dashboard web está diseñado para mostrar información de manera dinámica a partir de los archivos JSON ubicados en core\web\data. Esto lo hace sumamente flexible y adaptable a cualquier tipo de contenido o de web, ya que para crear la web solo se necesita agregar archivos JSON sin necesidad de modificar nada de Backend, simplemente escribir los datos de una determinada forma que se explicará posteriormente y obtener los resultados en pantalla.
De esta manera cualquier persona, sin necesidad de que tenga conocimientos de programación, puede crear una web simplemente incluyendo los ficheros de datos que quiera mostrar y haciendo referencia en los JSON en los que inserte la estructura de la web que desee.
En cuanto a los ficheros que hay que modificar o agregar para crear esta web se encuentran los siguientes:
- El archivo principal de configuración: webs.json, en el cual se tienen que definir qué archivos se usan para cada sección. Un ejemplo de configuración de este fichero podría ser el siguiente:

---

Fuente: `core/docs/ka0s_dashboard/legacy_user.md`

