#DIAS DO MÊS
mes = int(input("Digite o número do mês:\n"))

print("----------------")

if mes == 2:
    print("Número de dias: 28.")
elif mes in [4, 6, 9, 11]:
    print("Número de dias: 30.")
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    print("Número de dias: 31.")
else:
    print("Número inválido.")
