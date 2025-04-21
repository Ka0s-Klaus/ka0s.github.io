---
layout: post
title: "La metodología"
subtitle: El origen de nuestra metodología
cover-img: /assets/img/AI1.png
thumbnail-img: /assets/img/kaos-init.png
share-img: /assets/img/AI1.png
tags: [post, metodología]
author: Ka0s
---
## Ka0s *metodología y estructura*

Nuestra metodología de desarrallo, que no quiere decir que tenga que ser la tuya por obligación 'se explicara mas en detalle', por ende nuestra manera de trabajar se basa en que Ka0s única y exclusivamente se diseño para trabajar en "origin/main".

Explicado de manera sencilla sería algo así como " ... Ka0s dispone de una unica rama y un único "iniciador" que a través del cual podemos discriminar los entornos de ejecución de las diferentes solicitudes.

¿cómo difencia Ka0s los entornos? Pues tiene un "compliance" específico definido en un fichero json que le indica para cada cambio en el número de versión cual es el entorno de ejecución. (nota: tenga en cuenta que el core de Ka0s, donde se desarrolla la solución, cuenta con varios módulos que gestiona los diferentes entornos y runners donde se ejecuta el código)

¿Ka0s v1.0.38 rc unnamed? La característica del versionado de Ka0s es la siguiente: la version de compone de un MAYOR "." un MINOR "." y un PATCH que en la equivalencia de nuestro equipo de desarrollo es algo así como:

- Un PATCH (H) hace referencia a una correccción y/o modificación de alguno de los módulos de Ka0s. Por defecto, PATCH es la "rama" donde se desarrolla.
- Un MINOR (F) hace referencia a una nueva "funcionalidad" dentro del propio core de Ka0s, ya sea con un ampliación de funcionalidades de algo existente como una mejora completa o diseño un nuevo módulo. Por defecto, MINIOR es la rama donde se depurar y prueban esos desarrollos de PATCH.
- Un MAYOR (RN) hace referencia a que se añaden funcionalidades no existentes en "releases" anteriores. Por defecto, MAYOR es la "rama" previa a poner en main una nueva funcionalidad desarrollada en PATCH y probada y depurada en MINOR.

¿Y 'rc unnamed'? Esta es la manera en la que hacemos que las diferentes versiones de Ka0s vean la luz. Cuando una versión queda completada (una v1.0.38) dentro de Ka0s hay un mecanismo automatizado para que se genere una nueva release cuyo nombre se elije aleatoriamente por el equipo de desarrollo.

¿Que tienen de diferente una release con otra? Pues somos "Ka0s" asique la respuesta sería algo así como; el todo y el nada. Nosotros ponemos nombre a las release y las identificamos porque en su contenido se desarrolla alguna faceta especifica que se haya solicitado. Por ejemplo, en estos momentos el qeuipo del core esta trabajando en el desarrollo de Ka0s "Release Klaus" donde su función principal es añadir la funcionalidad de poder gestionar y visualizar la información referente a FinOps + Monitorización + Observabilidad de cualquier recurso de una compañía independietemente de donde este alojado.......

*"Próxima Release"* Anticipamos que en estos momentos se esta "cocinando" la Release Proyecto D cuya funcionalidad se basa en añadir el control de un SOC a Ka0s.

Llegados a este punto nos dimos cuenta que con los mínimos recursos y variaciones disponiamos de más opciones de adaptabilidad de Ka0s a cualquiera ecosistema tecnológico y nos surgio la duda de añadir un frontal a través del cual puediesemos estar informados en todo momento de lo que ocurre dentro de Ka0s. Para lo cual decidimos diseñar un módulo que nos permitiese gestionar tanto las solicitudes de ejecución, como registrar cualquier cambio dentro de la plataforma de manera que nos permitiese usar el dashboard más sencillo que se pueda diseñar.
[Aquí dispone de toda la información](https://github.com/Ka0s-Klaus/ka0s/blob/main/core/docs/ka0s/ka0s_metodologia.md)
