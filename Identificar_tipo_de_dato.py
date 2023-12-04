#Gerardo Fernandez
#Gabriel Soto

#Importa la opcion para poder hacer aleatorias las preguntas
import random

#Mensaje de bienvenida
print("Bienvenido! solo te quiero hacer un par de preguntas rapidas para que me contestes de manera correcta :D ")

#Preguntas y respuestas
preguntas = {
    "True": "Booleano",
    "3.1416": "Flotante",
    "42": "Entero",
    "Hola Mundo": "Cadena de texto"
}

#Declaracion de variables de respuestas respondidas correctamente
respondidas = []
respuestas_correctas = 0

#Mientras las respuestas correctas sean menos que las preguntas seguir
while respuestas_correctas < len(preguntas):
    almacen = random.choice(list(preguntas.keys()))
    while almacen in respondidas: #almacenamos en respondidas para que no se repitan
        almacen = random.choice(list(preguntas.keys()))
    respuestas = input(f"Que tipo de dato es {almacen}? ")
    
#Si es correcta pasar a la siguiente sino volver a intentarlo
    if respuestas == preguntas[almacen]: 
        print("Respuesta correcta! continuemos ")
        respuestas_correctas += 1 
        respondidas.append(almacen)
    else: 
        print("Respuesta incorrecta, vuelve a intentarlo")
        break
    
#Ya has respondido todas las preguntas correctamente puedes ir a Casa :D
    if respuestas_correctas == len(preguntas):
        print("Ya has respondido todas las preguntas, muchisimas gracias! ")
        break




    