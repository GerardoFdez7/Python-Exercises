# Gerardo Fernández

import turtle
import random
from math import sqrt
turtle.speed(0)

# dibuja una linea recta
def linea(longitud, x, y, color):

    # establece la posición de la tortuga
    turtle.pu()
    turtle.setpos(x, y)
    turtle.pd()

    # rellena la figura de un color
    turtle.color('black', color)
    turtle.begin_fill()

    # linea
    turtle.fd(longitud)

# dibuja un triángulo equilátero
def triangulo(longitud, x, y, color):

    # establece la posición de la tortuga
    turtle.pu()
    turtle.setpos(x, y)
    turtle.pd()

    # rellena la figura de un color
    turtle.color('black', color)
    turtle.begin_fill()

    # dibuja el triángulo con lados y ángulos iguales
    for i in range(0,3):
        turtle.fd(longitud)
        turtle.lt(120)
    turtle.end_fill()

# dibuja un triángulo rectángulo
def triangulo_rectangulo(longitud, x, y, color):

    # establece la posición de la tortuga
    turtle.pu()
    turtle.setpos(x, y)
    turtle.pd()

    # rellena la figura
    turtle.color('black', color)
    turtle.begin_fill()

    # dibuja el triángulo con un ángulo de 90 grados
    turtle.fd(longitud)
    turtle.lt(90)
    turtle.fd(longitud)
    turtle.lt(135)
    turtle.fd(longitud * sqrt(2))
    turtle.end_fill()

    # resetea la dirección hacia la que observa la tortuga
    turtle.seth(0)

# dibuja un cuadrado
def cuadrado(longitud, x, y, color):

    # establece la posición de la tortuga
    turtle.pu()
    turtle.setpos(x, y)
    turtle.pd()

    # rellena la figura
    turtle.color('black', color)
    turtle.begin_fill()

    # dibuja el cuadrado
    for i in range(0, 4):
        turtle.fd(longitud)
        turtle.lt(90)
    turtle.end_fill()

def rectangulo(base, altura, x, y, color):

    # establece la posición de la tortuga
    turtle.pu()
    turtle.setpos(x, y)
    turtle.pd()

    # rellena la figura
    turtle.color('black', color)
    turtle.begin_fill()

    # dibuja el rectángulo
    turtle.fd(base)
    turtle.lt(90)
    turtle.fd(altura)
    turtle.lt(90)
    turtle.fd(base)
    turtle.lt(90)
    turtle.fd(altura)

    turtle.end_fill()

# dibuja un paralelogramo con ángulos internos deseados
def paralelogramo(longitud, angulo, x, y, color):

    # establece la posición de la tortuga
    turtle.pu()
    turtle.setpos(x, y)
    turtle.pd()

    # rellena la figura
    turtle.color('black', color)
    turtle.begin_fill()

    # dibuja el paralelogramo con el ángulo introducido
    for i in range(0, 2):
        turtle.fd(longitud)
        turtle.lt(angulo)
        turtle.fd(longitud)
        turtle.lt(180 - angulo)
    turtle.end_fill()

# dibuja un hexagono
def hexagono(longitud, x, y, color):
     # establece la posición de la tortuga
    turtle.pu()
    turtle.setpos(x, y)
    turtle.pd()

    # rellena la figura
    turtle.color('black', color)
    turtle.begin_fill()

    for i in range(6):
        turtle.forward(longitud)
        turtle.left(300)
    turtle.end_fill()

# dibuja un trapecio
def trapecio(longitud, x, y, color):
     # establece la posición de la tortuga
    turtle.pu()
    turtle.setpos(x, y)
    turtle.pd()

    # rellena la figura
    turtle.color('black', color)
    turtle.begin_fill()

    turtle.fd(longitud)
    turtle.lt(120)
    turtle.fd(longitud / 2)
    turtle.lt(60)
    turtle.fd(longitud / 2)
    turtle.lt(60)
    turtle.fd(longitud / 2)
    turtle.lt(60)
    turtle.end_fill()

# dibuja un circulo
def circulo(angulo, x, y, color):
    # establece la posición de la tortuga
    turtle.pu()
    turtle.setpos(x, y)
    turtle.pd()

    # rellena la figura
    turtle.color('black', color)
    turtle.begin_fill()

    turtle.circle(angulo)
    turtle.end_fill()

# dibuja un roseton


# dibuja el perro de un color variable
def perro(col):
    ventana = turtle.Screen()
    turtle.TurtleScreen._RUNNING = True

    # define las propiedades de la tortuga
    turtle.speed(10)
    turtle.pensize(2)
    turtle.shape('turtle')

    # dibuja la pata trasera y el cuerpo
    triangulo_rectangulo(100, -200, -250, col)
    triangulo_rectangulo(200, -100, -150, col)
    turtle.seth(180)
    triangulo_rectangulo(200, 0, -50, col)

    # dibuja la cola y la pata delantera
    turtle.seth(90)
    triangulo_rectangulo(100, -200, -50, col)
    cuadrado(100, 0, -250, col)

    # dibuja la cabeza
    turtle.lt(135)
    triangulo_rectangulo(100, 241.4, 0, 'black')
    turtle.lt(45)
    paralelogramo(100, 45, 100, 0, col)

    ventana.exitonclick()

# dibuja el gato de un color variable
def gato(col):
    ventana = turtle.Screen()
    turtle.TurtleScreen._RUNNING = True

    # define las propiedades de la tortuga
    turtle.speed(10)
    turtle.pensize(2)
    turtle.shape('turtle')

    # dibuja la cola y el cuerpo
    paralelogramo(100, -45, -250, -150, col)
    triangulo_rectangulo(100, -80.5, -220.5, col)
    turtle.lt(45)
    triangulo_rectangulo(141.4, -80.5, -220.5, col)
    turtle.lt(225)
    triangulo_rectangulo(141.4, 19.5, 79.5, col)

    # dibuja la cabeza y orejas
    turtle.lt(45)
    cuadrado(75, -0.5, 59.5, col)
    triangulo_rectangulo(75, -53.5, 112.5, 'pink')
    turtle.lt(225)
    triangulo_rectangulo(75, 52.5, 218.6, 'pink')

    ventana.exitonclick()

# Dibuja el logo de spotify
def inicio():
    circulo(100, 0, 0, 'lime green')
    turtle.penup()
    turtle.goto (40,50)
    turtle.pendown()
    turtle.left(150)
    turtle.forward (0)
    turtle.pensize (15)
    turtle.pencolor('black')
    turtle.circle (80,60)
    turtle.penup()
    turtle.goto(50,85)
    turtle.pendown()
    turtle.pensize(17)
    turtle.right(60)
    turtle.forward(0)
    turtle.circle(100,60)
    turtle.penup()
    turtle.goto(60,120)
    turtle.pendown()
    turtle.pensize(20)
    turtle.right(60)
    turtle.forward(0)
    turtle.circle(120,60)
    turtle.penup()

    # Dibuja las letras
    turtle.color('white')
    turtle.goto(0, -60)
    turtle.write('Spotify UVG', align='center', font=('Arial', 40, 'bold'))
    turtle.goto(0, -100)
    turtle.write('Agrega una canción', align='center', font=('Arial', 16, 'normal'))

# Aplica un color aleatorio
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)