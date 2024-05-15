letras = []
vogais = ['a', 'e', 'i', 'o', 'u']

for i in range (10): 
    letras.append(input("Digite uma letra:\n").lower())

total = 0
consoantes = []
for letra in letras:
    if letra not in vogais: 
        consoantes.append(letra)
        total += 1

print (consoantes)
print (f"Você digitou {total} consoantes.")