#PROGRAMA PARA LER NOTAS, MOSTRAR A MÉDIA E DEFINIR SE ESTÁ REPROVADO, DE RECUPERAÇÃO OU APROVADO

n1 = float(input("Digite a primeira nota:\n"))
n2 = float(input("Digite a segunda nota:\n"))

media = (n1 + n2)/2

if media >=4 and media<=6: 
    print(f"Você está de recuperação, sua média foi: {media:.2f}")
elif media<4:
    print(f"Você está reprovado, sua média foi: {media:.2f}")
elif media>=6:
    print(f"Você está aprovado! Sua média foi: {media:.2f}")
    
    



