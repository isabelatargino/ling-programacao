vetor = []
for i in range(10):
    numero = float(input(f"Digite o {i + 1}º número: "))
    vetor.append(numero)
print("Números na ordem inversa:")
for numero in reversed(vetor):
    print(numero)