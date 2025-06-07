n = int(input(""))

for i in range(n):
    x = int(input(""))
    y = int(input(""))
    if x % 2 == 0:
        x += 1

    soma = 0
    for j in range(y):
        soma += x + (j *2)
    
    print(soma)