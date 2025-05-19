lista = []
print("Informe as pontuações dos atletas. Digite -1 para encerrar")
while True:
    pontuacao = int(input(""))
    lista.append(pontuacao)
    if pontuacao == -1:
        break
recorde = max(lista)
print(f"O recorde de pontos é {recorde}")