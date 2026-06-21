def clasificar_intencion(texto_usuario: str) -> str:
    """
    Este es el 'motor de pensamiento' del agente.
    Analiza el lenguaje natural del alumno y determina la acción (intención).
    """
    texto = texto_usuario.lower()

    if texto in {"hola", "buenas", "buenos dias", "buen día", "buenas tardes", "buenas noches"}:
        return "bienvenida"
    elif texto in {"inicio", "menu", "menú", "ayuda"}:
        return "menu"
    elif "historial" in texto or "comandos" in texto or "he puesto" in texto:
        return "historial"
    elif "palabras" in texto or "keywords" in texto or "reservadas" in texto:
        return "mostrar_palabras_reservadas"
    elif "identificadores" in texto or "identificador" in texto or "nombres de variables" in texto:
        return "mostrar_identificadores"
    elif "tipos de datos compuestos" in texto or "data structures" in texto or "compuestos" in texto:
        return "mostrar_tipos_datos_compuestos"
    elif "tipos de datos simples" in texto or "simples" in texto:
        return "mostrar_tipos_datos_simples"
    elif "tipos de datos" in texto or "data types" in texto:
        return "mostrar_tipos_datos"
    elif "tipos de variables" in texto or "variables y constantes" in texto or "variables" in texto or "constantes" in texto:
        return "mostrar_variables_constantes"
    elif "operadores aritméticos" in texto or "operadores aritmeticos" in texto or "aritméticos" in texto or "aritmeticos" in texto:
        return "mostrar_operadores_aritmeticos"
    elif "operadores lógicos" in texto or "operadores logicos" in texto or "lógicos" in texto or "logicos" in texto:
        return "mostrar_operadores_logicos"
    return "desconocido"