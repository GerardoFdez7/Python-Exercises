#Gerardo Fernandez

#Importamos turtle y el modulo anterior
import figuras_geométricas
import turtle

#Declaracion de variables
w = turtle.Screen()
w.bgcolor("light blue")
t = turtle.Turtle()
t.speed(speed=0)

            #Dibujo
#Casa
t.penup()
t.goto(-50, -50)
t.pendown()
figuras_geométricas.dibujar_cuadrado(t, 'dark blue', 250)
#Puerta
t.penup()
t.goto(50, -240)
t.pendown()
figuras_geométricas.dibujar_cuadrado(t, 'orange', 60)
#Techo
t.penup()
t.goto(-50, -50)
t.pendown()
figuras_geométricas.dibujar_triangulo(t, 'pink', 250)
#Sol
t.penup()
t.goto(-200, 50)
t.pendown()
figuras_geométricas.dibujar_circulo(t, 'yellow', 50)
#Jardin
t.penup()
t.goto(-120, -300)
t.pendown()
figuras_geométricas.dibujar_triangulo(t, 'green', 70)
t.penup()
t.goto(-190, -300)
t.pendown()
figuras_geométricas.dibujar_triangulo(t, 'green', 70)
t.penup()
t.goto(-260, -300)
t.pendown()
figuras_geométricas.dibujar_triangulo(t, 'green', 70)
t.penup()
t.goto(-330, -300)
t.pendown()
figuras_geométricas.dibujar_triangulo(t, 'green', 70)
#Pelota
t.penup()
t.goto(250, -300)
t.pendown()
figuras_geométricas.dibujar_circulo(t, "red", 25)
#Arbol
    #Hojas
t.penup()
t.goto(225, -50)
t.pendown()
figuras_geométricas.dibujar_triangulo(t, 'green', 200)
    #Tronco
t.penup()
t.goto(300, -300)
t.pendown()
t.color('maroon')
t.begin_fill()
t.forward(50)
t.left(90)
t.forward(250)
t.left(90)
t.forward(50)
t.left(90)
t.forward(250)
t.end_fill()
t.penup()
t.goto(1000, -3000)
t.pendown()

#cerrar ventana
w.exitonclick()