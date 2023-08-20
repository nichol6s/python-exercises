import random

lista = [random.randint(0, 500) for quantidade in range(100)]
print(lista)
print()

numero = int(input("Digite um número: "))

ocorrencias = lista.count(numero)

if ocorrencias > 0:
    print("O número {} está na lista.".format(numero))
    print("Há {} ocorrências deste número na lista.".format(ocorrencias))
else:
    print("O número {} não está na lista.".format(numero))
