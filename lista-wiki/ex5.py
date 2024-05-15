numeros = []
pares = []
impares = []

for i in range(20):
    numero = int(input(f"Digite o {i+1}º número: \n"))
    numeros.append(numero)
    if (numero % 2 == 0):
        pares.append(numero)
    else: 
        impares.append(numero)
    
print (f"Os números digitados foram: {numeros}.")
print (f"Os números pares digitados foram: {pares}.")
print (f"Os números impares digitados foram: {impares}.")