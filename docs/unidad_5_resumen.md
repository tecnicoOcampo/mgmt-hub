# Resumen – Unidad 5: Funciones

En esta unidad se trabajan los conceptos fundamentales de funciones en Python:

- Definición de funciones con `def`.
- Parámetros y argumentos.
- Valores de retorno (`return`).
- Alcance de variables (scope).
- Funciones como herramienta para modularizar y reutilizar código.

Las funciones permiten aplicar el principio DRY (*Don't Repeat Yourself*): en lugar de copiar y pegar código, se encapsula en funciones reutilizables. Esto reduce errores y facilita los cambios.

En MGMT-Hub las funciones se utilizan para:
- separar la lógica de interacción con el usuario (`crear_tarea_desde_input`, `ejecutar_cambio_estado`, `ejecutar_busqueda`),
- encapsular operaciones de negocio (`buscar_tarea_por_id`, `filtrar_tareas_por_texto`, `guardar_tareas`, `cargar_tareas`).

Esto permite que el código sea más legible, fácil de probar y mantener.
