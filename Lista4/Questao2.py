lista = []
print("Digite 10 números:")
for x in range(10):
    numero = float(input(""))
    lista.append(numero)
media = sum(lista) / 10
print(f"A média é: {media}")
print("Os números acima da média são:")
for i in lista:
    if i > media:
        print(i)