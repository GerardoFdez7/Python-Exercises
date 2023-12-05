# Gerardo Fernandez
# Este programa es un mini Spotify o mas bien un organizador de canciones en el cual podras registrar tu canciones favoritas
# y nosotros las organizaremos para ti.

# Importar módulos
import turtle
import dibujos_turtle

# Declarar variables, diccionarios y configurar la ventana
turtle.Screen()
turtle.bgcolor('black')
turtle.hideturtle()
seguir_en_programa = True
diccionarios = []
artistas = {}
vista = {}

        # Programa principal
dibujos_turtle.inicio() # Función que dibuja el menú de inicio

while seguir_en_programa == True:

    print("")
    print("### BIENVENIDO ###")
    print("¿Qué desea hacer?")
    print("1. Agregar nueva canción")
    print("2. Eliminar canción")
    print("3. Ver canciones guardadas")
    print("4. Ver artistas guardados ")
    print("5. Eliminar todas las canciones")
    print("6. Salir")
    print("")
    
    opcion = input("Seleccione una opción válida ")

    # Hacer que la opción elegida sea un dígito, y si no lo es, volver a ejecutar el menú
    if opcion.isdigit() == False:
        print("Seleccione un tipo de valor válido")
    else:
        opcion = int(opcion)

    # Opción 1: Agregar nueva canción.
    if opcion == 1:
        print("")
        add_song = {
            'Nombre de la canción' : input("Nombre de la canción: "),
            'Artista' : input("Artista: "),
            'Álbum' : input("Álbum: "),
            'Duración' : input("Duración: ")
        }
        print("Canción añadida exitosamente!")
        diccionarios.append(add_song)

        artista = add_song['Artista']
        if artista in artistas:
            artistas[artista] += 1
        else:
            artistas[artista] = 1

    # Opción 2: Eliminar canción.
    elif opcion == 2:
        eliminar_cancion = input("Ingrese el nombre de la canción que desea eliminar: ")
        for cancion in diccionarios:
            if cancion['Nombre de la canción'] == eliminar_cancion:
                diccionarios.remove(cancion)
                print(f"Canción '{eliminar_cancion}' eliminada exitosamente!")
                break
        else:
            print(f"Canción '{eliminar_cancion}' no encontrada.")

    # Opcion 3: Ver canciones guardadas
    elif opcion == 3:

        turtle.clear()
        turtle.color('white')
        turtle.penup()
        y = 250

        # Ordenar alfabeticamente
        artistas_ordenados = sorted(diccionarios, key=lambda x: x['Artista'])

        # Dibujar canciones guardadas
        for pantalla in artistas_ordenados:
            texto = f"{pantalla['Artista']} - {pantalla['Nombre de la canción']} / {pantalla['Álbum']}     {pantalla['Duración']}"
            turtle.setpos(-290, y)
            turtle.write(texto, font=("Arial", 15, "normal"))
            y -= 60
            
        if not diccionarios:
            print("No hay canciones guardadas")

    # Opcion 4: Ver artistas y su cantidad de canciones 
    elif opcion == 4:
        turtle.clear()
        turtle.setheading(0)
        turtle.pensize(0)        

        # Diccionario con artistas y canciones organizado de mayor a menor
        vista_ordenada = dict(sorted(vista.items(), key=lambda item: item[1], reverse=True))

        for artista, num_canciones in artistas.items():
            vista[artista] = num_canciones

        # Posicion original de todo
        y = 72
        x = -382

        circulo_x = -358
        circulo_y = 235

        artista_x = -255
        artista_y = 130

        canciones_x = -270
        canciones_y = 100
        
        # Fondo
        for artista, num_canciones in vista_ordenada.items():  
       
            if artista == 4:
                y -= 270
                x = -382
                circulo_x = -358
                circulo_y -= 270
                artista_x = -255
                artista_y -= 270
                canciones_x = -270
                canciones_y -= 270
            
            # Fondo
            dibujos_turtle.rectangulo(180, 250, x, y,'#262626')

            # Circulo
            turtle.colormode(255)
            turtle.fillcolor(dibujos_turtle.random_color())
            turtle.begin_fill()
            turtle.penup()
            turtle.goto(circulo_x, circulo_y)
            turtle.pendown()
            turtle.circle(65)
            turtle.end_fill()
            turtle.penup()

            # Letras
            turtle.color('white')
            turtle.goto(artista_x, artista_y)
            turtle.write(artista, align='right', font=('Arial', 20, 'bold'))
            turtle.goto(canciones_x, canciones_y)
            turtle.write('Canciones: {}'.format(num_canciones), align='right', font=('Arial', 12, 'normal'))
            turtle.setheading(0)

            # Posicion nueva en X
            x += 192
            circulo_x += 195
            artista_x += 195
            canciones_x += 195

    # Opcion 5: Eliminar todas las canciones 
    elif opcion == 5:
        turtle.reset()
        turtle.hideturtle()
        diccionarios.clear()
        print("Todas las canciones se han eliminado exitosamente!")
        dibujos_turtle.inicio()

    # Opción 6: Salir del programa
    elif opcion == 6:
        seguir_en_programa = False
        print("Eso ha sido todo, vuelva pronto!")
        turtle.bye()
    else:
        print("Seleccione una opción válida.")