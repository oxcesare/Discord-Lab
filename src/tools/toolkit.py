# toolkit.py
"""
Módulo de registro de capacidades del Agente.
Aquí se centralizan y documentan todas las herramientas disponibles.
"""

from sintaxis_basica.basicos import (
    mostrar_palabras_reservadas,
    mostrar_identificadores,
    mostrar_tipos_datos,
    mostrar_tipos_datos_simples,
    mostrar_tipos_datos_compuestos,
    mostrar_variables_constantes,
    mostrar_operadores_aritmeticos,
    mostrar_operadores_logicos
)
from practica03.agente_logica import obtener_historial_comandos

TOOLKIT = {
    "mostrar_palabras_reservadas": {
        "funcion": mostrar_palabras_reservadas,
        "descripcion": "Muestra las palabras reservadas en Python."
    },
    "mostrar_identificadores": {
        "funcion": mostrar_identificadores,
        "descripcion": "Muestra los identificadores en Python."
    },
    "mostrar_tipos_datos": {
        "funcion": mostrar_tipos_datos,
        "descripcion": "Muestra un resumen de los tipos de datos en Python."
    },
    "mostrar_tipos_datos_simples": {
        "funcion": mostrar_tipos_datos_simples,
        "descripcion": "Muestra los tipos de datos simples en Python."
    },
    "mostrar_tipos_datos_compuestos": {
        "funcion": mostrar_tipos_datos_compuestos,
        "descripcion": "Muestra los tipos de datos compuestos en Python."
    },
    "mostrar_variables_constantes": {
        "funcion": mostrar_variables_constantes,
        "descripcion": "Muestra la diferencia entre variables y constantes en Python."
    },
    "mostrar_operadores_aritmeticos": {
        "funcion": mostrar_operadores_aritmeticos,
        "descripcion": "Muestra los operadores aritméticos en Python."
    },
    "mostrar_operadores_logicos": {
        "funcion": mostrar_operadores_logicos,
        "descripcion": "Muestra los operadores lógicos en Python."
    },
    "historial": {
        "funcion": obtener_historial_comandos,
        "descripcion": "Muestra las últimas interacciones registradas en la sesión."
    }
}