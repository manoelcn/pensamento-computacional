t = int(input())
for x in range(t):
    populacao_a = int(input(""))
    populacao_b = int(input(""))
    taxa_crescimento_a = float(input(""))
    taxa_crescimento_b = float(input(""))
    anos = 0
    while populacao_a <= populacao_b and anos <= 100:
        populacao_a += int(populacao_a * (taxa_crescimento_a / 100))
        populacao_b += int(populacao_b * (taxa_crescimento_b / 100))
        anos += 1
    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{anos} anos.")