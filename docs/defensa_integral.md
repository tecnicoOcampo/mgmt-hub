# Defensa Integral del Proyecto: MGMT-Hub

## Sistema de Gestión de Tareas en Python

Estudiante: Gonzalo Ocampo  
Materia: Programación 1  
Profesor: Juan Pablo Sosa  
Fecha: Diciembre 2025

---

## **1\. Presentación del Programa**

MGMT-Hub es un sistema de gestión de tareas (CRUD) desarrollado en Python, diseñado para operar desde una interfaz de línea de comandos (CLI). Su objetivo principal es permitir a los usuarios crear, listar, buscar, filtrar y modificar el estado de sus tareas diarias de manera eficiente y persistente.

El proyecto no solo busca cumplir una funcionalidad, sino demostrar la aplicación de principios de ingeniería de software como modularidad, mantenibilidad y legibilidad.

---

## **2\. Justificación de Decisiones Técnicas**

## **2.1. Implementación de Métodos y Funciones**

El código se estructura fundamentalmente en funciones, siguiendo el paradigma procedural pero organizado en módulos. Cada función cumple con el principio de responsabilidad única (SRP):

* Funciones de Lógica (core.py): Se crearon funciones puras que reciben datos y retornan resultados sin interactuar con la consola (ej. buscar\_tarea\_por\_id, filtrar\_tareas\_por\_texto).  
* Funciones de Interfaz (main.py): Gestionan la entrada/salida (input/print) y llaman a las funciones del núcleo.

Ejemplo de justificación:  
Se decidió separar la lógica de guardado en guardar\_tareas(tareas) para que pueda ser invocada desde cualquier parte del programa (al crear, al modificar, al borrar), evitando duplicar el código de escritura de archivos (Principio DRY).

## **2.2. Uso de Docstrings y Comentarios**

Se adoptó el estándar PEP 257 para la documentación:

* Docstrings: Todas las funciones públicas incluyen un docstring que explica *qué* hace, sus argumentos y qué retorna. Esto permite entender la función sin leer su código interno y facilita el uso de herramientas como help().  
* Comentarios: Se limitaron a explicar el *por qué* de decisiones complejas o lógica no trivial, evitando comentar lo obvio (como \# asigna variable).

## **2.3. Buenas Prácticas y Código Limpio**

Para garantizar un código limpio ("Clean Code"), se aplicaron:

* Nombres descriptivos: Variables como fecha\_creacion o funciones como crear\_tarea\_desde\_input comunican su intención claramente.  
* Manejo de Excepciones: Se utiliza try/except para manejar errores previsibles (como archivos corruptos o inputs inválidos) sin que el programa colapse.  
* Evitar "Magic Numbers/Strings": Uso de constantes (ej. RUTA\_TAREAS) para facilitar cambios futuros en un solo lugar.

---

## **3\. Organización del Proyecto**

La estructura de archivos separa claramente las responsabilidades:

mgmt-hub/  
├── core.py           \# Lógica pura (Business Logic)  
├── main.py           \# Interfaz de usuario (Presentation Layer)  
├── data/             \# Almacenamiento de datos  
│   └── tareas.json  
├── docs/             \# Documentación académica  
└── venv/             \# Entorno virtual

Justificación: Esta separación permite que, en el futuro, se pueda cambiar la interfaz (por ejemplo, a una web con Flask o GUI con Tkinter) reemplazando solo main.py y manteniendo intacto core.py.

---

## **4\. Aplicación del Zen de Python y PEP8**

El proyecto respeta las guías de estilo de PEP 8 (indentación de 4 espacios, snake\_case para funciones, espacios alrededor de operadores).

Principios del Zen de Python aplicados:

1. "Explicit is better than implicit": No se asumen comportamientos ocultos; las funciones piden explícitamente lo que necesitan.  
2. "Readability counts": Se priorizó un código verbal y espaciado sobre "oneliners" complejos y difíciles de leer.  
3. "Simple is better than complex": Se utilizaron listas de diccionarios y JSON, estructuras nativas simples y efectivas, evitando sobreingeniería innecesaria.

---

## **5\. Entorno Virtual y Desarrollo Colaborativo**

## **5.1. Justificación del uso de venv**

El uso de un entorno virtual (venv) es crítico para aislar las dependencias del proyecto. MGMT-Hub utiliza librerías externas como rich (para formato en terminal) y pendulum (para fechas).

* Sin venv, estas librerías se instalarían en el Python global del sistema, pudiendo causar conflictos con otros proyectos.  
* Con venv, el proyecto es autocontenido.

## **5.2. Facilitando la colaboración**

El archivo requirements.txt permite que cualquier colaborador (como Bruno o Martín) clone el repositorio y ejecute:  
pip install \-r requirements.txt  
Esto garantiza que todos trabajen con exactamente las mismas versiones de las librerías, eliminando el clásico problema de "en mi máquina funciona".

---

## **6\. Contenido del README.md**

El archivo README.md actúa como la portada y manual del proyecto. Su contenido incluye:

1. Descripción del proyecto: Qué es y qué problema resuelve.  
2. Instrucciones de instalación: Pasos claros para clonar, crear el venv e instalar dependencias.  
3. Guía de uso: Ejemplos de comandos para ejecutar el programa.  
4. Estructura del proyecto: Explicación de qué contiene cada archivo.  
5. Autores y Licencia: Créditos correspondientes.

Es la primera pieza de documentación que cualquier desarrollador o evaluador leerá, por lo que su claridad es fundamental para la experiencia del usuario.