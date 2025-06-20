def par(numero):
    if numero % 2 == 0:
        return 0
    else:
        return 1

soma = 0
for x in range(4):
    valor = int(input(f"Digite o número {x + 1}: "))
    if par(valor) == 0:
        soma = soma + valor

print(f"Soma dos números pares: {soma}")