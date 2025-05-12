valor = float(input("Qual o valor da compra? "))
forma_de_pagamento = input("Como gostaria de pagar à vista(V) ou à prazo(P)? ")
if forma_de_pagamento == "V" or forma_de_pagamento == "v":
    print(f"Valor à pagar: { valor - (valor * 0.05) }")
else:
    print(f"Valor à pagar: {valor * 1.08}")
    for x in range(0,3):
        print(f"Parcela {x + 1}: {(valor * 1.08) / 3}")