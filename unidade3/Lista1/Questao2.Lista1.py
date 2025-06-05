nota1 = float(input("Qual é a nota da primeira unidade? "))
nota2 = float(input("Qual é a nota da segunda unidade? "))
nota3 = float(input("Qual é a nota da terceira unidade? "))
media_final = (((nota1 * 2) + (nota2 * 3) + (nota3 * 4)) / 9)
if media_final >= 7:
    print("Francisco está aprovado")
elif media_final < 3:
    print("Francisco está reprovado")
else:
    print("Francisco está em prova final")