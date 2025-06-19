n = int(input("Qual o N? "))
lista = []

print("Digite os valores:")
for x in range(n):
    valor = int(input(""))
    lista.append(valor)

operacao = input("Qual a op? ")
if operacao == "0":
    a = int(input("Qual o A? "))
    b = int(input("Qual o B? "))
    resultado = lista[(a - 1)] + lista[(b - 1)]
    print(f"{lista[(a - 1)]} + {lista[(b - 1)]} = {resultado} ")
elif operacao == "1":
    a = int(input("Qual o A? "))
    b = int(input("Qual o B? "))
    resultado = lista[(a - 1)] * lista[(b - 1)]
    print(f"{lista[(a - 1)]} * {lista[(b - 1)]} = {resultado} ")
else:
    print("Erro")
