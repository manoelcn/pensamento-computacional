def primo(numero):
    if numero <= 1:
        divisores = [x for x in range(1, numero + 1) if numero % x == 0]
        return f"{numero} não é primo, os divisores são: {divisores}"
    if numero == 2:
        return f"{numero} é primo"
    if numero % 2 == 0:
        divisores = [x for x in range(1, numero + 1) if numero % x == 0]
        return f"{numero} não é primo, os divisores são: {divisores}"
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            divisores = [x for x in range(1, numero + 1) if numero % x == 0]
            return f"{numero} não é primo, os divisores são: {divisores}"
    return f"{numero} é primo"

n = int(input("Qual o valor de N? "))
numeros = []

print("Digite os valores:")
for x in range(n):
    valor = int(input(""))
    numeros.append(valor)

print("A classificação é:")
for i in numeros:
    print(primo(i))