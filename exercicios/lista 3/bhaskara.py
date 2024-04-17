import math

def calcularBhaskara(a, b, c): 
    if a==0:
        print("A precisa ser diferente de 0.")
        return
    
    delta = b**2 - 4*a*c

    if delta < 0:
        print("Delta é negativo, a equação não possui raízes reais.")
        return
    elif delta == 0: 
        raiz = -b / (2*a)
        print(f"Raiz real: {raiz}")
    else: 
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"As raízes reais são: {raiz1} e {raiz2}")

a= float(input("Digite o valor de A:\n"))

if a != 0: 
    b = float(input("Digite o valor de B:\n"))
    c = float(input("Digite o valor de C:\n"))
    calcularBhaskara(a,b,c)
else:
    print("A = 0, não é uma equação de segundo grau.")