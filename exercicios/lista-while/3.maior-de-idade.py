maiores = 0
i = 0

while i<5:
    idade = int(input(f"Digite a idade da {i+1}ª pessoa:\n"))

    if idade > 18:
        maiores +=1
    i+=1

print(f"Existem {maiores} pessoas com mais de 18 anos.")