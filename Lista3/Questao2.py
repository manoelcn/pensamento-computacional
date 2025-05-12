print("Insira a taxa do exame para 10 pacientes:")
valores = []
for i in range(10):
    valor = float(input())
    valores.append(valor)

media_aritmetica = sum(valores) / len(valores)
media_harmonica = len(valores) / sum(1 / numero for numero in valores)
produto = 1
for numero in valores:
    produto = produto * numero
media_geometrica = produto ** (1 / len(valores))

erro_harmonica = (media_harmonica - media_aritmetica) / media_aritmetica
erro_geometrica = (media_geometrica - media_aritmetica) / media_aritmetica
erro_medio = (erro_harmonica + erro_geometrica) / 2

print(f"Média aritmética: {media_aritmetica:.2f}")
print(f"Média harmônica: {media_harmonica:.2f}")
print(f"Média geométrica: {media_geometrica:.2f}")
print(f"Erro médio: {erro_medio * 100:.2f}%")