# Realizar un programa que verifique la compatibilidad de una pareja mediante algunos parametros en sus nombres 
# Eddy Giron
# Gerardo Fernandez

print("### BIENVENIDO AL LOVE COMPATIBILITY TEST ###")
c = int(input("Ingrese la cantidad de parejas que desea comprobar su compatibilidad: "))

parejas = []

# Comprobar si el número ingresado es un entero positivo
if c <= 0:
    print("Por favor ingrese un numero entero positivo.")
else:
    for i in range(c):
        n1 = input("Nombre 1: ")
        n2 = input("Nombre 2: ")
        pareja = n1 + " y " + n2
        parejas.append(pareja)

    # Analizar la compatibilidad de cada pareja de nombres y almacenarla en una lista
    compatibilidad = []
    for pareja in parejas:
        n1, n2 = pareja.split(" y ")
        score = 0
        if len(n1) == len(n2):
           score += 10
        if n1[0] in "qwrtyupsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM" and n2[0] in "qwrtyupsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM" or n1[-1] in "qwrtyupsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM" and n2[-1] in "qwrtyupsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM":
           score += 10
        if n1[0] in "aeiouAEIOU" and n2[0] in "aeiouAEIOU" or n1[-1] in "aeiouAEIOU" and n2[-1] in "aeiouAEIOU":
            score += 5
        if n1[0] == n2[0]:
            score += 3
        if n1[-1] == n2[-1]:
            score += 2
        compatibilidad.append((pareja, score))

    # Ordenar la lista de parejas por su puntuación de compatibilidad de menor a mayor
    compatibilidad = sorted(compatibilidad, key=lambda x: x[1])

    # Imprimir la lista de parejas con su puntuación en el formato solicitado
    print("\nLista de parejas con su puntuación de compatibilidad de menor a mayor:")
    for pareja, score in compatibilidad:
        if score >= 20:
            print(f"La compatibilidad entre {pareja.upper()} es de: {score} Felicidades son almas gemelas!")
        else:
            print(f"La compatibilidad entre {pareja} es de: {score}")

