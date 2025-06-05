valor = float(input("Qual o valor da compra? "))
forma_pagamento = input("Como gostaria de pagar: à vista(V) ou à prazo(P)? ").lower()
if forma_pagamento == "v":
    print(f"Valor à pagar: {valor - (valor * 0.05)}")
elif forma_pagamento == "p":
    print(f"Valor à pagar: {valor * 1.08}")
    for x in range(3):
        print(f"Parcela {x + 1}: {(valor * 1.08) / 3}")
else:
    print("Erro!")