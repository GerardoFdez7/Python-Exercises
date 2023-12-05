# Gerardo Fernandez
# Luis Palacios

import random
import turtle
import dibujos_turtle

# Configuración de la ventana de Turtle
turtle.Screen()
turtle.hideturtle()

# Declaración de variables
palabras = ['programacion', 'computadora', 'teclado', 'raton', 'monitor']
palabra = random.choice(palabras)
max_intentos = 4
max_intentos_robot = 4
adivinadas = ['_' for _ in palabra]
incorrectas = []
incorrectas_robot = []

# Registraremos si cada parte del muneco ha sido dibujada
partes_dibujadas = [False, False, False, False, False, False, False]

# Funciones
def dibujar_muneco(intentos):
    if intentos >= 1 and not partes_dibujadas[0]:   # Palo
        turtle.lt(45)
        dibujos_turtle.linea(100, -150, -240, 'black')
        turtle.rt(90)
        dibujos_turtle.linea(100, -80, -170, 'black' )
        turtle.lt(135)
        dibujos_turtle.linea(350, -80, -170, 'black')
        turtle.rt(90)
        dibujos_turtle.linea(200, -80, 180, 'black')
        partes_dibujadas[0] = True
    if intentos >= 2 and not partes_dibujadas[1]:  # Cabeza
        dibujos_turtle.circulo(50, 120, 80, 'white')
        partes_dibujadas[1] = True
    if intentos >= 3 and not partes_dibujadas[2]:  # Torzo
        turtle.rt(90)
        dibujos_turtle.linea(180, 120, 80, 'black' )
        partes_dibujadas[2] = True
    if intentos >= 4 and not partes_dibujadas[3]:  # Pierna
        turtle.rt(45)
        dibujos_turtle.linea(100, 120, -100, 'black')
        partes_dibujadas[3] = True
    if intentos >= 5 and not partes_dibujadas[4]: # Pierna
        turtle.lt(90)
        dibujos_turtle.linea(100, 120, -100, 'black')
        partes_dibujadas[4] = True
    if intentos >= 6 and not partes_dibujadas[5]: # Brazo
        turtle.lt(90)
        dibujos_turtle.linea(100, 120, -25, 'black' )
        partes_dibujadas[5] = True
    if intentos >= 7 and not partes_dibujadas[6]: # Brazo
        turtle.rt(-90)
        dibujos_turtle.linea(100, 120, -25, 'black' )

def agente_autonomo(adivinadas, incorrectas_robot, palabras_posibles):
    letras_frecuentes = "aeioulnstr"
    for letra in letras_frecuentes:
        if letra not in adivinadas and letra not in incorrectas_robot:
            for palabra in palabras_posibles:
                if letra in palabra:
                    return letra
    # Si no se encontró ninguna letra común, elegir una aleatoria
    letras_disponibles = set('abcdefghijklmnopqrstuvwxyz') - set(adivinadas) - set(incorrectas_robot)
    if letras_disponibles:
        return random.choice(list(letras_disponibles))
    else:
        return ''
    
# Bucle principal del juego
print("### BIENVENIDO ###")
while True:
    opcion = input("¿Qué desea hacer?\n1. Jugar\n2. Salir\n")
    if opcion == '1':
        intentos = 0
        acertadas = 0
        adivinadas = ['_' for _ in palabra]
        incorrectas = []
        palabras_posibles = palabras[:]
        while intentos < max_intentos and max_intentos_robot and acertadas < len(palabra):

            # Turno del usuario
            letra = input(f'Adivina una letra de la palabra: {" ".join(adivinadas)}\n')
            if letra in palabra:
                for i, letra_palabra in enumerate(palabra):
                    if letra_palabra == letra:
                        adivinadas[i] = letra
                acertadas += 1
            else:
                incorrectas.append(letra)
                intentos += 1
                dibujar_muneco(intentos)
                print(f'Tus letras incorrectas: {", ".join(incorrectas)}')

            # Turno del agente
            if acertadas < len(palabra):
                letra = agente_autonomo(adivinadas, incorrectas_robot, palabras_posibles)
                if letra:
                    print(f'El agente autonomo eligio la letra "{letra}"')
                    if letra in palabra:
                        for i, letra_palabra in enumerate(palabra):
                            if letra_palabra == letra:
                                adivinadas[i] = letra
                        acertadas += 1
                    else:
                        incorrectas_robot.append(letra)
                        intentos += 1
                        dibujar_muneco(intentos)
                        print(f'Letras incorrectas del agente autonomo: {", ".join(incorrectas_robot)}')
                        
                    # Actualizar la lista de palabras posibles
                    palabras_posibles = [p for p in palabras_posibles if all(l in adivinadas or l == '_' for l in p)]

        if acertadas == len(palabra):
            print(f'¡Ganaste! La palabra era "{palabra}".')
            break
        else:
            print(f'¡Perdiste! La palabra era "{palabra}".')
            break
    elif opcion == '2':
        print("¡Hasta luego!")
        break
    else:
        print("Seleccione una opción válida.")