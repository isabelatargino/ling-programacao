def encontrarMaiorNumero(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else: 
        return num3
    
def encontrarMenorNumero(num1, num2, num3):
    if num1 < num2 and num1 < num3:
        return num1
    elif num2 < num1 and num2 < num3:
        return num2
    else: 
        return num3 
    
num1 = float(input("Digite um número:\n"))
num2 = float(input("Digite outro número:\n"))
num3 = float(input("Digite outro número:\n"))

maiorNumero = encontrarMaiorNumero(num1, num2, num3)
menorNumero = encontrarMenorNumero(num1, num2, num3)
print(f"O menor número é {menorNumero} e o maior número é {maiorNumero}")