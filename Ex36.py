print("-=-=-=-=-=-=-=-=-= Programa do Bubble Sort -=-=-=-=-=-=-=-=-= \n")

lista = [7, 15, 8, 2, 22, 4, 5]

i = 0

for j in range (0, len(lista)):
    for i in range(0, len(lista) - 1):
        if lista[i] > lista[i + 1]:
            temp = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = temp

print(lista)