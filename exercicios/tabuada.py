#PROGRAMA PARA REALIZAR A TABUADA DO 1 AO 10 DO NÚMERO ESCOLHIDO

num = int(input("Digite um número entre 1 e 10:\n"))

if num>10 or num<=0:
    print("Número não aceito, digite um número entre um e dez.")
else: 
    print(f"Tabuada do {num}")
    for i in range(1,11):
        result = num * i
        print(f"{num} X {i} = {result}")