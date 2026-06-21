import discord
import os
from dotenv import load_dotenv

from practica03.agente_logica import (
    registrar_comando,
)

# IMPORTAMOS ÚNICAMENTE LA CAJA DE HERRAMIENTAS CENTRALIZADA
from tools.toolkit import TOOLKIT

from tools.clasificador_intenciones import clasificar_intencion

def mostrar_bienvenida():
    """Retorna la lista de comandos disponibles dinámicamente."""
    return (
        "📜 **Bot de Procesador de Comandos (Programación Estructurada V2):**\n"
        "Soy un agente tutor de Python y mi propósito es enseñarte el lenguaje de forma guiada.\n"
        "Puedo explicarte estos temas:\n"
        "- palabras reservadas\n"
        "- identificadores\n"
        "- tipos de datos\n"
        "- tipos de datos simples\n"
        "- tipos de datos compuestos\n"
        "- variables y constantes\n"
        "- operadores aritmeticos\n"
        "- operadores logicos\n\n"
        "Solo escribe el tema que quieras consultar, por ejemplo: `tipos de datos`, `variables`, `operadores logicos` o `palabras reservadas`.\n"
        "También puedo mostrar el historial de tus últimas interacciones si escribes `historial`.\n\n"
    )

def main(entrada_usuario: str):
    """
    Bucle de decisión del Agente: Percibe -> Piensa -> Actúa
    """
    # 1. PERCEPCIÓN: Limpiar la entrada
    texto_limpio = entrada_usuario.strip()
    if not texto_limpio:
        return "[Agente]: Hola, soy tu tutor de Python. ¿En qué tema o duda te puedo ayudar hoy?"

    registrar_comando(texto_limpio)

    # 2. PENSAMIENTO: El agente analiza el texto para buscar la intención
    intencion = clasificar_intencion(texto_limpio)
    
    print(f"[Agente - Pensamiento]: El usuario dijo: '{texto_limpio}'. Clasificado como: '{intencion}'")

    if intencion == "bienvenida":
        return "[Agente]: Hola, soy tu tutor de Python. ¿En qué tema o duda te puedo ayudar hoy?"
    if intencion == "menu":
        return mostrar_bienvenida()

    # 3. ACCIÓN: Buscar en la caja de herramientas (TOOLKIT) de forma autónoma
    if intencion in TOOLKIT:
        herramienta = TOOLKIT[intencion]["funcion"]
        resultado_herramienta = herramienta()
            
        return f"[Tutor Python]: Entiendo que tienes dudas sobre *{TOOLKIT[intencion]['descripcion']}*.\nAquí tienes la respuesta:\n\n{resultado_herramienta}"
    
    else:
        return "[Tutor Python]: Vaya, aún no he aprendido a procesar esa solicitud. " \
                "Prueba preguntándome sobre palabras reservadas, tipos de datos, variables u operadores."


# --- CONFIGURACIÓN E INTERFAZ DE DISCORD (PERCEPCIÓN) ---
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Sincronizado como {client.user} (ID: {client.user.id})')
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    print(f"Mensaje recibido de {message.author}: {message.content}")

    resultado = main(message.content)
    await message.channel.send(f"{resultado}")
    
if __name__ == "__main__":
    if TOKEN:
        client.run(TOKEN)
    else:
        print("ERROR: No se encontró el TOKEN en el archivo .env")