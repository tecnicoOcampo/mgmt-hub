# **Cheatsheet \- Funciones en Python (Ampliada)**

Estudiante: Gonzalo Ocampo  
Materia: Programación 1  
Profesor: Juan Pablo Sosa  
Fecha: Diciembre 2025

---

## **📌 Definición Básica**

def nombre\_funcion(parametro1, parametro2):  
    """Docstring: descripción de la función."""  
    *\# Cuerpo de la función*  
    resultado \= parametro1 \+ parametro2  
    return resultado

---

## **📥 Parámetros y Argumentos**

## **Parámetros básicos**

def saludar(nombre):  
    return f"Hola, {nombre}"

saludar("Gonzalo")  *\# "Hola, Gonzalo"*

## **Parámetros con valores por defecto**

def sumar(a, b=0):  
    return a \+ b

sumar(5)      *\# 5 (usa b=0)*  
sumar(5, 3)   *\# 8*

## **Argumentos posicionales**

def dividir(dividendo, divisor):  
    return dividendo / divisor

dividir(10, 2)  *\# El orden importa: 10/2 \= 5*

## **Argumentos con nombre (keyword)**

def describir(nombre, edad, ciudad):  
    return f"{nombre}, {edad} años, {ciudad}"

*\# Orden no importa con keywords*  
describir(edad=25, ciudad="CABA", nombre="Juan")

## **\*args \- Múltiples argumentos posicionales**

def sumar\_todos(\*numeros):  
    """Acepta cualquier cantidad de números."""  
    return sum(numeros)

sumar\_todos(1, 2, 3, 4, 5)  *\# 15*  
sumar\_todos(10, 20)          *\# 30*

## **\*\*kwargs \- Múltiples argumentos con nombre**

def mostrar\_config(\*\*opciones):  
    """Acepta cualquier cantidad de opciones."""  
    for clave, valor in opciones.items():  
        print(f"{clave}: {valor}")

mostrar\_config(debug=True, timeout=30, host="localhost")

## **Combinación de todos los tipos**

def funcion\_completa(arg\_requerido, arg\_default=10, \*args, \*\*kwargs):  
    """Combina todos los tipos de parámetros."""  
    print(f"Requerido: {arg\_requerido}")  
    print(f"Default: {arg\_default}")  
    print(f"Args: {args}")  
    print(f"Kwargs: {kwargs}")

funcion\_completa(1, 2, 3, 4, 5, nombre="Test", activo=True)

---

## **📤 Return \- Retorno de Valores**

## **Return simple**

def multiplicar(a, b):  
    return a \* b

resultado \= multiplicar(3, 4)  *\# 12*

## **Return múltiple (tupla)**

def dividir\_con\_resto(dividendo, divisor):  
    cociente \= dividendo // divisor  
    resto \= dividendo % divisor  
    return cociente, resto

c, r \= dividir\_con\_resto(17, 5)  *\# c=3, r=2*

## **Return temprano (early return)**

def validar\_edad(edad):  
    if edad \< 0:  
        return "Error: edad negativa"  
    if edad \< 18:  
        return "Menor de edad"  
    return "Mayor de edad"

## **Sin return (retorna None implícitamente)**

def imprimir\_mensaje(texto):  
    print(texto)  
    *\# No hay return, retorna None automáticamente*

resultado \= imprimir\_mensaje("Hola")  *\# resultado \= None*

---

## **🔍 Scope \- Alcance de Variables**

## **Variables locales**

def calcular():  
    x \= 10  *\# Variable local*  
    return x \* 2

calcular()  *\# 20*  
*\# print(x)  \# Error: x no existe fuera de la función*

## **Variables globales**

contador \= 0  *\# Global*

def incrementar():  
    global contador  *\# Modificar global*  
    contador \+= 1

incrementar()  
print(contador)  *\# 1*

## **Variables nonlocal (funciones anidadas)**

def externa():  
    x \= 10  
      
    def interna():  
        nonlocal x  *\# Modificar variable de función externa*  
        x \+= 5  
      
    interna()  
    return x

externa()  *\# 15*

---

## **📝 Docstrings \- Documentación**

## **Docstring simple**

def sumar(a, b):  
    """Suma dos números y retorna el resultado."""  
    return a \+ b

## **Docstring completo (Google Style)**

