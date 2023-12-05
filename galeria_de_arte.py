#Gerardo Fernandez

import turtle

#abrir ventana para mostrar la tortuga
window = turtle.Screen()
window.bgcolor("light blue")

#Declaracion de la tortuga y sus variables
tortuga = turtle.Turtle()
tortuga.shape('turtle')
tortuga.speed(speed=0.5)
recorrido = 100
contar_lados = 0
seguir_en_menu = True

while seguir_en_menu == True:
     print("GALERIA DE ARTE")
     opcion = input("""
    Seleccione que opcion desea dibujar.

        1. Figuras geometricas
        2. Cara de robot
        3. Espiral colorido
        4. Ninguna, salir del programa
    """)

     if opcion.isdigit() == True:
        opcion_entero = int(opcion)
        if opcion_entero >= 1 and opcion_entero <=4:
     
#Figuras geometricas
            if opcion_entero == 1:
            #Cuadrado
                while contar_lados < 4:
                    tortuga.forward(recorrido)
                    tortuga.left(90)
                    contar_lados = contar_lados +1

            #Circulo
                tortuga.penup()
                tortuga.goto(200, 0)
                tortuga.pendown()
                r = 50
                tortuga.circle(r)

            #Triangulo
                tortuga.penup()
                tortuga.goto(-150, 0)
                tortuga.pendown()
                for i in range (3):
                    tortuga.forward(recorrido)
                    tortuga.right(240)

            #Rombo
                tortuga.penup()
                tortuga.goto(-250, 0)
                tortuga.pendown()
                tortuga.left(110)
                tortuga.forward(75)
                tortuga.left(-70)
                tortuga.forward(75)
                tortuga.right(110)
                tortuga.forward(75)
                tortuga.right(70)
                tortuga.forward(75)

                tortuga.penup()
                tortuga.goto(-550, 0)
                tortuga.pendown()
#Robot
            elif opcion_entero == 2:
     #Cara           
                tortuga.penup()
                tortuga.goto(-150, -150)
                tortuga.pendown()
            
                tortuga.forward(400)
                tortuga.left(90)
                tortuga.forward(250)
                tortuga.left(90)
                tortuga.forward(400)
                tortuga.left(90)
                tortuga.forward(250)
                tortuga.left(90)
    #Boca
                tortuga.penup()
                tortuga.goto(-100, -75)
                tortuga.pendown()

                tortuga.right(90)
                tortuga.forward(40)
                tortuga.left(90)
                tortuga.forward(300)
                tortuga.left(90)
                tortuga.forward(40)

    #Nariz
                tortuga.penup()
                tortuga.goto(30, -90)
                tortuga.pendown()

                tortuga.right(90)
                tortuga.forward(40)
                tortuga.right(250)
                tortuga.forward(70)
                tortuga.right(220)
                tortuga.forward(70)
                tortuga.left(105    )
                tortuga.forward(9)

    #Ojos       #Izq
                tortuga.penup()
                tortuga.goto(-25, -15)
                tortuga.pendown()

                r = 45
                tortuga.circle(r)
                #Der
                tortuga.penup()
                tortuga.goto(105, -15)
                tortuga.pendown()

                r = 45
                tortuga.circle(r)

    #Antena
                tortuga.penup()
                tortuga.goto(45, 100)
                tortuga.pendown()

                tortuga.left(95)
                tortuga.forward(58)
                tortuga.penup()

                tortuga.goto(85, 200)
                tortuga.pendown()
                r = 45
                tortuga.circle(r)

                tortuga.penup()
                tortuga.goto(400, 400)
                tortuga.pendown()

                
#Espiral Colorido

            elif opcion_entero == 3: 
                lista_colores = ['blue', 'orange','green', 'purple', 'red', 'yellow' ]
                t = tortuga.pen()
                window.bgcolor('black')
                for i in range (360):
                    tortuga.pencolor(lista_colores[i % 6])
                    tortuga.width(i / 100 + 1)
                    tortuga.forward(i)
                    tortuga.left(59)

#Salir del menu         
            elif opcion_entero == 4:
                print("Gracias por ver nuestra galeria de arte!")
                seguir_en_menu = False