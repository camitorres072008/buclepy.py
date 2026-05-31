seguir = 'S'

while seguir == 'S' or seguir == 's':
    
    print("Con cuál tabla desea jugar?: ")
    tabla = int(input())
    
    while tabla < 1 or tabla > 20:
        print("Con cuál tabla desea jugar?: ")
        tabla = int(input())
        
    aciertos = 0
    desaciertos = 0
    

    for contadorFilas in range(1, 11, 1):
        producto = tabla * contadorFilas
        
        print("Escriba el resultado de ", tabla, " x ", contadorFilas)
        respuesta = int(input())
        

        if respuesta == producto:
            print("Felicitaciones")
            aciertos = aciertos + 1
        else:
            print("Lo siento, ese no es el resultado")
            print("La respuesta correcta es: ", producto)
            desaciertos = desaciertos + 1
            
    print("Aciertos: ", aciertos)
    print("Desaciertos: ", desaciertos)
    
    if aciertos <= 5:
        print("Insuficiente")
    else:
        if aciertos <= 7:
            print("Aceptable")
        else:
            if aciertos <= 9:
                print("Sobresaliente")
            else:
                print("Excelente")
                
    print("¿Desea volver a jugar [S] o [N]?: ")
    seguir = input()
    
    while seguir != 'S' and seguir != 'N' and seguir != 's' and seguir != 'n':
        print("¿Desea volver a jugar [S] o [N]?: ")
        seguir = input()