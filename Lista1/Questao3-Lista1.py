area_total = []
for x in range(1,5):
    largura = float(input(f"Qual é a largura do lote {x} ? "))
    comprimento = float(input(f"Qual é o comprimento do lote {x}? "))
    area = largura * comprimento
    area_total.append(area)
print(f"A área total do terreno é {sum(area_total)} m2")