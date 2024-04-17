#EXERCÍCIO NOTAS DA PROVA

nota = int(input("Digite a nota a ser convertida:\n"))

if nota>=86 and nota<=100:
    print("NOTA A")
elif nota>=61 and nota<=85:
    print("NOTA B")
elif nota>=36 and nota<=60:
    print("NOTA C")
elif nota>=1 and nota<=35:
    print("NOTA D")
elif nota==0:
    print("NOTA E")
else:
    print("Insira um número válido!")