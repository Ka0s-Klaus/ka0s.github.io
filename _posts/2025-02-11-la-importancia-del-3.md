---
layout: post
title: La importanciancia del "3"
subtitle: Tarea - Acción - Resultado
cover-img: /assets/img/path.jpg
thumbnail-img: /assets/img/kaos-vars.png
share-img: /assets/img/path.jpg
tags: [post, release candidate Klaus]
author: bbt2+
---
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/w/ka0s-klaus/ka0s/main) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/ka0s-klaus/ka0s)

Albert Einstein dijo una vez: "... si tu intención es describir la verdad, hazlo con sencillez y la elegancia déjasela al sastre."

¿de que se compone la sencillez?

Antes de entrar de lleno a analizar en profundidad el término sencillez y su significado, tenemos que dejar patente que aquel procede del latín. Concretamente su origen etimológico se encuentra en el vocablo latino singulus, que puede traducirse como *“uno por uno”*, y en la suma además del sufijo –ez, que es equivalente a “cualidad”.

Para lo cual, dicho esto .... Sencillez es la cualidad de sencillo *(que no tiene composición, carece de ostentación o no ofrece dificultad)*. Este adjetivo puede aplicarse a las personas o a los objetos.

Y que más sencillo que todos los procesos, servicios, acciones y demas ejecuciones dentro de la plataforma de Ka0s estan diseño en su proceso más básico: tarea-acción-resultado. PAra este propósito tenemos terminos como:

- **Atomicos**: con este término nos referimos a todos aquelllos automatismo que únicamente ejecutan una acción y que permiten ser orquestados.

- **Efímeros/as**: con este término nos referimos esas pequeñas acciones de corta, muy corta duración.

- **Iniciador**: con este término nos referimos siempre al módulo de ka0s.yml responsable de accionar el resto de mecanismos dentro de él.

- **Inspector**(audit): con este términos nos referimos a uno de los módulos que se encarga de extraer el resumen de todas y cada una de las ejecuciones que se realizan dentro de Ka0s.

- **Número Aureo (3)**: y sí, con esté término en concreto somos muy tenaces. La base de Ka0s es que en menos de tres tienes que ser capaz de obtener un resultado.

- **Laya**: con este término nos referimos a una situación dentro de Ka0s que determina que, sí él propio sistema conoce el origen del dato, dispone de todas aquellas acciones automatizadas que trabajan con el dato y dispone de un control de registro de todas las ejecuciones, hayan sido estas correctas o fallidas, Laya (asap nuestro módulo de IA) debería de poder ser capaz de contestar a cualquiera de tus preguntas sobre el propio sistema.

- **Reusar**: este es el término que nos gustar aplicar a cada diseño de los módulos core de Ka0s. Todos estan diseñados para poder ser "reusados" para generar nuevos módulos.

- **Reutilizar**: Ka0s esta diseñado, para que la estructura core y es resto de desarrollos sean dos procesos que si cambian en el tiempo permitan siempre reutilizar el código ya funcional.

- **Simple y Sencillo**: pues si, dos conceptos en uno que engloban la filosofía que permite que dentro de Ka0s (a fecha de hoy) se puedan utilizar más de [XX](https://keepcoding.io/blog/cuantos-lenguajes-de-programacion-existen/) lenguajes de programación diferentes, permitiendo a la herramienta un *flexibilidad* completa.

- **Agnóstico**: pues sí, Ka0s es muy suyo y le es indistinto para quien trabaje o a donde debe conectarse. Est diseádo a traves de variables y secretos los cuales le permiten una modularidad y una reunsabilidad muy alta (+ del 75% del código core de Ka0s en totalmente reusable), lo cual nos permite facilitar una agilidad a los equipos de desarollo que les permite reducir las líneas de código reiterativo y disminuir su tiemnpo de operación hasta en un 65%.
