import discord
import os
import re
from dotenv import load_dotenv
import datetime
# importar la classe tareas_agente.py
from src.practica02.procesador_comandos import obtener_saludo, procesar_comando_recordar, calcular_uptime

tareas = []  # Nuestra "base de datos" en memoria (lista)

def mostrar_bienvenida():
    """Retorna la lista de comandos disponibles."""
    return (
        "📜 Bot de procesador de comandos (Programacion Estructurada):\n"
        "📜 Escriba !saludo para recibir un saludo del bot:\n"        
        "📜 Escriba !recordar <mensaje> para que el bot recuerde algo:\n"        
        "📜 Escriba !tiempo para conocer el tiempo de actividad del bot:\n"        
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

        elif comando == "ayuda":
            return mostrar_bienvenida()
            
        elif comando == "saludo":
            return obtener_saludo(NOMBRE_BOT)
            
        elif comando == "recordar":
            respuesta = procesar_comando_recordar(argumento)
            return respuesta
            
        elif comando == "tiempo":
            return calcular_uptime(hora_inicio_programa)
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