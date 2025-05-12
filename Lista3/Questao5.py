print("Informe os gastos no dia: ")
resultado = []
while True:
    gastos = float(input(""))
    if gastos == 0:
        break
    resultado.append(gastos)
if len(resultado) > 1:
    print(f"O seu maior gasto hoje foi R$ {max(resultado)}")
else:
    print("Você não teve gastos hoje!")