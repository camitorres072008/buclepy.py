cantestu=int(input("Ingrese la cantidad de estudiantes:"))
contestu=0
aprobaron=0
reprobaron=0
sumadef=0
while(contestu<cantestu):
    code=(input("Ingrese el codigo del estudiante:"))
    defin= float(input("Ingrese la def del estudiante:"))
    sumadef=sumadef+defin
    if defin>=3:
        aprobaron=aprobaron+1
    else:
        reprobaron=reprobaron+1
    contestu=contestu+1
    sumadef=sumadef+defin
promedio=sumadef/cantestu
print("El promedio de las definitivas es:",promedio)
print("La cantidad de estudiantes que aprobaron es:",aprobaron)
print("La cantidad de estudiantes que reprobaron es:",reprobaron)