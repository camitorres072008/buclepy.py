print("Escriba un número entero:")
num = int(input())

if num > 0:
    copiaNumero = num
    contadorCifras = 0
    sumaCifras = 0
    
    while copiaNumero > 0:
        cifra = copiaNumero % 10
        
        copiaNumero = copiaNumero // 10
        
        sumaCifras = cifra + sumaCifras
        contadorCifras = contadorCifras + 1
        
    print(f"La cantidad de cifras de: {num}")
    print(f"son: {contadorCifras}")
    print(f"La sumatoria es: {sumaCifras}")
    
else:
    print("No es un número positivo")