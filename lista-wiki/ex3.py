notas = []

for i in range(1, 5):
    nota = float(input(f'Digite a nota {i}: '))
    notas.append(nota)

print("As notas digitadas foram:")
for nota in notas:
    print(nota)

media = sum(notas) / len(notas)
print(f'A média é: {media:.2f}')

