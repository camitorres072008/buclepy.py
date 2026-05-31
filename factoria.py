print("Ingrese el número para el factorial: ")
num = int(input())

if num < 0:
    print("No se puede calcular el factorial")
else:
    factorial = 1
    inferiores = 1
    
    while True:
        factorial = factorial * inferiores
        inferiores = inferiores + 1
        
        if inferiores > num:
            break
            
    print(f"Factorial de {num} es: {factorial}")