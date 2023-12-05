#Solicitamos al usuario que ingrese un numero
numero = int(input("Ingrese un numero "))

suma = 0

#Calculamos si la suma de los divisores da como resultado el numero
for i in range(1, numero):
        if numero % i == 0:
            suma += i

#Comprobamos si el resultado de las sumas es igual al numero ingresado
if suma == numero:
    True
else: 
    False

#Imprimimos el resultado
if suma == numero:
    print(numero, "Es un numero perfecto")
else:
    print(numero, "No es un numero perfecto")