numero_jogadores = int(input("Quantidade de jogadores? "))
if numero_jogadores >= 1:
    saque = []
    bloqueio = []
    ataque = []
    saque1 = []
    bloqueio1 = []
    ataque1 = []
    print("Digite os dados para cada jogador: ")
    for x in range(numero_jogadores):
        nome, s, b, a, s1, b1, a1 = input("").split()
        saque.append(s), bloqueio.append(b), ataque.append(a)
        saque1.append(s1), bloqueio1.append(b1), ataque1.append(a1)


percentual_saques = (sum(map(int, saque1)) / sum(map(int, saque))) * 100
percentual_bloqueios = (sum(map(int, bloqueio1)) / sum(map(int, bloqueio))) * 100
percentual_ataques = (sum(map(int, ataque1)) /sum(map(int, ataque))) * 100

print("As estatísticas do jogo são as seguintes: ")
print(f"Pontos de saque: {percentual_saques:.2f} %")
print(f"Pontos de bloqueio: {percentual_bloqueios:.2f} %")
print(f"Pontos de ataque: {percentual_ataques:.2f} %")  