print("Escriba el número a analizar: ")
num = int(input())

contadorCifras = 0
copiaNumero = num

while copiaNumero > 0:
    cifra = copiaNumero % 10
    copiaNumero = copiaNumero // 10
    contadorCifras = contadorCifras + 1

sumaCifras = 0
copiaNumero = num

while copiaNumero > 0:
    cifra = copiaNumero % 10
    copiaNumero = copiaNumero // 10
    # Elevamos la cifra usando el operador **
    sumaCifras = sumaCifras + (cifra ** contadorCifras)

if num == sumaCifras:
    print(f"{num} es un número de Armstrong.")
else:
    print(f"{num} no es un número de Armstrong.")