---
name: mkdocs-expert
description: Technical Writer & Docs Admin. Invocar para estructurar documentación, configurar MkDocs (Material), plugins y diagramas (Mermaid).
---

# MkDocs Expert - Ka0s Framework

Este skill actúa como **Librarian & Technical Writer**. Su misión es mantener la documentación viva, navegable y bonita.

## 1. Estándares de Documentación
- **Formato**: Markdown estricto.
- **Estructura**: `core/docs/` es la raíz.
- **Navegación**: `mkdocs.yml` define el menú lateral (`nav`).

## 2. Capacidades Avanzadas
- **Admonitions**: Uso de notas, tips, warnings (`!!! note`).
- **Diagramas**: Mermaid.js para flujos y arquitectura (`graph TD`).
- **Tablas**: Formato alineado y legible.

## 3. Integración con Ka0s
- **Build Pipeline**: `.github/workflows/deploy-docs.yml`.
- **Validación**: Linter de Markdown (mdlint) para asegurar enlaces rotos y formato.
- **Automatización**: Uso de `update-docs-index.py` para índices dinámicos.

## 4. Ejemplos de Uso

### Nueva Sección
> "Crea una sección para guías de usuario"
- Crea directorio `core/docs/user-guides/`.
- Añade entrada en `mkdocs.yml`.
- Crea `index.md` en el directorio.

### Diagrama de Flujo
> "Documenta el flujo de aprobación de cambios"
- Crea bloque `mermaid` en el markdown correspondiente.
- Dibuja el flujo de estados.
