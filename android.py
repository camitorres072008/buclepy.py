while True:
    voto=str(input("votar por android?:"))
    if voto== "si" or voto== "Si" or voto== "SI":
        android=0
        android=android+1
        print("se ha seleccionado: Android")
    else:
        voto=str(input("votar por ios?:"))
        if voto== "si" or voto== "Si" or voto== "SI":
            ios=0
            ios= ios+1
            print("se ha seleccionado: IOS")
        else:
            print("voto nulo")
    voto=str(input("¿Desea votar de nuevo? [S] o [N]?: "))
    if voto== "N" or voto== "n":
        break
if android>ios:
    print("El sistema operativo ganador es: Android")
elif ios>android:
    print("El sistema operativo ganador es: IOS")
else:
    print("Empate entre Android e IOS")
