print("-=-=-=-=-=- Programa de Busca Binária -=-=-=-=-=- \n")

lista = [4, 6, 8, 12, 15, 16, 19, 22]
valor_procurado = 22
encontrado = None
inicio = 0
termino = len(lista) - 1

while encontrado == None:
    meio = int(((termino - inicio) / 2) + inicio)
    if valor_procurado == lista[meio]:
        encontrado = meio
    elif valor_procurado > lista[meio]:
        if termino == meio:
            break
        else:
            inicio = meio + 1
    elif valor_procurado < lista[meio]:
        if inicio == meio:
            break
        else:
            termino = meio - 1

print("Valor encontrado na posicao: ", encontrado)