meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
numero = int(input("Qual é o número do mês? "))
if 1 <= numero <= 12:
    print(f"O mês é {meses[numero - 1]}")
else:
    print(f"Erro: não existe mês de número {numero}! Por favor, digite um número entre 1 e 12.")