def procesar\_datos(datos, opciones=None):  
    """  
    Procesa una lista de datos según las opciones especificadas.  
      
    Esta función toma una lista de datos y aplica transformaciones  
    según las opciones proporcionadas. Si no se especifican opciones,  
    usa valores por defecto.  
      
    Args:  
        datos (list): Lista de datos a procesar  
        opciones (dict, optional): Diccionario con opciones de procesamiento.  
            Por defecto es None, lo que usa opciones predeterminadas.  
      
    Returns:  
        list: Lista de datos procesados  
      
    Raises:  
        TypeError: Si datos no es una lista  
        ValueError: Si la lista está vacía  
      
    Examples:  
        \>\>\> procesar\_datos(\[1, 2, 3\])  
        \[2, 4, 6\]  
        \>\>\> procesar\_datos(\[1, 2, 3\], {"multiplicador": 3})  
        \[3, 6, 9\]  
    """  
    if not isinstance(datos, list):  
        raise TypeError("datos debe ser una lista")  
    if len(datos) \== 0:  
        raise ValueError("La lista no puede estar vacía")  
      
    if opciones is None:  
        opciones \= {"multiplicador": 2}  
      
    multiplicador \= opciones.get("multiplicador", 1)  
    return \[x \* multiplicador for x in datos\]

## **Acceder a docstrings**

print(sumar.\_\_doc\_\_)          *\# Muestra el docstring*  
help(sumar)                    *\# Muestra ayuda completa*

---

## **🔧 Funciones Avanzadas (No en el Libro)**

## **Lambda \- Funciones anónimas**

*\# Función normal*  
def cuadrado(x):  
    return x \*\* 2

*\# Lambda equivalente (función anónima)*  
cuadrado\_lambda \= lambda x: x \*\* 2

cuadrado(5)         *\# 25*  
cuadrado\_lambda(5)  *\# 25*

*\# Uso común: con map, filter, sorted*  
numeros \= \[1, 2, 3, 4, 5\]  
cuadrados \= list(map(lambda x: x\*\*2, numeros))  *\# \[1, 4, 9, 16, 25\]*  
pares \= list(filter(lambda x: x % 2 \== 0, numeros))  *\# \[2, 4\]*

## **Decoradores (Decorators)**

*\# Decorador básico*  
def mi\_decorador(func):  
    """Decorador que agrega funcionalidad antes/después."""  
    def wrapper(\*args, \*\*kwargs):  
        print("Antes de ejecutar la función")  
        resultado \= func(\*args, \*\*kwargs)  
        print("Después de ejecutar la función")  
        return resultado  
    return wrapper

@mi\_decorador  
def saludar(nombre):  
    print(f"Hola, {nombre}")

saludar("Gonzalo")  
*\# Salida:*  
*\# Antes de ejecutar la función*  
*\# Hola, Gonzalo*  
*\# Después de ejecutar la función*

## **Decorador con parámetros**

def repetir(veces):  
    """Decorador que repite la ejecución N veces."""  
    def decorador(func):  
        def wrapper(\*args, \*\*kwargs):  
            for \_ in range(veces):  
                resultado \= func(\*args, \*\*kwargs)  
            return resultado  
        return wrapper  
    return decorador

@repetir(3)  
def decir\_hola():  
    print("Hola\!")

decir\_hola()  
*\# Salida:*  
*\# Hola\!*  
*\# Hola\!*  
*\# Hola\!*

## **Decorador @functools.wraps**

from functools import wraps

def mi\_decorador(func):  
    @wraps(func)  *\# Preserva metadata de la función original*  
    def wrapper(\*args, \*\*kwargs):  
        print(f"Llamando a {func.\_\_name\_\_}")  
        return func(\*args, \*\*kwargs)  
    return wrapper

@mi\_decorador  
def sumar(a, b):  
    """Suma dos números."""  
    return a \+ b

print(sumar.\_\_name\_\_)  *\# "sumar" (sin @wraps sería "wrapper")*  
print(sumar.\_\_doc\_\_)   *\# "Suma dos números."*

## **Funciones como objetos de primera clase**

*\# Asignar función a variable*  
def saludar():  
    return "Hola"

mi\_funcion \= saludar  
print(mi\_funcion())  *\# "Hola"*

*\# Pasar función como argumento*  
def ejecutar\_dos\_veces(func, valor):  
    """Ejecuta una función dos veces."""  
    func(valor)  
    func(valor)

