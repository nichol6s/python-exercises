a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

if a > b:
    maior = a
    menor = b
elif b > a:
    maior = b
    menor = a
else:
    print("Os números são iguais :( ")
    quit()
    
print("Os números em ordem crescente são: ", menor, maior)
