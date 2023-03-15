a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a > b and a > c:
    maior = a
    if b > c:
        menor = c
        menor2 = b
    else:
        menor = b
        menor2 = c
elif b > a and b > c:
    maior = b
    if a > c:
        menor = c
        menor2 = a
    else:
        menor = a
        menor2 = c
elif c > a and c > b:
    maior = c
    if a > b:
        menor = b
        menor2 = a
    else:
        menor = a
        menor2 = b
else:
    print("Os números são iguais :( ")
    quit()

print("Os números em ordem crescente são: ", menor2, menor, maior)
