# Gerardo Fernández
# Victor Pérez
# Nils Muralles
# Programa que lleva el control de las mascotas que un albergue de animales domésticos tiene a su disposición.

# Importar los módulos
import dibujos_turtle
import utiles

# Diccionarios
Firulais = {
'Nombre' : 'Firulais',
'Tipo' : 'Perro',
'Color' : 'Cafe',
'Adoptado' : False,
'Edad en años' : 3.0,
'Enfermedades' : 'Ninguna de momento',
'Observaciones' : 'No le gusta estar solo, puede ser muy jugueton'
}

Mishy = {
'Nombre' : 'Mishy',
'Tipo' : 'Gato',
'Color' : 'Gris',
'Adoptado' : False,
'Edad en años' : 1.0,
'Enfermedades' : 'Pulgas',
'Observaciones' : 'Ninguna'
}

Toby = {
'Nombre' : 'Toby',
'Tipo' : 'Perro',
'Color' : 'Azul',
'Adoptado' : False,
'Edad en años' : 2.0,
'Enfermedades' : 'Infeccion en los oidos',
'Observaciones' : 'Le gusta ejercitarse, no come comida seca'
}

Tom = {
'Nombre' : 'Tom',
'Tipo' : 'Gato',
'Color' : 'Amarillo',
'Adoptado' : False,
'Edad en años' : 2.0,
'Enfermedades' : 'Ninguna de momento',
'Observaciones' : 'Ninguna de momento'
}

# Diccionario con todas las macotas
mi_diccionario = {
    "Firulais" : Firulais,
    "Mishy" : Mishy,
    "Toby" : Toby,
    "Tom" : Tom,
}

# Crear un menú que permita al usuario elegir lo que desea hacer
salir_del_programa = False
while salir_del_programa == False:
    print("")
    print("### BIENVENIDO ###")
    print("¿Qué desea hacer?")
    print("1. Ver listado de mascotas")
    print("2. Modificar el registro de una mascota")
    print("3. Ver fotografía de una mascota")
    print("4. Salir")
    print("")
    opcion = input("Seleccione una opción válida ")

    # Hacer que la opción elegida sea un dígito, y si no lo es, volver a ejecutar el menú
    if opcion.isdigit() == False:
        print("Seleccione un tipo de valor válido")
    else:
        opcion = int(opcion)

        # Opción 1: Ver listado de mascotas.
        if opcion == 1:
            print("")
            for mascota in mi_diccionario.keys():
                utiles.imprimir_diccionario(mi_diccionario[mascota])
                print("")
    
        # Opción 2: Modificar el registro de una mascota.
        elif opcion == 2:
            print("")
            print(list(mi_diccionario))
            mascota_modificar = input("¿A qué mascota desea modificar? ")

            # Valida que el nombre exista
            if utiles.validar_llaves(mascota_modificar, mi_diccionario):
                mascota_modificar = utiles.primera_mayuscula(mascota_modificar)
                print("")
                print("Ha seleccionado a " + mascota_modificar)
                print("")
                utiles.imprimir_diccionario(mi_diccionario[mascota_modificar])
                print("")

                valor = input("¿Qué información desea modificar? ")

                # Valida que el valor a modificar exista
                if utiles.validar_llaves(valor, mi_diccionario[mascota_modificar]):
                    valor = utiles.primera_mayuscula(valor)
                    
                    # Realiza las modificaciones
                    if valor.lower() == "edad en años":
                        mi_diccionario[mascota_modificar][valor] = utiles.validar_float(f"Ingrese un nuevo valor para {valor}: ")
                    elif valor.lower() == "adoptado":
                        mi_diccionario[mascota_modificar][valor] = utiles.validar_bool(f"Ingrese un nuevo valor para {valor}: ")
                    elif valor.lower() == "enfermedades" or valor.lower() == "observaciones":
                        mi_diccionario[mascota_modificar][valor] = input(f"Ingrese un nuevo valor para {valor}: ")
                    else:
                        print("La característica no se puede modificar.")

                    print("")
                    utiles.imprimir_diccionario(mi_diccionario[mascota_modificar])
                else:
                    print("La característica no es válida.")
            else:
                print("Esta mascota no se encuentra en el registro.")

        # Opción 3: Mostrar el dibujo de la mascota que seleccione el usuario
        elif opcion == 3:
            print("")
            print("1. Firulais")
            print("2. Mishy")
            print("3. Toby")
            print("4. Tom")
            print("")
            mascota_dibujar = input("¿A qué mascota desea dibujar? ")

            if mascota_dibujar.isdigit() == False:
                print("Seleccione un tipo de valor válido")
            else:
                mascota_dibujar = int(mascota_dibujar)

                if mascota_dibujar == 1:
                    print("Ha seleccionado a Firulais")
                    dibujos_turtle.perro('Saddlebrown')
                elif mascota_dibujar == 2:
                    print("Ha seleccionado a Mishy")
                    dibujos_turtle.gato('Grey')
                elif mascota_dibujar == 3:
                    print("Ha seleccionado a Toby")
                    dibujos_turtle.perro('Blue')
                elif mascota_dibujar == 4:
                    print("Ha seleccionado a Tom")
                    dibujos_turtle.gato('Yellow')
                else:
                    print("Seleccione un dígito válido.")

        # Opción 4: Salir del programa
        elif opcion == 4:
            salir_del_programa = True
        else:
            print("Seleccione una opción válida.")