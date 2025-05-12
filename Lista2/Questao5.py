nome = input("Nome: ")
idade = int(input("Idade: "))
if idade < 5:
    mensagem = "Categoria não aplicável para menores de 5 anos."
elif 5 <= idade <=10:
    mensagem = f"O atleta {nome} está classificado na categoria Infantil."
elif 11 <= idade <= 15:
    mensagem = f"O atleta {nome} está classificado na categoria Juvenil."
elif 16 <= idade <= 20:
    mensagem = f"O atleta {nome} está classificado na categoria Júnior."
elif 21 <= idade <= 25:
    mensagem = f"O atleta {nome} está classificado na categoria Profissional."
else:
    mensagem = f"Fora das categorias estabelecidas."
print(mensagem)