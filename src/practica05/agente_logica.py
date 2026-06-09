import discord
import os
import re
from dotenv import load_dotenv
import datetime
# importar la classe tareas_agente.py
from src.practica03.agente_logica import ejecutar_suma, buscar_en_diccionario,validar_variable,ejecutar_multiplicacion,obtener_fecha_completa

historial_comandos = []  # Nuestra "base de datos" en memoria (lista)

def mostrar_bienvenida():
    """Retorna la lista de comandos disponibles."""
    return (
        "📜 Bot de procesador de comandos (Programacion Estructurada):\n"
        "📜 Escriba !saludo para recibir un saludo del bot:\n"        
        "📜 Escriba !sumar <n1> <n2> para que el bot realice una suma:\n"        
        "📜 Escriba !multiplicar <n1> <n2> para que el bot realice una multiplicación:\n" \
        "📜 Escriba !fecha para conocer la fecha completa:\n"
        "📜 Escriba !definir <palabra> para buscar su definición:\n"
        
        "📜 Escriba !exit para salir del Agente:"
    )

def main(entrada):
    
        PREFIJO = "!"
        NOMBRE_BOT = "PyBot_V2"
        hora_inicio_programa = datetime.datetime.now()
        

        if not entrada.startswith(PREFIJO):
            if entrada: print("Recuerda usar '!' para comandos.")
            
        # Procesamiento de la entrada
        cuerpo = entrada[len(PREFIJO):].split(maxsplit=1)
        comando = cuerpo[0].lower()
        argumento = cuerpo[1] if len(cuerpo) > 1 else ""
        
        # Selección de acción (Estructura de control)
        if comando == "exit":
            print("Saliendo del gestor...")
            return "Saliendo del gestor..."

         # Registrar en el historial (Máximo 5 elementos)
        if len(historial_comandos) >= 5:
            historial_comandos.pop(0)
        historial_comandos.append(comando)

        # --- UNIDAD 3: ESTRUCTURAS DE SELECCIÓN ---
        if comando == "!definir":
            return buscar_en_diccionario(argumento)
        
        elif comando == "!validar":
            return validar_variable(argumento)
            
        elif comando == "!hora":
            ahora = datetime.datetime.now().strftime("%H:%M:%S")
            return f" Hora actual: {ahora}"
        
        elif comando == "!historial":
            # UNIDAD 3.2: Estructuras de repetición
            res = "Últimos comandos:\n"
            for i, cmd in enumerate(historial_comandos, 1):
                res += f"{i}. {cmd}\n"
            return res

        elif comando == "!sumar":
            # UNIDAD 4.3: Parámetros de entrada
            return ejecutar_suma(argumento)
        
        elif comando == "!fecha":
            return obtener_fecha_completa()
        
        elif comando == "!multiplicar":
            return ejecutar_multiplicacion(argumento)
            
        elif comando == "!ayuda":
            return (" **Comandos V2:**\n"
                    "!definir, !validar, !hora, !historial, !sumar <n1> <n2>, !multiplicar <n1> <n2>, !fecha")
        else:
            print(f" Error: Comando '!{comando}' no reconocido.")
            return f" Error: Comando '!{comando}' no reconocido."
        
        print("-" * 20)


# --- CONFIGURACIÓN DE DISCORD ---

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Definir los "intents" (permisos) necesarios
intents = discord.Intents.default()
intents.message_content = True  # Necesario para leer el contenido de los mensajes

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Sincronizado como {client.user} (ID: {client.user.id})')
    print('------')

@client.event
async def on_message(message):
    # Evitar que el bot se responda a sí mismo
    if message.author == client.user:
        return
    
    # Invocar la función de bienvenida 
    if message.content.lower() == "!inicio":
        bienvenida = mostrar_bienvenida()
        main(message.content)        
        await message.channel.send(bienvenida)
        return
    
    #invocar la funcion main para procesar los comandos
        
    # 3. Procesamiento: Pasamos el contenido del mensaje a nuestra lógica
    print(f"Mensaje recibido de {message.author}: {message.content}")

      # Solo procesamos si el mensaje empieza con un prefijo (opcional, pero recomendado)
    if message.content.startswith('!'):
        resultado = main(message.content)

        print(f"Resultado del procesamiento: {resultado}")
        
        # 4. Respuesta: El bot escribe el resultado en el mismo canal
        await message.channel.send(f" **Bot Procesador:** {resultado}")
    
# Ejecutar el bot
if __name__ == "__main__":
    if TOKEN:
        client.run(TOKEN)
    else:
        print("ERROR: No se encontró el TOKEN en el archivo .env")