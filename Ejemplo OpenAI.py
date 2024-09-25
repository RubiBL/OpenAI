import openai

# Configura tu clave API
openai.api_key = "tu_clave_api_aqui"

# Función que interactúa con OpenAI
def asistente_virtual(pregunta):
    response = openai.chat.completions.create(
       model="gpt-4o-mini",  # El motor de IA que deseas utilizar
       messages = [
           {"role": "system", "content" : pregunta},
           ]
      )
    return response.choices[0].message.content

# Simula una interacción
print("Hola, soy tu asistente virtual. ¿En qué puedo ayudarte hoy?")
while True:
    entrada = input("Tú: ")
    if entrada.lower() in ["salir", "adiós", "terminar"]:
        print("Asistente: ¡Hasta luego!")
        break
    respuesta = asistente_virtual(entrada)
    print(f"Asistente: {respuesta}")
