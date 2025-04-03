---
layout: post
title: El codigo Dashboard Ka0s
subtitle: Dashboard para visualización de datos de Ka0s.
cover-img: /assets/img/path.jpg
thumbnail-img: /assets/img/codigo_html.png
share-img: /assets/img/path.jpg
tags: [dashboard, architecture]
author: jorgecg
---

# Codigo del Dashboard Ka0s

## Arquitectura General
El dashboard de Ka0s sigue una arquitectura modular basada en JavaScript y HTML con Tailwind CSS para los estilos. La estructura está diseñada para ser extensible y fácil de mantener.

## Componentes Principales

### 1. Archivos HTML
- **Index.html**: Punto de entrada principal que carga los scripts y define la estructura base.
- **templates/**: Contiene plantillas HTML para diferentes secciones:

### 2. Módulos JavaScript
- **dashboard.js**: Inicializa y coordina todos los componentes del dashboard.
- **loaders.js**: Utilidades para cargar datos JSON y plantillas HTML.
- **navigation.js**: Gestiona la navegación entre secciones y el comportamiento del sidebar.
- **sections.js**: Maneja la creación y actualización de secciones de contenido.
- **charts.js**: Configura y renderiza gráficos utilizando Chart.js.
- **workflows.js**: Procesa datos específicos de los workflows de GitHub Actions.

### 3. Datos JSON
- **dashboard/principal.json**: Configuración general del dashboard.
- **dashboard/sections/**: Contiene datos específicos para cada sección:

## Flujo de Datos
1. Los scripts Python procesan datos de los archivos event_data_*.json
2. Los resultados se almacenan en archivos JSON en dashboard/sections/
3. El frontend carga estos datos mediante fetch() y los visualiza
4. Los gráficos se generan dinámicamente con Chart.js

## Características Responsivas
- Diseño adaptable para dispositivos móviles y escritorio
- Sidebar colapsable para optimizar espacio
- Gráficos que se ajustan al tamaño de la pantalla

- Haciendo público cada paso en el que se trabaja.
[Ka0s DashBoard v0.0.0](https://www.ka0s.io/dashboard/Index.html)

