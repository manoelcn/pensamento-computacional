while True:
    n = int(input())
    if n == 0:
        break

    for l in range(n):
        linha = []
        for c in range(n):
            valor = abs(l - c) + 1
            linha.append(f"{valor} ")
        print(linha)
    print()