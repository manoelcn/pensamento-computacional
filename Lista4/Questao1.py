print("A lista contém os seguintes nomes:")
print("Daniel")
print("Aluizio")
print("Isabel")
print("Teles")
print("Eduardo")
lista = ["daniel", "aluizio", "isabel", "teles", "eduardo"]
nome = input("Qual nome você quer verificar? ").lower()
if nome in lista:
    print(f"O nome {nome.capitalize()} está na lista, acesso permitido!")
else:
    print(f"O nome {nome.capitalize()} não está na lista, acesso negado!")