#OPERAÇÕES MATEMÁTICAS
num1 = float(input("Digite um número:\n"))
num2 = float(input("Digite um número:\n"))
operacao = (input("Digite a operação a ser feita:\n"))

match operacao:
    case '*':
        result = num1*num2
        print(f"{num1} x {num2} = {result}")
    case '+':
        result = num1+num2
        print(f"{num1} + {num2} = {result}")
    case '-':
        result = num1-num2
        print(f"{num1} - {num2} = {result}")
    case '/':
        result = num1/num2
        print(f"{num1}/{num2} = {result}")