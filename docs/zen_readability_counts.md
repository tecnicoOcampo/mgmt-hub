# Reflexión sobre el Zen de Python: "Readability counts"

El principio del Zen de Python seleccionado para este proyecto es:

> Readability counts.  
> (La legibilidad cuenta.)

Este principio destaca que el código debe ser fácil de leer y entender, no solo por quien lo escribió, sino también por otros desarrolladores que lo mantendrán en el futuro. En lugar de priorizar soluciones excesivamente compactas o “ingeniosas”, se favorece un código explícito y claro.

## Cómo se aplica en MGMT-Hub

En MGMT-Hub, este principio se aplicó de varias formas:

1. **Nombres descriptivos**

   Las clases, funciones y variables tienen nombres que describen claramente su propósito:
   - `Tarea`, `buscar_tarea_por_id`, `filtrar_tareas_por_texto`,
   - `guardar_tareas`, `cargar_tareas`, `crear_tarea_desde_input`, etc.

   Esto permite entender el código casi como si fuera un texto en lenguaje natural.

2. **Separación en módulos**

   Se separó la lógica del dominio (`core.py`) de la interfaz de usuario (`main.py`).  
   Esto hace que:
   - `core.py` se enfoque en qué es una tarea y cómo se guarda/busca,
   - `main.py` se enfoque en el flujo del programa y la interacción por consola.

3. **Uso de docstrings y comentarios**

   Cada clase y función tiene una docstring que explica qué hace, sus parámetros y qué retorna.  
   Esto sigue PEP 257 y ayuda a que otros puedan usar las funciones sin leer toda la implementación.

4. **Estructura simple del flujo principal**

   La función `main()` se organiza como un loop claro:
   - mostrar menú,
   - leer opción,
   - ejecutar una acción según el caso.

   Se evitaron construcciones innecesariamente complejas o anidadas, privilegiando un flujo legible incluso para alguien que recién entra al proyecto.

## Ejemplo concreto

En lugar de mezclar toda la lógica dentro de `main()`, se definieron funciones separadas como `ejecutar_cambio_estado(tareas)` y `ejecutar_busqueda(tareas)`. Esto mejora la legibilidad del código y hace que cada parte tenga una responsabilidad clara.

Esta elección está directamente inspirada en el principio “Readability counts”: es más importante que el código sea fácil de leer y mantener, que intentar hacerlo todo en una sola función.