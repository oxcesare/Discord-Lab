import discord
import os
import re
from dotenv import load_dotenv
# importar la classe tareas_agente.py
from src.practica04.tareas_agente import agregar_tarea, listar_tareas, eliminar_tarea
from src.practica01.gestor_comandos import buscar_en_diccionario, validar_variable
from src.practica02.procesador_comandos import mostrar_ayuda

tareas = []  # Nuestra "base de datos" en memoria (lista)


def mostrar_bienvenida():
    """Retorna la lista de comandos disponibles."""
    return (
        "📜 Agente tutor Python (Programacion Estructurada):\n"
        "📜 Primeros pasos Agente Discord UX:\n"  
        "📜 Escriba !add <tarea> para agregar una tarea:\n"        
        "📜 Escriba !list para listar las tareas:\n"
        "📜 Escriba !delete <tarea> para eliminar una tarea:\n"
        "📜 Escriba !buscar <termino> para buscar un término en el diccionario:\n"
        "📜 Escriba !ayuda para mostrar esta lista de comandos:\n"
        "📜 Escriba !exit para salir del Agente:"
    )

def main(entrada):
    
        PREFIJO = "!"
        

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

        elif comando == "add":            
            return agregar_tarea(tareas, argumento)
        
        elif comando == "list":
            return listar_tareas(tareas)
        
        elif comando == "help" or comando == "ayuda":
            return mostrar_bienvenida()
        
        elif comando == "delete":
            return eliminar_tarea(tareas, argumento)

        elif comando == "buscar":
            return buscar_en_diccionario(argumento)

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