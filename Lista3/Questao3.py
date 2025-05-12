print("Cardápio")
print("100 - Cachorro quente: R$ 5,50")
print("101 - Bauru simples: R$ 15,00")
print("103 - Hambúrguer: R$ 20,00")
print("104 - Cheeseburger: R$ 18,00")
print("105 - Refrigerante: R$ 6,00")

total = []

while True:
    codigo = int(input("Digite o código do item: "))
    if codigo == -1:
        break
    quantidade = int(input("Digite a quantidade: "))

    if codigo == 100:
        total.append(quantidade * 5.50)
    elif codigo == 101:
        total.append(quantidade * 15)
    elif codigo == 103:
        total.append(quantidade * 20)
    elif codigo == 104:
        total.append(quantidade * 18)
    elif codigo == 105:
        total.append(quantidade * 6)
    else:
        print("Código inválido!")
resultado = sum(total)
print(f"Total a pagar: R$ {resultado}")