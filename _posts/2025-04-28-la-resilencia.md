---
layout: post
title: "La resilencia"
subtitle: El origen de la red neuronal de Ka0s
cover-img: /assets/img/AI2.png
thumbnail-img: /assets/img/ka0s-runner-controller.png
share-img: /assets/img/AI2.png
tags: [post, metodología, networking, neuronal]
author: Ka0s
---
## Ka0s *resilencia y ...*

Nuestra metodología de desarrallo, que no quiere decir que tenga que ser la tuya por obligación 'se explicara mas en detalle', nos permitió desarrollar una red neuronal que se adapta a cualquier entorno de ejecución. Y sí, has oido bien, "cualquier entorno de ejecución" y "red neuronal".

El primer escollo fue solventar el tema de la "resilencia", y más basándola en una red neuronal, que no es otra cosa que la capacidad de la red de adaptarse a cualquier entorno de ejecución. Y para ello, se diseñó un módulo que se encarga de "entrenar" a la red neuronal para que se adapte a cualquier entorno de ejecución.

Co...¡ ¿Entrenar? Sí, entrenar. Ka0s dispone de una metodología de "deploy" de sus *ejecutores* diseñada en tres capas, lo cual nos permite:

- Realizar la implementación del computo necesario para Ka0s, usando cada uno de los diferentes "dispositivos" añadidos al *c0re*.
- Realizar la implementación de cada uno de los componentes de Ka0s, usando cada uno de los diferentes "dispositivos" añadidos al *c0re*.
- Realizar el "gobierno" de la propia plataforma, es decir, de cada uno de los diferentes "dispositivos" añadidos al *c0re*.

Algo así como ...
![Ka0s Runner Controller](/assets/img/ka0s-runner-controller.png)

Si que es cierto, que hacemos hincapíe en que la red neuronal se adapta a cualquier entorno de ejecución, y esto es lo que nos permite que Ka0s sea una plataforma de ejecución de cualquier tipo de aplicación, y no solo de aplicaciones basadas en la tecnología de "contenedores".

Además, dentro del desarrollo de Ka0s, actualmente se esta trabajando en añadir un módulo asociado a la IA, que nos permita desplegar en los diferentes recursos de la red neuronal, pequeños agentes dedicados a la monitorización de los recursos, y que nos permitan realizar una gestión de los mismos, y de los recursos que se estén ejecutando en ellos.

[Aquí dispones de toda la información](https://github.com/Ka0s-Klaus/ka0s/blob/main/core/docs/ka0s/ka0s_metodologia.md)
