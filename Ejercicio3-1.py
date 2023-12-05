# En este programa haremos un control de cuantos bonos recibira cada empleado este año

# Gerardo Fernandez 23763
# Eddy Giron 23073

# Variables y Diccionario
Bonos = {
'Leticia' : 50.00,
'Alberto' : 35.00,
'Carlos' : 15.00,
'Karina' : 23.00,
'Julio' : 12.00,
'Guevara' : 30.00,
'Emilio' : 25.00,
'Pamela' : 62.50,
'Andres' : 28.50,
'Ignacio' : 10.00,
}

seguir_en_programa = True
Total = 0

# Programa
while seguir_en_programa == True:
    print("### Bienvenido ####")
    print("1. Agregar Bono a ")
    print("2. Salir")
    opcion = input("Seleccione una opción válida ")

    # Hacer que la opción elegida sea un dígito, y si no lo es, volver a ejecutar el menú
    if opcion.isdigit() == False:
        print("Seleccione un tipo de valor válido")
    else:
        opcion = int(opcion)

        # Control de bonos
        if opcion == 1:
            for k,v in Bonos.items(): # Imprimir listado de empleados con sus respectivos bonos
             print(k,v)

            print("Cuando desee salir escriba: 'salir'") # Si el usuario termino escribir salir
            while True:
                Persona = input("Ingrese el nombre de la persona que recibira un bono este año: ") 
                # Validar que la persona que ingreso el usuario esta en el registro
                if Persona in Bonos:
                    Total += Bonos[Persona]
                    print(f"El bono de {Persona} ha sido agregado.")
                
                elif Persona.lower() == "salir":
                    print(f"El total en bonos este año sera de {Total}")
                    seguir_en_programa = False
                    break

                else:
                    print("Esta persona no se encuentra en el registro.")
        
        # Salir del programa
        elif opcion == 2:
                seguir_en_programa = False
        else:
            print("Seleccione una opción válida.")