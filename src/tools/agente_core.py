# agente_core.py

# agente_core.py
from src.practica03.agente_logica import (
    ejecutar_suma, 
    buscar_en_diccionario, 
    validar_variable, 
    ejecutar_multiplicacion, 
    obtener_fecha_completa
)

from src.practica04.tareas_agente import (
    agregar_tarea,
    listar_tareas,
    eliminar_tarea
)

TOOLKIT = {
    "validar_sintaxis_variable": {
        "funcion": validar_variable,
        "descripcion": "Valida si un identificador cumple con las reglas de nombrado de Python.",
        "topico": "Sintaxis Básica"
    },
    "calcular_suma": {
        "funcion": ejecutar_suma,
        "descripcion": "Realiza la suma aritmética de dos números proporcionados.",
        "topico": "Operadores y Aritmética"
    },
    "consultar_diccionario": {
        "funcion": buscar_en_diccionario,
        "descripcion": "Busca una definición o clave dentro de las estructuras de datos pedagógicas.",
        "topico": "Estructuras de Datos"
    },
    "calcular_multiplicacion": {
        "funcion": ejecutar_multiplicacion,
        "descripcion": "Realiza la multiplicación de dos factores matemáticos.",
        "topico": "Operadores y Aritmética"
    },
    "obtener_sistema_fecha": {
        "funcion": obtener_fecha_completa,
        "descripcion": "Devuelve la fecha actual formateada para el aprendizaje del módulo datetime.",
        "topico": "Módulos y Librerías Estándar"
    }
}