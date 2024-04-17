#LANCHONETE
pedido = int(input("Digite o código do pedido:\n"))
quantidade = int(input("Digite a quantidade:\n"))

preco = 0

if pedido == 100:
    preco = 1.20
    conta = quantidade * preco
    print(f"------------\nNota fiscal\n{quantidade} x Cachorro-quente\nPreço final: {conta:.2f}")
elif pedido == 101:
    preco = 1.30
    conta = quantidade * preco
    print(f"------------\nNota fiscal\n{quantidade} x Bauru Simples\nPreço final: {conta:.2f}")
elif pedido == 102:
    preco = 1.50
    conta = quantidade * preco
    print(f"------------\nNota fiscal\n{quantidade} x Bauru com Ovo\nPreço final: {conta:.2f}")
elif pedido == 103:
    preco = 1.20
    conta = quantidade * preco
    print(f"------------\nNota fiscal\n{quantidade} x Hamburger\nPreço final: {conta:.2f}")
elif pedido == 104:
    preco = 1.70
    conta = quantidade * preco
    print(f"------------\nNota fiscal\n{quantidade} x Cheeseburger\nPreço final: {conta:.2f}")
elif pedido == 105:
    preco = 2.20
    conta = quantidade * preco
    print(f"------------\nNota fiscal\n{quantidade} x Suco\nPreço final: {conta:.2f}")
elif pedido == 106: 
    preco = 1.00
    conta = quantidade * preco
    print(f"------------\nNota fiscal\n{quantidade} x Refrigerante\nPreço final: {conta:.2f}")
    
