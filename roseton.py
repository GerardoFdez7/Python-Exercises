# Gerardo Fernandez
# Sebastian Tunchez

import turtle
import dibujos_turtle

#Declaracion de variables
w = turtle.Screen()
w.bgcolor('black')
turtle.hideturtle()

# Interfaz
print("### BIENVENIDO ###")
petalos = int(input("Elija la cantidad de petalos que desea hacer: "))
longitud = int(input("Elija la longitud que desea en los petalos: "))
color = input("Ingrese el color del cual desea que sea su roseton: (en ingles) ")
turtle.pencolor(color)

# Dibujar los pétalos
for i in range(longitud):
    turtle.circle(petalos, 180)
    turtle.left(120)
    turtle.circle(petalos)
    turtle.right(110)

w.exitonclick()