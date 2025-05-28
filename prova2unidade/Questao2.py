itens = int(input("Quantas itens serão calculados? "))
valorTotal = []
for x in range(itens):
    valor = float(input(f"Qual o valor do item {x + 1}: "))
    quantidade = int(input(f"Qual a quantidade do item {x + 1}: "))
    resultado = valor * quantidade
    valorTotal.append(resultado)
print(f"O valor total da sua compra: {sum(valorTotal):.2f}")