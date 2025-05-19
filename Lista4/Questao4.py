numero = int(input("Qual o número de pessoas? "))
lista = []
print("Informe as idades: ")
for x in range(numero):
    idade = int(input(""))
    lista.append(idade)
media = sum(lista) / numero
print(f"A média de idade das pessoas é {round(media)} anos")