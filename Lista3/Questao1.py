altura_inicial_levi = float(input("Altura inicial de Levi: "))
taxa_crescimento_levi = float(input("Taxa de crescimento de Levi: "))
altura_inicial_hugo = float(input("Altura inicial de Hugo: "))
taxa_crescimento_hugo = float(input("Taxa de crescimento de Hugo: "))

if altura_inicial_levi >= altura_inicial_hugo:
    print("Erro: Hiago deve ser maior que Levi inicialmente.")
elif taxa_crescimento_levi <= taxa_crescimento_hugo:
    print("Erro: A taxa de crescimento de Levi deve ser maior que a de Hiago.")
else:
    anos = 0
    taxa_crescimento_hugo = taxa_crescimento_hugo / 100
    taxa_crescimento_levi = taxa_crescimento_levi /100
    while altura_inicial_hugo >= altura_inicial_levi:
        altura_inicial_levi += taxa_crescimento_levi
        altura_inicial_hugo += taxa_crescimento_hugo
        anos += 1
    print(f"Serão necessários {anos} anos para que Levi seja maior que Hiago.")