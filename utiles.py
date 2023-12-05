# Gerardo Fernández
# Nils Muralles
# Victor Pérez
# Módulo que contiene las validaciones necesarias

# Imprime de manera legible un diccionario
def imprimir_diccionario(diccionario):

    # Reccorre el diccionario e imprime cada valor con su llave en una línea
    for llave, valor in diccionario.items():
        print(llave, ":", valor)

# Convierte un string para que tenga la primera mayúscula y las demás minúsculas
def primera_mayuscula(cadena):
    cadena = cadena[0].upper() + cadena[1:len(cadena)].lower()
    return cadena

# Valida que una llave esté en un diccionario dado
def validar_llaves(cadena, diccionario):
    lista_llaves = [llave.lower() for llave in diccionario.keys()]
    
    if cadena.lower() in lista_llaves:
        return True
    else:
        return False

# Valida que el ingreso sea de tipo flotante o entero
def validar_float(mensaje):
    preguntar = True
    while preguntar == True:
        ingreso = input(mensaje)
        try:
            ingreso = float(ingreso)
            return ingreso
        except ValueError:
            print("Ingreso no válido")

# Valida que el ingreso sea de tipo booleano
def validar_bool(mensaje):
    preguntar = True
    while preguntar == True:
        ingreso = input(mensaje)
        if ingreso.lower() == "true":
            return True
        elif ingreso.lower() == "false":
            return False
        else:
            print("Ingreso no válido")