def imprimir(x):  
    print(x)

ejecutar\_dos\_veces(imprimir, "Hola")  
*\# Salida:*  
*\# Hola*  
*\# Hola*

*\# Retornar función*  
def crear\_multiplicador(n):  
    """Crea una función que multiplica por n."""  
    def multiplicar(x):  
        return x \* n  
    return multiplicar

por\_dos \= crear\_multiplicador(2)  
por\_tres \= crear\_multiplicador(3)

print(por\_dos(5))   *\# 10*  
print(por\_tres(5))  *\# 15*

## **Closures (Clausuras)**

def contador():  
    """Closure que mantiene estado entre llamadas."""  
    cuenta \= 0  
      
    def incrementar():  
        nonlocal cuenta  
        cuenta \+= 1  
        return cuenta  
      
    return incrementar

c1 \= contador()  
print(c1())  *\# 1*  
print(c1())  *\# 2*  
print(c1())  *\# 3*

c2 \= contador()  *\# Nuevo contador independiente*  
print(c2())  *\# 1*

## **Recursión**

def factorial(n):  
    """  
    Calcula el factorial de n recursivamente.  
      
    Args:  
        n (int): Número entero positivo  
      
    Returns:  
        int: El factorial de n  
    """  
    if n \== 0 or n \== 1:  *\# Caso base*  
        return 1  
    return n \* factorial(n \- 1)  *\# Caso recursivo*

print(factorial(5))  *\# 120*

*\# Fibonacci recursivo*  
def fibonacci(n):  
    """Retorna el n-ésimo número de Fibonacci."""  
    if n \<= 1:  
        return n  
    return fibonacci(n-1) \+ fibonacci(n-2)

print(fibonacci(7))  *\# 13*

## **Type Hints (Anotaciones de Tipo)**

from typing import List, Dict, Optional, Union, Tuple

def procesar\_lista(numeros: List\[int\]) \-\> List\[int\]:  
    """  
    Procesa una lista de enteros.  
      
    Args:  
        numeros: Lista de números enteros  
      
    Returns:  
        Lista procesada de enteros  
    """  
    return \[n \* 2 for n in numeros\]

def buscar\_usuario(id: int) \-\> Optional\[Dict\[str, str\]\]:  
    """  
    Busca un usuario por ID.  
      
    Args:  
        id: ID del usuario  
      
    Returns:  
        Diccionario con datos del usuario o None si no existe  
    """  
    usuarios \= {1: {"nombre": "Juan", "email": "juan@mail.com"}}  
    return usuarios.get(id)

def dividir(a: Union\[int, float\], b: Union\[int, float\]) \-\> float:  
    """Divide dos números (int o float)."""  
    return a / b

def obtener\_coordenadas() \-\> Tuple\[float, float\]:  
    """Retorna una tupla de coordenadas (x, y)."""  
    return 10.5, 20.3

## **Generators (Generadores)**

def contador(max: int):  
    """  
    Generador que cuenta hasta max.  
      
    Uso de memoria eficiente: genera valores uno a la vez.  
    """  
    n \= 0  
    while n \< max:  
        yield n  *\# Retorna valor y pausa ejecución*  
        n \+= 1

*\# Uso del generador*  
for numero in contador(5):  
    print(numero)  *\# 0, 1, 2, 3, 4*

*\# Generator expression (como list comprehension)*  
cuadrados\_gen \= (x\*\*2 for x in range(1000000))  *\# No consume memoria*  
primer\_cuadrado \= next(cuadrados\_gen)  *\# 0*

## **Funciones parciales (functools.partial)**

from functools import partial

def potencia(base, exponente):  
    """Calcula base elevado a exponente."""  
    return base \*\* exponente

*\# Crear función especializada*  
cuadrado \= partial(potencia, exponente=2)  
cubo \= partial(potencia, exponente=3)

print(cuadrado(5))  *\# 25*  
print(cubo(5))      *\# 125*

## **Cache/Memoization**

from functools import lru\_cache

@lru\_cache(maxsize=128)  
def fibonacci\_optimizado(n):  
    """  
    Fibonacci con cache para evitar recálculos.  
      
    Mucho más eficiente que la versión recursiva simple.  
    """  
    if n \<= 1:  
        return n  
    return fibonacci\_optimizado(n-1) \+ fibonacci\_optimizado(n-2)

