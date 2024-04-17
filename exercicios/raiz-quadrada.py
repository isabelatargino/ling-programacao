#EXERCÍCIO RAIZ QUADRADA

import math

num = float(input("Digite um número:\n"))

if num>=0:
    raiz = math.sqrt(num)
    print(f"√{num:.0f} = {raiz:.2f}")
else:
    print("Digite um número positivo.")