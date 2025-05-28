print("Digite 10 números:")
lista = []
for x in range(10):
    numero = int(input(""))
    lista.append(numero)

media = sum(lista) / 10
print(f"A média é: {media}")
print("Os itens acima da média são:")
for x in lista:
    if x > media:
        print(x)