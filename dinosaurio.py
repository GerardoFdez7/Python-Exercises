# Gerardo Fernandez
# Sebastian Tunchez

import turtle
import dibujos_turtle

#Declaracion de variables
w = turtle.Screen()
w.bgcolor("light blue")

    #Dibujo 
    
# Patas
dibujos_turtle.cuadrado(75, 48, -150, 'purple')
dibujos_turtle.cuadrado(75, -100, -150, 'purple')

# Tronco
dibujos_turtle.hexagono(72, 49, 49, 'green')
dibujos_turtle.hexagono(72, -98, 49, 'green')

dibujos_turtle.triangulo(75, -25, -75, 'saddlebrown')
turtle.seth(180)
dibujos_turtle.triangulo(75, 49, 50, 'saddlebrown')
dibujos_turtle.triangulo(75, 195, 50, 'saddlebrown')
dibujos_turtle.triangulo(73, -171, 49, 'limegreen')

turtle.seth(0)
dibujos_turtle.triangulo(75, -25, 50, 'red')
dibujos_turtle.triangulo(75, -99, 50, 'red')
dibujos_turtle.triangulo(75, 48, 50, 'red')
dibujos_turtle.triangulo(75, 122, 50, 'red')

dibujos_turtle.paralelogramo(73, 60, -209, -14, 'limegreen')

# Cabeza
dibujos_turtle.trapecio(150, 159, -14, 'lime')
dibujos_turtle.circulo(10, 225, 15, 'black')
dibujos_turtle.circulo(3, 231, 19, 'white')

# Colmillos 
turtle.seth(180)
dibujos_turtle.triangulo(75, 233, -14, 'white')
dibujos_turtle.triangulo(75, 307, -14, 'white')

w.exitonclick()