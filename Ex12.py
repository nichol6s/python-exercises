n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 <= n2 and n1 <= n3:
    menor_numero = n1
    if n2 <= n3:
        numero_mediano = n2
        maior_numero = n3
    else:
        numero_mediano = n3
        maior_numero = n2
elif n2 <= n1 and n2 <= n3:
    menor_numero = n2
    if n1 <= n3:
        numer_mediano = n1
        maior_numero = n3
    else:
        numero_mediano = n3
        maior_numero = n1
else:
    menor_numero = n3
    if n1 <= n2:
        numero_mediano = n1
        maior_numero = n2
    else:
        numero_mediano = n2
        maior_numero = n1

print("Os números em ordem crescente são: ", menor_numero, numero_mediano, maior_numero)


