# Discord-Lab

## Descripcion general

Discord-Lab es un bot de Discord orientado a la ensenanza de Python. El proyecto implementa un agente tutor que recibe mensajes en lenguaje natural, identifica la intencion del usuario y responde con explicaciones pedagogicas sobre conceptos basicos del lenguaje.

El objetivo principal es que un estudiante pueda escribir consultas simples como `hola`, `tipos de datos`, `identificadores` u `operadores logicos` y recibir una respuesta clara, corta y util para aprender Python sin depender de comandos tecnicos con prefijos.

## Proposito del proyecto

Este proyecto fue disenado como un tutor introductorio de Python integrado con Discord. Su funcion es ayudar a un usuario a comprender reglas, sintaxis y conceptos fundamentales del lenguaje, manteniendo una interaccion natural y sencilla.

El agente puede:

- saludar al usuario y mostrar un mensaje de bienvenida
- identificar el tema que el usuario quiere consultar
- responder con informacion educativa previamente definida
- registrar un pequeno historial de interacciones recientes

## Temas soportados

Actualmente el agente puede explicar estos temas:

- palabras reservadas
- identificadores
- tipos de datos
- tipos de datos simples
- tipos de datos compuestos
- variables y constantes
- operadores aritmeticos
- operadores logicos
- historial de interacciones

## Funcionamiento general

El flujo principal del proyecto es el siguiente:

1. El usuario envia un mensaje en Discord.
2. El archivo principal del bot recibe el mensaje.
3. El agente registra la interaccion en memoria.
4. Un clasificador de intenciones analiza el texto del usuario.
5. La intencion detectada se busca en un toolkit centralizado.
6. Se ejecuta la funcion asociada al tema solicitado.
7. El bot responde en el canal con la explicacion correspondiente.

Este enfoque evita el uso de comandos estrictos como `!sumar` o `!definir`, y permite una conversacion mas natural basada en temas.

## Arquitectura del proyecto

### Archivo principal

- `src/agente_discord.py`

Contiene la integracion con Discord, la bienvenida, el flujo principal del agente y la conexion entre el mensaje del usuario, el clasificador de intenciones y el toolkit.

### Clasificador de intenciones

- `src/tools/clasificador_intenciones.py`

Se encarga de analizar el texto del usuario y determinar que tema desea consultar. Por ejemplo, reconoce entradas como `palabras reservadas`, `tipos de datos`, `variables`, `constantes` u `operadores logicos`.

### Toolkit del agente

- `src/tools/toolkit.py`

Centraliza el registro de capacidades del agente. Cada intencion se mapea a una funcion concreta, junto con una descripcion breve de lo que hace.

### Contenido pedagogico

- `src/sintaxis_basica/basicos.py`

Contiene las funciones que devuelven las explicaciones educativas de cada tema. Las respuestas estan pensadas para ser directas, didacticas y acompanadas por ejemplos cortos.

### Historial de interacciones

- `src/practica03/agente_logica.py`

Se utiliza para registrar en memoria las ultimas interacciones del usuario y mostrarlas cuando el usuario escribe `historial`.

## Caracteristicas principales

- Interaccion natural sin prefijos obligatorios.
- Respuestas enfocadas en teoria basica de Python.
- Clasificacion de intenciones basada en palabras clave.
- Toolkit centralizado para despachar funcionalidades.
- Historial corto de mensajes recientes.
- Contenido pedagogico modular y facil de ampliar.

## Requisitos

Para ejecutar el proyecto necesitas:

- Python 3
- una aplicacion de Discord con su token configurado
- las dependencias instaladas en el entorno virtual

Dependencias observadas en el proyecto:

- `discord.py`
- `python-dotenv`

## Configuracion

### 1. Crear o activar el entorno virtual

El proyecto ya incluye un entorno virtual en la carpeta `env/`. Si quieres usarlo en macOS o Linux:

```bash
source env/bin/activate
```

### 2. Configurar el token del bot

Crea un archivo `.env` en la raiz del proyecto con una variable como esta:

```env
DISCORD_TOKEN=tu_token_aqui
```

### 3. Verificar permisos del bot

El bot necesita el intent de lectura de contenido de mensajes (`message_content`) habilitado para poder analizar lo que el usuario escribe.

## Ejecucion

Desde la carpeta `src`, el bot puede ejecutarse con:

```bash
python -m agente_discord
```

Si el token esta configurado correctamente, el bot se conectara a Discord y quedara listo para responder mensajes.

## Ejemplos de uso

El usuario puede escribir mensajes como estos:

- `Hola`
- `inicio`
- `palabras reservadas`
- `identificadores`
- `tipos de datos`
- `tipos de datos compuestos`
- `variables`
- `constantes`
- `operadores aritmeticos`
- `operadores logicos`
- `historial`

Ejemplo esperado:

- Si el usuario escribe `Hola`, el bot responde con un saludo.
- Si el usuario escribe `tipos de datos`, el bot explica tipos simples y compuestos.
- Si el usuario escribe `historial`, el bot muestra las ultimas interacciones registradas.

## Alcance actual

En su estado actual, el proyecto esta especializado en definiciones y explicaciones teoricas de Python. No esta enfocado en resolver ejercicios complejos, ejecutar codigo del usuario ni mantener conversaciones abiertas sobre cualquier tema fuera de los conceptos definidos en el toolkit.

## Posibles mejoras futuras

- agregar mas temas de sintaxis y estructuras de control
- incluir ejemplos de codigo mas amplios por cada concepto
- incorporar quizzes o preguntas de practica
- registrar historial persistente en archivo o base de datos
- mejorar el clasificador para reconocer mas variaciones de lenguaje natural

## Estructura general del repositorio

```text
Discord/
├── README.md
├── env/
└── src/
	├── agente_discord.py
	├── practica03/
	│   └── agente_logica.py
	├── sintaxis_basica/
	│   └── basicos.py
	└── tools/
		├── clasificador_intenciones.py
		└── toolkit.py
```


## Resumen

Discord-Lab es un tutor basico de Python para Discord. Su arquitectura separa claramente la recepcion de mensajes, la clasificacion de intenciones, el registro de herramientas y el contenido pedagogico. Esto hace que el proyecto sea sencillo de entender, mantener y ampliar con nuevos temas educativos.