print(fibonacci\_optimizado(100))  *\# Instantáneo con cache*  
print(fibonacci\_optimizado.cache\_info())  *\# Estadísticas del cache*

---

## **⚡ Buenas Prácticas**

## **✅ DO (Hacer)**

*\# Nombres descriptivos*  
def calcular\_promedio\_estudiantes(calificaciones):  
    return sum(calificaciones) / len(calificaciones)

*\# Una responsabilidad por función*  
def leer\_archivo(ruta):  
    """Solo lee el archivo."""  
    with open(ruta, 'r') as f:  
        return f.read()

def procesar\_datos(datos):  
    """Solo procesa datos."""  
    return datos.strip().split('\\n')

*\# Documentar con docstrings*  
def funcion\_importante(param):  
    """Descripción clara de la función."""  
    pass

*\# Validar parámetros*  
def dividir(a, b):  
    if b \== 0:  
        raise ValueError("No se puede dividir por cero")  
    return a / b

## **❌ DON'T (Evitar)**

*\# Nombres ambiguos*  
def f(x):  *\# ¿Qué hace f?*  
    return x \* 2

*\# Funciones muy largas (hacer demasiado)*  
def procesar\_todo():  
    *\# 200 líneas de código...*  
    pass

*\# Sin documentación*  
def funcion\_misteriosa(a, b, c):  
    return a \+ b \* c  *\# ¿Qué significa esto?*

*\# Modificar variables globales*  
contador \= 0  
def incrementar():  
    global contador  
    contador \+= 1  *\# Efecto secundario*

---

## **🎯 Ejemplos Prácticos del Proyecto MGMT-Hub**

## **Función de búsqueda**

def buscar\_tarea\_por\_id(tareas: list, id\_buscado: str) \-\> Optional\[Tarea\]:  
    """  
    Busca una tarea por su ID único.  
      
    Args:  
        tareas: Lista de objetos Tarea  
        id\_buscado: ID de la tarea a buscar  
      
    Returns:  
        La tarea encontrada o None si no existe  
    """  
    for tarea in tareas:  
        if tarea.id \== id\_buscado:  
            return tarea  
    return None

## **Función de filtrado**

def filtrar\_tareas\_por\_texto(tareas: list, texto: str) \-\> list:  
    """  
    Filtra tareas que contengan el texto en título o descripción.  
      
    Args:  
        tareas: Lista de objetos Tarea  
        texto: Texto a buscar (case-insensitive)  
      
    Returns:  
        Lista de tareas que coinciden con el filtro  
    """  
    resultados \= \[\]  
    texto\_lower \= texto.lower()  
    for tarea in tareas:  
        if (texto\_lower in tarea.titulo.lower() or   
            texto\_lower in tarea.descripcion.lower()):  
            resultados.append(tarea)  
    return resultados

## **Función de persistencia**

def guardar\_tareas(tareas: list) \-\> None:  
    """  
    Guarda la lista de tareas en archivo JSON.  
      
    Args:  
        tareas: Lista de objetos Tarea a persistir  
      
    Raises:  
        IOError: Si hay error al escribir el archivo  
    """  
    lista\_dicts \= \[tarea\_a\_dict(t) for t in tareas\]  
    with open(RUTA\_TAREAS, "w", encoding="utf-8") as f:  
        json.dump(lista\_dicts, f, ensure\_ascii=False, indent=2)

---

## **📚 Referencias Adicionales**

* PEP 257 \- Docstring Conventions:   
* [https://peps.python.org/pep-0257/](https://peps.python.org/pep-0257/)  
* PEP 8 \- Style Guide:   
* [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)  
* Type Hints (PEP 484):   
* [https://peps.python.org/pep-0484/](https://peps.python.org/pep-0484/)  
* Python functools:   
* [https://docs.python.org/3/library/functools.html](https://docs.python.org/3/library/functools.html)  
* Python typing:   
* [https://docs.python.org/3/library/typing.html](https://docs.python.org/3/library/typing.html)

---

Nota: Esta cheatsheet amplía el contenido del libro "Python desde cero, fundamentos claros" (Unidad 6\) con métodos y técnicas avanzadas para funciones en Python, incluyendo decoradores, generadores, type hints, y optimizaciones que son usadas en desarrollo profesional.

