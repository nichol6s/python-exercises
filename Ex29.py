import random

lista = [random.randint(0, 500) for quantidade in range(100)]
print(lista)
print()

numero = int(input("Digite um número: "))


if numero in lista:
    print("O número {} está na lista.".format(numero))
else:
    print("O número {} não está na lista.".format(numero))
