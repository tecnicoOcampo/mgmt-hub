Tu **resumen** de la Unidad 5 está bien enfocado y es correcto; solo le agregaría 1–2 frases al final (te dejo propuesta abajo).  

Ahora voy a hacer lo que pediste: **corregir solo el formato Markdown de la cheatsheet**, sin cambiar el contenido lógico (solo agrego bloques de código).

***

### Resumen Unidad 5 (ligeramente ampliado)

Podés dejar tu `docs/unidad_5_resumen.md` así:

```markdown
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
```

***

### Cheatsheet – corrección solo de formato Markdown

Tomando la versión conceptual que ya tenés, así quedaría bien formateada en `docs/unidad_5_cheatsheet.md`:

```markdown
# Cheatsheet – Funciones en Python (Unidad 5 + extras)

## Definición básica

```
def nombre_funcion(param1, param2):
    """Descripción breve de lo que hace la función."""
    # bloque de código
    return resultado
```

- `def`: palabra clave para definir una función.
- `nombre_funcion`: debe ser descriptivo y en minúsculas, con guiones bajos.
- `return`: devuelve un valor (o nada, si se omite).

---

## Parámetros y argumentos

```
def saludar(nombre):
    print("Hola,", nombre)

saludar("Gonzalo")      # argumento posicional
saludar(nombre="Ana")   # argumento nombrado
```

- Parámetro: la variable en la definición (`nombre`).
- Argumento: el valor real que se pasa al llamar (`"Gonzalo"`).

---

## Valores por defecto

```
def conectar(host="localhost", puerto=3306):
    print("Conectando a", host, "en el puerto", puerto)

conectar()                      # usa valores por defecto
conectar("servidor.remoto")     # cambia host, puerto por defecto
conectar(puerto=8080)           # usa host por defecto, cambia puerto
```

- Evitan repetir los mismos valores en muchas llamadas.
- Se evalúan una vez al definir la función.

---

## Retorno de valores

```
def sumar(a, b):
    return a + b

resultado = sumar(10, 5)
print(resultado)  # 15
```

- Una función puede devolver cualquier tipo: número, string, lista, objeto, etc.
- Si no hay `return`, Python devuelve `None`.

---

## Scope (alcance) de variables

```
x = 10  # variable global

def mostrar():
    x = 5  # variable local
    print("Dentro de la función:", x)

mostrar()
print("Fuera de la función:", x)
```

- Variables **locales**: definidas dentro de la función, solo existen ahí.
- Variables **globales**: definidas fuera, visibles en todo el módulo (mejor usarlas poco).

---

## Funciones como herramienta de modularización

Buena práctica: una función debe tener **una responsabilidad clara**.

```
def calcular_total(precios):
    """Suma todos los precios de una lista."""
    return sum(precios)

def mostrar_total_en_pantalla(total):
    """Muestra el total formateado."""
    print(f"Total: ${total:.2f}")
```

Separar lógica de cálculo y lógica de presentación mejora la legibilidad.

---

## Ejemplos de MGMT-Hub

```
def guardar_tareas(tareas):
    """Guarda la lista completa de tareas en el archivo JSON de datos."""
    lista_dicts = [tarea_a_dict(t) for t in tareas]
    with open(RUTA_TAREAS, "w", encoding="utf-8") as f:
        json.dump(lista_dicts, f, ensure_ascii=False, indent=2)


def cargar_tareas():
    """
    Carga las tareas desde el archivo JSON de datos.

    Retorna:
        Lista de objetos Tarea. Si el archivo no existe, retorna una lista vacía.
    """
    if not os.path.exists(RUTA_TAREAS):
        return []
    with open(RUTA_TAREAS, "r", encoding="utf-8") as f:
        lista_dicts = json.load(f)
    return [dict_a_tarea(d) for d in lista_dicts]
```

- Ejemplo real de uso de funciones para separar responsabilidades.

---

## Extras (más allá del libro)

### `*args` – cantidad variable de argumentos posicionales

```
def sumar_todos(*args):
    """Suma todos los números que reciba."""
    return sum(args)

print(sumar_todos(1, 2, 3))        # 6
print(sumar_todos(10, 20, 30, 40)) # 100
```

- `*args` agrupa todos los argumentos posicionales en una tupla.

---

### `**kwargs` – argumentos nombrados variables

```
def mostrar_config(**kwargs):
    """Muestra claves y valores de configuración."""
    for clave, valor in kwargs.items():
        print(clave, "=", valor)

mostrar_config(host="localhost", puerto=3306, debug=True)
```

- `**kwargs` agrupa los argumentos nombrados en un diccionario.

---

### Funciones lambda (anónimas)

```
doble = lambda x: x * 2

print(doble(5))  # 10

numeros =
cuadrados = list(map(lambda n: n * n, numeros))
print(cuadrados)  #
```

- Útiles para funciones cortas “de una sola línea”.
- Se usan mucho con `map`, `filter`, `sorted`, etc.

---

### Funciones que llaman a otras funciones

```
def crear_tarea_desde_input():
    """Pide datos al usuario y devuelve una nueva tarea."""
    # ...
    return Tarea(...)

def agregar_tarea(tareas):
    """Crea una tarea y la agrega a la lista, si es válida."""
    nueva = crear_tarea_desde_input()
    if nueva is not None:
        tareas.append(nueva)
```

- Ayuda a dividir tareas complejas en pasos más simples.
- Mejora la legibilidad y facilita las pruebas.

---

## Buenas prácticas generales

- Nombres descriptivos (en minúsculas, con `_`): `crear_tarea_desde_input`.
- Una función = una responsabilidad clara.
- Usar docstrings según PEP 257 para documentar qué hace cada función.
- Mantener las funciones cortas y legibles: si una hace demasiado, probablemente haya que dividirla.
```

Solo tenés que pegar esto encima de tu cheatsheet actual.

Pregunta de chequeo:  
¿Ves ahora en GitHub que los bloques de código de la cheatsheet se renderizan con formato (cuadro gris y coloreado), no como texto plano?