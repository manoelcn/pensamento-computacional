numero_de_pessoas = int(input("Qual o número de pessoas? "))
lista_de_idades = []
print("Informe as idades: ")
for x in range(0,numero_de_pessoas):
    idade = int(input(""))
    lista_de_idades.append(idade)
resultado = sum(lista_de_idades) / numero_de_pessoas
print(f"A média de idade das pessoas é {round(resultado)} anos")