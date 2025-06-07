lista_valores = []
while True:
    valor = float(input("Informe os gastos no dia: "))
    lista_valores.append(valor)
    if valor == 0:
        break
resultado = max(lista_valores)
if resultado == 0:
    print("Você não teve gastos hoje!")
else:
    print(f"O seu maior gasto hoje foi R$ {resultado:.2f}")