# Gerardo Andre Fernandez Cruz #23763
# Proposito:  Llevar el control de un servicio de renta de videojuegos
#             fisicos. La tienda tiene un limite de 10 videojuegos.
#             Los videojuegos tienen 3 categorias (Premium, Normal, Clasico)
#             Los precios de alquiler son: Premium Q15, Normal Q10 y Clasico Q7
#             Hay 3 videojuegos premium, 3 normales y 4 clasicos

# Variables
total_ingresos = 0
videos_en_stock = 10
juegos_premium = 3
juegos_normales = 3
juegos_clasicos = 4
precio_premium = 15
precio_normal = 10
precio_clasico = 7

seguir_en_programa = True
while seguir_en_programa == True:
    # Menu
    print("\n ### CONTROL DE ALQUILER DE VIDEOJUEGOS ###")
    # Solicitamos la categoria a alquilar
    categoria = input("""
    Seleccione que categoria desea alquilar:
    1. Premium
    2. Normal
    3. Clasico
    4. Ninguna, salir del programa
    """)

    if categoria.isdigit() == True:
        # Convertimos el valor de cateogoria a un tipo entero
        categoria_entero = int(categoria)
        
        # Validamos que el numero este en el rango del menu
        if categoria_entero >= 1 and categoria_entero <=4:
            # Validamos el tipo de categoria
            if categoria_entero == 1:
                print("Premium")
                if videos_en_stock > 0 and juegos_premium > 0:
                    # Quitamos videojuegos del stock
                    videos_en_stock = videos_en_stock - 1
                    juegos_premium = juegos_premium - 1
                    # Sumamos ingresos del alquiler
                    total_ingresos = total_ingresos + precio_premium
                    print("Ingresos al momento:", total_ingresos)
                else:
                    print("No hay videojuegos disponibles")
            elif categoria_entero == 2:
                print("Normal")
                 # Validamos el tipo de categoria
                if videos_en_stock > 0 and juegos_normales > 0:
                    # Quitamos videojuegos del stock
                    videos_en_stock = videos_en_stock - 1
                    juegos_normales = juegos_normales - 1
                    # Sumamos ingresos del alquiler
                    total_ingresos = total_ingresos + precio_normal
                    print("Ingresos al momento:", total_ingresos)
                else:
                    print("No hay videojuegos disponibles")
            elif categoria_entero == 3:
                print("Clasico")
                if videos_en_stock > 0 and juegos_clasicos > 0:
                    # Quitamos videojuegos del stock
                    videos_en_stock = videos_en_stock - 1
                    juegos_clasicos = juegos_clasicos - 1
                    # Sumamos ingresos del alquiler
                    total_ingresos = total_ingresos + precio_clasico
                    print("Ingresos al momento:", total_ingresos)
                else:
                    print("No hay videojuegos disponibles")
            else:
                # Salimos del programa
                print("Gracias por usar nuestro programa")
                seguir_en_programa = False
        else:
            print("ERROR: Opcion no valida")
    else:
        print("ERROR: Ingreso invalido")
