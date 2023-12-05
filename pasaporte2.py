# Gerardo Fernandez

import turtle
import dibujos_turtle

#Declaracion de variables
w = turtle.Screen()
w.bgcolor("light blue")

    # Dibujo

#Cabeza
turtle.lt(45)
dibujos_turtle.cuadrado(75, 140, -90, 'green')
dibujos_turtle.triangulo_rectangulo(75, 87.5, -38.5, 'red')
turtle.lt(225)
dibujos_turtle.triangulo_rectangulo(75, 195.5, 68, 'purple')

# Tronco bajo
turtle.seth(90)
dibujos_turtle.triangulo_rectangulo(150, 88, -180, 'orange')

# Tronco medio
turtle.seth(135)
dibujos_turtle.triangulo_rectangulo(150, 45, -30, 'blue')

# Tronco alto
turtle.seth(315)
dibujos_turtle.triangulo_rectangulo(100, -202, 76, 'pink')

# Cola
turtle.seth(45)
dibujos_turtle.paralelogramo(100, 40, -69, 69, 'yellow')

w.exitonclick() 