def tipoTriangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"
    
lado1 = float(input("Digite o primeiro lado do triângulo:\n"))
lado2 = float(input("Digite o segundo lado do triângulo:\n"))
lado3 = float(input("Digite o terceiro lado do triângulo:\n"))

if lado1 + lado2 > lado3 and lado1 + lado3 >lado2 and lado2 + lado3 > lado1: 
    print("Pode formar um triângulo")

    tipo = tipoTriangulo(lado1, lado2, lado3)
    print(f"Esse triângulo é {tipo}")
else: 
    print("Os valores fornecidos não podem formar um triângulo.")
    

