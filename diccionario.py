# Gerardo Fernandez

# Diccionario de cada mascota
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

print("""\n+---Bienvenido al registro de mascotas---+ 
""")


llaves_ordenadas = sorted(mi_diccionario.keys())

# imprimir los diccionarios
for llave in llaves_ordenadas:
    valor = mi_diccionario[llave]
    
    for clave, valor in valor.items():
        print(clave + ":", valor)
    print()

# Modificar valores
while True:
    modificar = input("Desea modificar el registro de alguna mascota? (y/n): ")
    if modificar == "n":
        break
    if modificar != "y":
        print("Opción inválida. Por favor ingrese 'y' o 'n'.")
        break
    elif modificar == "y":
        nombre = input("Ingrese el nombre del animal que desea modificar: ")
        if nombre in mi_diccionario:
            print("¿Qué valor desea modificar?")
            print("1 - Adoptado")
            print("2 - Edad en años")
            print("3 - Enfermedades")
            print("4 - Observaciones")

            opcion = int(input("Ingrese la opción que desea modificar: "))
            if opcion == 1:
                mi_diccionario[nombre]['Adoptado'] = bool(input("Ingrese True o False: "))
                print("El valor de 'adoptado'se ha modificado correctamente ")
                for llave in llaves_ordenadas:
                    valor = mi_diccionario[llave]
                    for clave, valor in valor.items():
                        print(clave + ":", valor)
                    print()

            elif opcion == 2:
                mi_diccionario[nombre]['Edad en años'] = float(input("Ingrese la nueva edad en años: "))
                print("El valor de 'Edad en años'se ha modificado correctamente ")
                for llave in llaves_ordenadas:
                    valor = mi_diccionario[llave]
                    for clave, valor in valor.items():
                        print(clave + ":", valor)
                    print()

            elif opcion == 3:
                mi_diccionario[nombre]['Enfermedades'] = input("Ingrese la nueva enfermedad: ")
                print("El valor de 'Enfermedades'se ha modificado correctamente ")
                for llave in llaves_ordenadas:
                    valor = mi_diccionario[llave]
                    for clave, valor in valor.items():
                        print(clave + ":", valor)
                    print()

            elif opcion == 4:
                mi_diccionario[nombre]['Observaciones'] = input("Ingrese las nuevas observaciones: ")
                print("El valor de 'Observaciones'se ha modificado correctamente ")
                for llave in llaves_ordenadas:
                    valor = mi_diccionario[llave]
                    for clave, valor in valor.items():
                        print(clave + ":", valor)
                    print()
            else:
                print("Opción no válida")
        else:
            print("El nombre ingresado no existe en el diccionario")
    else:
        print("Gracias")  
    break