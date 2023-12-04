#Gerardo Fernandez
#Gabriel Soto

#importar tortuga
import turtle

#abrir ventana para mostrar la tortuga
window = turtle.Screen()

#Declaracion de la tortuga y su forma
pepe = turtle.Turtle()
pepe.shape("turtle")

#Programa
contar_lados = 0
recorrido = 10
while contar_lados < 14 :
   pepe.forward(recorrido)
   pepe.right(90)
   recorrido = recorrido + 15
   contar_lados = contar_lados + 1

#cerrar ventana
window.exitonclick()

