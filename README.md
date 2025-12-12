# MGMT-Hub

MGMT-Hub es una herramienta de línea de comandos en Python pensada para gestionar tareas y objetivos de trabajo IT, estudio y proyectos personales.

El enfoque principal del proyecto es la **legibilidad del código** y la **organización modular**, siguiendo el principio del Zen de Python “Readability counts”.

## Funcionalidades

- Crear tareas con:
  - título
  - requerimientos mínimos
  - contexto
  - referencias
  - tags
  - prioridad
  - estado
  - fecha objetivo (validada con `pendulum`)
- Listar todas las tareas registradas.
- Cambiar el estado de una tarea seleccionada por ID.
- Buscar tareas por texto en título o contexto.
- Guardar y cargar tareas desde un archivo JSON (`data/tareas.json`).

## Estructura del proyecto

mgmt-hub/
├── core.py # Lógica de dominio: clase Tarea, búsqueda, filtros, persistencia
├── main.py # Interfaz de línea de comandos (menú, input del usuario)
├── data/
│ └── tareas.json # Archivo de datos en formato JSON
├── venv/ # Entorno virtual (no se sube completo a GitHub)
├── requirements.txt
└── README.md

La lógica se separa en:

- `core.py`: modelo de datos, funciones de negocio, acceso a archivo JSON.
- `main.py`: flujo principal, interacción por consola, menú y opciones.

## Instalación y entorno virtual

Se recomienda usar un entorno virtual para aislar las dependencias del proyecto:
python -m venv venv

Activar (Windows PowerShell)
venv\Scripts\activate
Activar (Linux/Mac)
source venv/bin/activate

Luego, instalar las dependencias:
pip install -r requirements.txt

### Justificación del entorno virtual

El entorno virtual permite:

- aislar las librerías utilizadas en MGMT-Hub del resto del sistema,
- garantizar que otros desarrolladores puedan reproducir el mismo entorno con `requirements.txt`,
- evitar conflictos de versiones entre diferentes proyectos.

Esto facilita el **desarrollo colaborativo** y la **reproducibilidad del proyecto**.

## Uso

Desde la carpeta del proyecto (con el entorno virtual activado):
python main.py

Menú principal:

- `1` → Crear nueva tarea
- `2` → Listar tareas
- `3` → Cambiar estado de una tarea por ID
- `4` → Buscar tareas por título o contexto
- `0` → Salir

## Módulos utilizados

Módulos propios:

- `core.py`: módulo que define la clase `Tarea` y las funciones de negocio.
- `main.py`: módulo que implementa la interfaz de línea de comandos.

Módulos externos (instalados con `pip`):

- `rich`: utilizado para mejorar la salida en consola (colores y formato).
- `pendulum`: utilizado para validar y manejar fechas en formato `YYYY-MM-DD`.

Módulos estándar:

- `json`, `os`: lectura/escritura de archivos y rutas.

## Zen de Python aplicado

Principio elegido del Zen de Python:

> Readability counts. (La legibilidad cuenta)

Aplicaciones concretas en MGMT-Hub:

- nombres descriptivos para clases, funciones y variables (`Tarea`, `buscar_tarea_por_id`, `guardar_tareas`, etc.),
- uso extensivo de docstrings (PEP 257) y comentarios explicativos,
- separación de responsabilidades entre módulos (`core.py` para la lógica, `main.py` para la interfaz),
- estructura clara del flujo principal en `main()`.

## Trabajo colaborativo

El proyecto está pensado para ser mantenido y extendido por otros desarrolladores:

- estructura modular que facilita agregar nuevas funcionalidades (por ejemplo, nuevos filtros o exportaciones),
- docstrings y comentarios que explican el propósito de cada clase y función,
- uso de un entorno virtual y `requirements.txt` para compartir el entorno de desarrollo.