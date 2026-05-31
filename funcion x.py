print("Ingrese el máximo valor para x: ")
valorX = int(input())


while valorX < 0:
    print("Ingrese el máximo valor para x: ")
    valorX = int(input())

for x in range(0, valorX + 1, 2):
    funci = x**3 + x**2 - 5
    print("Para x =", x, ", f(x) =", funci)