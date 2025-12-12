from core import (
    Tarea,
    buscar_tarea_por_id,
    filtrar_tareas_por_texto,
    guardar_tareas,
    cargar_tareas,
)

from rich.console import Console

console = Console()


def mostrar_menu():
    """
    Muestra el menú principal de opciones en la consola.
    """
    print("\n=== MGMT-Hub ===")
    print("1) Crear nueva tarea")
    print("2) Listar tareas")
    print("3) Cambiar estado de una tarea")
    print("4) Buscar tareas por título o contexto")
    print("0) Salir")


def crear_tarea_desde_input():
    """
    Solicita al usuario los datos necesarios y construye una nueva Tarea.

    Retorna:
        Una instancia de Tarea con los valores ingresados por teclado.
    """
    print("\nCrear nueva tarea")
    titulo = input("Título: ")
    req_min = input("Requerimientos mínimos: ")
    contexto = input("Contexto: ")
    referencias = input("Referencias: ")
    tags_texto = input("Tags (separadas por coma): ")
    tags = [t.strip() for t in tags_texto.split(",")] if tags_texto else []
    prioridad = input("Prioridad (baja/media/alta): ")
    estado = input("Estado (pendiente/en progreso/completada): ")
    fecha = input("Fecha objetivo (YYYY-MM-DD): ")

    try:
        return Tarea(titulo, req_min, contexto, referencias,
                     tags, prioridad, estado, fecha)
    except ValueError as e:
        print(f"Error al crear la tarea: {e}")
        return None


def ejecutar_cambio_estado(tareas):
    """
    Permite al usuario seleccionar una tarea por ID y cambiar su estado.
    """
    print("\nCambiar estado de una tarea")

    if not tareas:
        print("No hay tareas cargadas.")
        return

    for tarea in tareas:
        tarea.mostrar_resumen()

    id_texto = input("Ingresá el ID de la tarea: ")
    try:
        id_busqueda = int(id_texto)
    except ValueError:
        print("ID inválido.")
        return

    tarea_encontrada = buscar_tarea_por_id(tareas, id_busqueda)
    if tarea_encontrada is None:
        print("No se encontró una tarea con ese ID.")
        return

    nuevo_estado = input("Nuevo estado (pendiente/en progreso/completada): ")
    tarea_encontrada.estado = nuevo_estado
    guardar_tareas(tareas)
    print("Estado actualizado.")


def ejecutar_busqueda(tareas):
    """
    Pide un texto al usuario y muestra
    las tareas que coinciden por título o contexto.
    """
    texto = input("Texto a buscar en título o contexto: ")
    resultados = filtrar_tareas_por_texto(tareas, texto)
    print(f"\nResultados de búsqueda ({len(resultados)}):")
    for tarea in resultados:
        tarea.mostrar_resumen()


def main():
    """
    Punto de entrada principal de MGMT-Hub.

    Se prioriza la legibilidad del flujo principal del programa
    (Zen of Python: "Readability counts").
    """
    tareas = cargar_tareas()
    console.print("[bold green]Bienvenido a MGMT-Hub[/bold green]")
    print(f"Se cargaron {len(tareas)} tareas.\n")

    while True:
        mostrar_menu()
        opcion = input("Opción: ")
        if opcion == "1":
            nueva = crear_tarea_desde_input()
            if nueva is not None:
                tareas.append(nueva)
                guardar_tareas(tareas)
                print("Tarea creada.")
        elif opcion == "2":
            print("\nListado de tareas:")
            if not tareas:
                print("No hay tareas cargadas.")
            for tarea in tareas:
                tarea.mostrar_resumen()
        elif opcion == "3":
            ejecutar_cambio_estado(tareas)
        elif opcion == "4":
            ejecutar_busqueda(tareas)
        elif opcion == "0":
            print("Saliendo de MGMT-Hub.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
