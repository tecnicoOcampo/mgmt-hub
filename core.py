import json
import os
import pendulum


class Tarea:
    """
    Representa una tarea de MGMT-Hub.

    Diseño basado en nombres claros y estructura simple
    para favorecer la legibilidad del código.
    (Zen of Python: "Readability counts")

    Atributos:
        id: identificador numérico único.
        titulo: título de la tarea.
        requerimientos_minimos: recursos o condiciones mínimas.
        contexto: ámbito donde se realiza (cliente, proyecto, personal, etc.).
        referencias: enlaces o notas de referencia.
        tags: lista de etiquetas de clasificación.
        prioridad: nivel de prioridad (baja, media, alta).
        estado: situación actual (pendiente, en progreso, completada).
        fecha: fecha objetivo en formato YYYY-MM-DD.
    """

    _ultimo_id = 0  # atributo de clase para autoincrementar

    def __init__(self, titulo, requerimientos_minimos, contexto,
                 referencias, tags, prioridad, estado, fecha):
        """
        Crea una nueva instancia de Tarea con un ID autoincremental.
        Valida que la fecha tenga formato correcto YYYY-MM-DD.
        """
        Tarea._ultimo_id += 1
        self.id = Tarea._ultimo_id

        # Validación de fecha con pendulum
        try:
            pendulum.from_format(fecha, "YYYY-MM-DD")
        except pendulum.parsing.exceptions.ParserError:
            raise ValueError("La fecha debe tener formato YYYY-MM-DD")

        self.titulo = titulo
        self.requerimientos_minimos = requerimientos_minimos
        self.contexto = contexto
        self.referencias = referencias
        self.tags = tags
        self.prioridad = prioridad
        self.estado = estado
        self.fecha = fecha

    def mostrar_resumen(self):
        """
        Imprime en consola un resumen legible de la tarea.
        """
        print(
            f"#{self.id} [{self.prioridad.upper()}] "
            f"{self.titulo} - {self.estado} ({self.fecha})"
            f" | {self.contexto}"
        )


def buscar_tarea_por_id(tareas, id_busqueda):
    """
    Busca una tarea por su ID dentro de una lista.

    Parámetros:
        tareas: lista de objetos Tarea.
        id_busqueda: entero con el ID a buscar.

    Retorna:
        La instancia de Tarea encontrada, o None si no existe.
    """
    for tarea in tareas:
        if tarea.id == id_busqueda:
            return tarea
    return None


def filtrar_tareas_por_texto(tareas, texto_busqueda):
    """
    Filtra tareas cuyo título o contexto contengan el texto indicado.

    Parámetros:
        tareas: lista de objetos Tarea.
        texto_busqueda: cadena a buscar (no sensible a mayúsculas).

    Retorna:
        Lista de tareas que coinciden parcialmente con el texto.
    """
    texto_busqueda = texto_busqueda.lower()
    resultados = []
    for tarea in tareas:
        if (texto_busqueda in tarea.titulo.lower()
                or texto_busqueda in tarea.contexto.lower()):
            resultados.append(tarea)
    return resultados


RUTA_TAREAS = os.path.join("data", "tareas.json")


def tarea_a_dict(tarea):
    """
    Convierte un objeto Tarea a un diccionario serializable a JSON.
    """
    return {
        "id": tarea.id,
        "titulo": tarea.titulo,
        "requerimientos_minimos": tarea.requerimientos_minimos,
        "contexto": tarea.contexto,
        "referencias": tarea.referencias,
        "tags": tarea.tags,
        "prioridad": tarea.prioridad,
        "estado": tarea.estado,
        "fecha": tarea.fecha,
    }


def dict_a_tarea(data):
    """
    Convierte un diccionario (proveniente de JSON) en un objeto Tarea.
    Ajusta el contador de IDs para mantenerlos únicos.
    """
    t = Tarea(
        data["titulo"],
        data["requerimientos_minimos"],
        data["contexto"],
        data["referencias"],
        data["tags"],
        data["prioridad"],
        data["estado"],
        data["fecha"],
    )
    t.id = data["id"]
    if data["id"] > Tarea._ultimo_id:
        Tarea._ultimo_id = data["id"]
    return t


def guardar_tareas(tareas):
    """
    Guarda la lista completa de tareas en el archivo JSON de datos.
    """
    lista_dicts = [tarea_a_dict(t) for t in tareas]
    with open(RUTA_TAREAS, "w", encoding="utf-8") as f:
        json.dump(lista_dicts, f, ensure_ascii=False, indent=2)


def cargar_tareas():
    """
    Carga las tareas desde el archivo JSON de datos.

    Retorna:
        Lista de objetos Tarea.
        Si el archivo no existe, retorna una lista vacía.
    """
    if not os.path.exists(RUTA_TAREAS):
        return []
    with open(RUTA_TAREAS, "r", encoding="utf-8") as f:
        lista_dicts = json.load(f)
    return [dict_a_tarea(d) for d in lista_dicts]
