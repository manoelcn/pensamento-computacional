def nesima(n):
    for i in range(1, n + 1):
        print(f"{i} " * i)

# Programa principal
n = int(input("Digite o valor de n: "))
if n >=1:
    nesima(n)
else:
    print("Valor inválido!")