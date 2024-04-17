senha_certa = 4401

while True: 
    tentativa = int(input("Digite sua senha de 4 digitos:\n"))
    if tentativa == senha_certa:
        print("Senha correta.")
    else: 
        print("Senha incorreta. Tente novamente.")
