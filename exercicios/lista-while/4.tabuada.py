num = int(input("Digite um número entre 1 e 10: \n"))

if num>=1 and num<=10: 
    i=0
    while i<10: 
        i+=1
        result = num*i
        print(f"{num} X {i} = {result}")
else:
    print("Digite um número válido.")