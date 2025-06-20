n = int(input("Quantos alunos? "))
alunos = []
indices_impar = []

print("Digite os nomes dos alunos:")

for x in range(n):
    nome = input("")
    alunos.append(nome)

for i in range(n):
    if i % 2 != 0:
        indices_impar.append(i)

for j in range(len(indices_impar) // 2):
    a = indices_impar[j]
    b = indices_impar[- (j + 1)]
    alunos[a], alunos[b] = alunos[b], alunos[a]

print("Nova lista")
for k in alunos:
    print(k)