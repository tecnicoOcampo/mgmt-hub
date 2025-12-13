# **Resumen \- Unidad 5: Funciones en Python**

Estudiante: Gonzalo Ocampo  
Materia: Programación 1  
Profesor: Juan Pablo Sosa  
Fecha: Diciembre 2025

---

## **Introducción**

Las funciones son uno de los pilares fundamentales de la programación en Python. Permiten organizar el código en bloques reutilizables que realizan tareas específicas, mejorando la legibilidad, mantenibilidad y eficiencia del desarrollo de software.

Una función es un bloque de código diseñado para resolver un trabajo específico, agrupado bajo un nombre identificable que permite invocarlo en cualquier parte del programa cuando sea necesario.

---

## **¿Qué es una Función?**

Una función es un bloque de código que:

* Realiza una tarea específica y bien definida  
* Puede recibir datos de entrada mediante parámetros  
* Puede devolver un resultado mediante la instrucción return  
* Es reutilizable en diferentes partes del programa

## **Beneficios de usar funciones**

1. Modularización: Divide el código en partes más pequeñas y manejables  
2. Reutilización: Evita duplicar código (principio DRY \- Don't Repeat Yourself)  
3. Legibilidad: Hace el código más comprensible al describir claramente su propósito  
4. Mantenibilidad: Facilita correcciones y mejoras al centralizar la lógica  
5. Escalabilidad: Permite trabajar en proyectos más complejos de forma organizada

---

## **Definición de una Función**

Para crear una función en Python se utiliza la palabra reservada def seguida del nombre de la función, paréntesis y dos puntos:

def mi\_primera\_funcion():  
    """Esta es mi primera función."""  
    print("Hola desde mi primer función")  
      
*\# Llamada a la función*  
mi\_primera\_funcion()

## **Elementos de la definición**

1. def: Palabra reservada que indica la definición de una función  
2. Nombre de la función: Debe ser descriptivo y seguir las reglas de nomenclatura (snake\_case)  
3. Paréntesis (): Contienen los parámetros (pueden estar vacíos)  
4. Dos puntos :: Finalizan la declaración e inician el bloque de código  
5. Cuerpo indentado: Conjunto de instrucciones que se ejecutarán al llamar la función  
6. Docstring (opcional pero recomendado): Documentación de la función entre comillas triples

## **Reglas importantes**

* No se puede invocar una función antes de que haya sido definida  
* Una función y una variable no pueden compartir el mismo nombre  
* Si no se llama a la función, el código dentro de ella nunca se ejecutará

---

## **Funciones con Parámetros**

Los parámetros permiten que una función reciba datos de entrada para trabajar con ellos.

def saludar\_usuario(nombre):  
    """  
    Saluda a un usuario por su nombre.

    Args:  
        nombre (str): El nombre del usuario a saludar  
    """  
    print(f"¡Hola, {nombre}\!")  
      
*\# Llamada con argumento*  
saludar\_usuario("Gonzalo")  *\# Salida: ¡Hola, Gonzalo\!*

## **Características de los parámetros**

* Existen solo dentro de la función donde fueron definidos (scope local)  
* Se definen entre paréntesis en la declaración de la función  
* Reciben valores cuando la función es invocada (argumentos)  
* Deben coincidir en número con los argumentos pasados (a menos que tengan valores por defecto)

## **Parámetros con valores por defecto**

Permiten hacer parámetros opcionales asignándoles un valor predeterminado:

def sumar(a, b=0):  
    """  
    Suma dos números.  
      
    Args:  
        a (float): Primer número  
        b (float, optional): Segundo número. Por defecto es 0\.  
      
    Returns:  
        float: La suma de a y b  
    """  
    return a \+ b

print(sumar(5))      *\# 5 (usa b=0 por defecto)*  
print(sumar(5, 3))   *\# 8*

---

## **La Instrucción return**

La palabra reservada return permite que una función devuelva un valor al punto desde donde fue llamada.

def multiplicar(a, b):  
    """  
    Multiplica dos números y retorna el resultado.  
      
    Args:  
        a (float): Primer número  
        b (float): Segundo número  
      
    Returns:  
        float: El producto de a y b  
    """  
    return a \* b

resultado \= multiplicar(4, 7)  
print(resultado)  *\# 28*

## **Características de return**

* Finaliza la ejecución de la función inmediatamente  
* Devuelve un valor al código que llamó la función  
* Es opcional: Si no se especifica, la función retorna None implícitamente  
* Puede retornar múltiples valores (como tupla): return a, b, c

## **return sin valor**

Puede usarse solo para terminar la ejecución de una función antes de llegar al final:

def validar\_edad(edad):  
    """Valida si la edad es válida para continuar."""  
    if edad \< 0:  
        print("Edad inválida")  
        return  *\# Termina aquí si la edad es negativa*  
      
    print(f"Edad válida: {edad}")

validar\_edad(-5)  *\# Imprime "Edad inválida" y termina*  
validar\_edad(25)  *\# Imprime "Edad válida: 25"*  
---

## **Argumentos Posicionales y con Nombre**

## **Argumentos posicionales**

El orden importa: cada argumento se asigna al parámetro según su posición.

def describir\_persona(nombre, edad, ciudad):  
    """Describe una persona con su información."""  
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

describir\_persona("Gonzalo", 25, "Argentina")

## **Argumentos con nombre (keyword arguments)**

Se especifica explícitamente qué valor corresponde a cada parámetro:

describir\_persona(edad=25, ciudad="Argentina", nombre="Gonzalo")  
*\# El orden no importa cuando usamos nombres*  
---

## **Parámetros con Número Variable de Argumentos**

## **\*args \- Argumentos posicionales variables**

Permite recibir cualquier cantidad de argumentos posicionales (se almacenan en una tupla):

def sumar\_todos(\*numeros):  
    """  
    Suma todos los números recibidos.  
      
    Args:  
        \*numeros: Cantidad variable de números  
      
    Returns:  
        float: La suma total  
    """  
    total \= sum(numeros)  
    return total

print(sumar\_todos(1, 2, 3, 4, 5))  *\# 15*  
print(sumar\_todos(10, 20))          *\# 30*

## **\*\*kwargs \- Argumentos con nombre variables**

Permite recibir cualquier cantidad de argumentos con nombre (se almacenan en un diccionario):

def mostrar\_info(\*\*datos):  
    """  
    Muestra información recibida como pares clave-valor.  
      
    Args:  
        \*\*datos: Datos con nombre en cantidad variable  
    """  
    for clave, valor in datos.items():  
        print(f"{clave}: {valor}")

mostrar\_info(nombre="Juan", edad=25, ciudad="Madrid")  
*\# Salida:*  
*\# nombre: Juan*  
*\# edad: 25*  
*\# ciudad: Madrid*

---

## **Scope (Alcance) de Variables**

El scope define en qué partes del código una variable puede usarse.

## **Variables locales**

Se crean dentro de una función y solo existen en ese contexto:

def calcular():  
    resultado \= 10 \* 2  *\# Variable local*  
    return resultado

print(calcular())   *\# 20*  
print(resultado)    *\# Error: resultado no existe fuera de la función*

## **Variables globales**

Se definen fuera de cualquier función y pueden usarse en todo el código:

contador \= 0  *\# Variable global*

def incrementar():  
    global contador  *\# Declaramos que usaremos la global*  
    contador \+= 1

incrementar()  
print(contador)  *\# 1*

## **Buenas prácticas con scope**

* Minimizar el uso de variables globales para evitar efectos secundarios  
* Pasar datos mediante parámetros en lugar de usar globales  
* Retornar valores en lugar de modificar variables externas  
* Usar nombres descriptivos para distinguir variables locales y globales

---

## **Flujo de Ejecución de una Función**

1. Python encuentra la llamada a la función  
2. Recuerda el lugar desde donde fue llamada  
3. Salta al inicio de la función  
4. Ejecuta el cuerpo de la función línea por línea  
5. Al llegar a return o al final, regresa al punto de llamada  
6. Continúa la ejecución normal del programa

Este proceso se repite cada vez que la función es invocada.

---

## **Documentación de Funciones: Docstrings**

Los docstrings son cadenas de documentación que describen qué hace una función, sus parámetros y su valor de retorno.

def dividir(dividendo, divisor):  
    """  
    Divide dos números y retorna el resultado redondeado.  
      
    Esta función realiza la división entre el dividendo y el divisor,  
    manejando el caso especial de división por cero.  
      
    Args:  
        dividendo (float): El número que será dividido  
        divisor (float): El número por el cual se divide  
      
    Returns:  
        float: El resultado de la división redondeado a 2 decimales  
      
    Raises:  
        ZeroDivisionError: Si el divisor es cero  
        TypeError: Si los argumentos no son números  
      
    Examples:  
        \>\>\> dividir(10, 3\)  
        3.33  
        \>\>\> dividir(8, 2\)  
        4.0  
    """  
    if not isinstance(dividendo, (int, float)):  
        raise TypeError("El dividendo debe ser un número")  
    if not isinstance(divisor, (int, float)):  
        raise TypeError("El divisor debe ser un número")  
    if divisor \== 0:  
        raise ZeroDivisionError("No se puede dividir entre cero")  
      
    resultado \= dividendo / divisor  
    return round(resultado, 2)

## **Estándar PEP 257**

* Usar comillas triples """ para docstrings  
* Primera línea: resumen breve de la función  
* Línea en blanco  
* Descripción detallada (si es necesario)  
* Documentar parámetros, retorno y excepciones

---

## **Buenas Prácticas con Funciones**

## **1\. Principio de Responsabilidad Única (SRP)**

Cada función debe hacer una sola cosa y hacerla bien.

*\# ❌ MAL: Hace demasiadas cosas*  
def procesar\_usuario(nombre, email):  
    print(f"Usuario: {nombre}")  
    print(f"Email: {email}")  
    archivo \= open("usuarios.txt", "a")  
    archivo.write(f"{nombre},{email}\\n")  
    archivo.close()

*\# ✅ BIEN: Funciones separadas por responsabilidad*  
def mostrar\_usuario(nombre, email):  
    """Muestra información del usuario."""  
    print(f"Usuario: {nombre}")  
    print(f"Email: {email}")

def guardar\_usuario(nombre, email):  
    """Guarda el usuario en un archivo."""  
    with open("usuarios.txt", "a") as archivo:  
        archivo.write(f"{nombre},{email}\\n")

## **2\. Nombres Descriptivos**

*\# ❌ MAL*  
def f(x, y):  
    return x \* y

*\# ✅ BIEN*  
def calcular\_area\_rectangulo(base, altura):  
    """Calcula el área de un rectángulo."""  
    return base \* altura

## **3\. Evitar Efectos Secundarios**

*\# ❌ MAL: Modifica variable global*  
contador \= 0

def incrementar():  
    global contador  
    contador \+= 1  
    return contador

*\# ✅ BIEN: No modifica estado externo*  
def incrementar(valor):  
    """Incrementa un valor y lo retorna."""  
    return valor \+ 1

contador \= 0  
contador \= incrementar(contador)

## **4\. Validación de Parámetros**

def calcular\_promedio(numeros):  
    """  
    Calcula el promedio de una lista de números.  
      
    Args:  
        numeros (list): Lista de números  
      
    Returns:  
        float: El promedio  
      
    Raises:  
        ValueError: Si la lista está vacía  
        TypeError: Si no es una lista o contiene no-números  
    """  
    if not isinstance(numeros, list):  
        raise TypeError("El argumento debe ser una lista")  
      
    if len(numeros) \== 0:  
        raise ValueError("La lista no puede estar vacía")  
      
    if not all(isinstance(n, (int, float)) for n in numeros):  
        raise TypeError("Todos los elementos deben ser números")  
      
    return sum(numeros) / len(numeros)  
---

## **Aplicación en MGMT-Hub**

En el proyecto MGMT-Hub, las funciones se utilizaron extensivamente siguiendo todas estas prácticas:

## **Ejemplos del proyecto**

*\# core.py \- Funciones puras de lógica de negocio*  
def buscar\_tarea\_por\_id(tareas, id\_buscado):  
    """  
    Busca una tarea por su ID.  
      
    Args:  
        tareas (list): Lista de objetos Tarea  
        id\_buscado (str): ID de la tarea a buscar  
      
    Returns:  
        Tarea|None: La tarea encontrada o None si no existe  
    """  
    for tarea in tareas:  
        if tarea.id \== id\_buscado:  
            return tarea  
    return None

def filtrar\_tareas\_por\_texto(tareas, texto):  
    """  
    Filtra tareas que contengan el texto en título o descripción.  
      
    Args:  
        tareas (list): Lista de objetos Tarea  
        texto (str): Texto a buscar  
      
    Returns:  
        list: Lista de tareas que coinciden con el filtro  
    """  
    resultados \= \[\]  
    texto\_lower \= texto.lower()  
    for tarea in tareas:  
        if (texto\_lower in tarea.titulo.lower() or   
            texto\_lower in tarea.descripcion.lower()):  
            resultados.append(tarea)  
    return resultados  
---

## **Conclusión**

Las funciones son fundamentales en Python y en la programación en general. Permiten:

* Organizar código en bloques lógicos y reutilizables  
* Mejorar la legibilidad mediante nombres descriptivos  
* Facilitar el mantenimiento al centralizar la lógica  
* Reducir errores mediante validación y documentación  
* Trabajar en equipo de forma más eficiente

Dominar el uso de funciones es esencial para escribir código profesional, mantenible y escalable. En MGMT-Hub, las funciones permitieron separar claramente la lógica de negocio (core.py) de la interfaz de usuario (main.py), facilitando futuras expansiones y mantenimiento del proyecto.

---

## **Referencias**

* PEP 257 \- Docstring Conventions:   
* [https://peps.python.org/pep-0257/](https://peps.python.org/pep-0257/)  
* PEP 8 \- Style Guide for Python Code:   
* [https://peps.python.org/pep-0008/](https://peps.python.org/pep-0008/)  
* Python Official Documentation \- Functions:   
* [https://docs.python.org/3/tutorial/controlflow.html\#defining-functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)  
* "Python desde cero, fundamentos claros" \- Juan Pablo Sosa, Unidad 6

