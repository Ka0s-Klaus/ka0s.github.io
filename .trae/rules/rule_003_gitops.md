# Regla 003: Inmutabilidad & GitOps

El repositorio es la Única Fuente de Verdad del sistema.

## Principios
1.  **Cero Cambios Manuales**: Prohibido modificar infraestructura o configuración directamente en producción (SSH/Console). Todo cambio debe pasar por un Commit/PR.
2.  **Logs Inmutables**: Las evidencias de ejecución y auditoría solo se agregan (`append`), nunca se sobrescriben ni eliminan (salvo rotación automática).
3.  **Ubicación de Evidencias**: Todo log o reporte generado por automatización debe guardarse exclusivamente en `audit/`.
4.  **Push to Origin**: Todos los archivos generados (código, documentación, logs, reportes) deben ser subidos al repositorio remoto (`origin`) inmediatamente tras su generación y validación. No deben quedar cambios locales sin versionar.

## Excepciones
Solo en casos de emergencia crítica (Break-Glass) se permite intervención manual, la cual debe ser documentada *a posteriori* en `audit/incidents/`.
