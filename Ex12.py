a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o  terceiro número: "))

if a > b and c:
    maior = a
    menor = b 
    menor2 = c
    
elif b > a and c:
    maior = b
    menor = a 
    menor2 = c

if c > b and a:
    maior = c
    menor = b 
    menor2 = a

elif c > a and b:
    maior = c
    menor = a
    menor2 = b

else:
    print("Os números são iguais :( ")
    quit()
    
print("Os números em ordem crescente são: ", menor2, menor, maior)
