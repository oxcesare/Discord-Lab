#funcion que muestre las palabras reservas de python
def mostrar_palabras_reservadas():
    import keyword
    palabras = keyword.kwlist
    return (
        "Palabras reservadas en Python:\n"
        "Son palabras que ya tienen un significado especial dentro del lenguaje y no deben usarse como nombres de variables o funciones.\n"
        "Ejemplos comunes: if, else, for, while, def, class, return, True, False.\n\n"
        "Lista completa:\n" + ", ".join(palabras)
    )

#funcion que muestre los identificadores en python
def mostrar_identificadores():
    return (
        "Identificadores en Python:\n"
        "Son los nombres que se usan para variables, funciones, clases y módulos.\n"
        "Reglas básicas:\n"
        "- Deben empezar con una letra o con guion bajo (_).\n"
        "- No pueden empezar con números.\n"
        "- No pueden ser palabras reservadas.\n"
        "- Pueden contener letras, números y guiones bajos.\n"
        "Ejemplos válidos: nombre, edad_1, _contador.\n"
        "Ejemplos no válidos: 2edad, mi-variable, class."
    )

# funcion que muestre los   Tipos de datos simples en python
def mostrar_tipos_datos_simples():
    return (
        "Tipos de datos simples en Python:\n"
        "- int: números enteros. Ejemplo: 10\n"
        "- float: números decimales. Ejemplo: 3.14\n"
        "- str: cadenas de texto. Ejemplo: 'Hola'\n"
        "- bool: valores lógicos. Ejemplo: True o False"
    )


def mostrar_tipos_datos():
    return (
        "Tipos de datos en Python:\n"
        "Python maneja tipos de datos simples y compuestos.\n\n"
        f"{mostrar_tipos_datos_simples()}\n\n"
        f"{mostrar_tipos_datos_compuestos()}"
    )

# funcion que muestra losTipos de datos compuestos en python
def mostrar_tipos_datos_compuestos():
    return (
        "Tipos de datos compuestos en Python:\n"
        "- list: colección ordenada y modificable. Ejemplo: [1, 2, 3]\n"
        "- tuple: colección ordenada e inmutable. Ejemplo: (1, 2, 3)\n"
        "- dict: colección de pares clave-valor. Ejemplo: {'nombre': 'Ana'}\n"
        "- set: colección sin elementos repetidos. Ejemplo: {1, 2, 3}"
    )

# funcion que muestra Variables y Constantes en Python
def mostrar_variables_constantes():
    return (
        "Variables y constantes en Python:\n"
        "- Variable: espacio en memoria cuyo valor puede cambiar durante la ejecución.\n"
        "  Ejemplo: edad = 20\n"
        "- Constante: en Python no existe una constante real, pero por convención se escribe en mayúsculas para indicar que no debería modificarse.\n"
        "  Ejemplo: PI = 3.1416"
    )

# funcion que muestra Operadores aritméticos en Python
def mostrar_operadores_aritmeticos():
    return (
        "Operadores aritméticos en Python:\n"
        "- + suma. Ejemplo: 2 + 3 = 5\n"
        "- - resta. Ejemplo: 5 - 2 = 3\n"
        "- * multiplicación. Ejemplo: 4 * 2 = 8\n"
        "- / división. Ejemplo: 10 / 2 = 5.0\n"
        "- % módulo o residuo. Ejemplo: 10 % 3 = 1\n"
        "- ** potenciación. Ejemplo: 2 ** 3 = 8\n"
        "- // división entera. Ejemplo: 10 // 3 = 3"
    )

# Funcion que muestra Operadores lógicos en Python
def mostrar_operadores_logicos():
    return (
        "Operadores lógicos en Python:\n"
        "- and: devuelve True si ambas condiciones son verdaderas.\n"
        "  Ejemplo: True and False -> False\n"
        "- or: devuelve True si al menos una condición es verdadera.\n"
        "  Ejemplo: True or False -> True\n"
        "- not: invierte el valor lógico.\n"
        "  Ejemplo: not True -> False"
    )