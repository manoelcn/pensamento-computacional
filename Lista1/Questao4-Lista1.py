numero = int(input("Qual é o número inteiro que deve ser utilizado para gerar a sequência? "))
sequencia = [ numero - 2, numero - 1, numero, numero + 1, numero + 2]
print(f"A sequência é a seguinte: {sequencia} {sum(sequencia)}")