n = int(input("Quantos nomes? "))
nomes = []
for x in range(n):
    nome = input("")
    nomes.append(nome)

print("Você digitou:")
for i in nomes[::-1]:
    print(i)