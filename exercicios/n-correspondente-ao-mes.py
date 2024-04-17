#NÚMERO CORRESPONDENTE AO MêS
num = int(input("Digite o número correspondente ao mês:\n"))

match num:
    case 1: print(f"Mês {num} é janeiro.")
    case 2: print(f"Mês {num} é fevereiro.")
    case 3: print(f"Mês {num} é março.")
    case 4: print(f"Mês {num} é abril.")
    case 5: print(f"Mês {num} é maio.")
    case 6: print(f"Mês {num} é junho.")
    case 7: print(f"Mês {num} é julho.")
    case 8: print(f"Mês {num} é agosto.")
    case 9: print(f"Mês {num} é setembro.")
    case 10: print(f"Mês {num} é outubro.")
    case 11: print(f"Mês {num} é novembro.")
    case 12:  print(f"Mês {num} é dezembro.")
    case _:
        print("Digite um número válido.")