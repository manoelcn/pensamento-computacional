nota1 = float(input("Qual é a nota da primeira unidade? "))
nota2 = float(input("Qual é a nota da segunda unidade? "))
nota3 = float(input("Qual é a nota da terceira unidade? "))
resultado = ((nota1 * 2) + (nota2 * 3) + (nota3 * 4)) / 9
if resultado >= 7:
    print("Francisco está aprovado")
elif resultado < 3:
    print("Francisco está reprovado")
else:
    print("Francisco está em prova final")