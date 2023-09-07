def troca_dicionario(letra):
    lista_troca = {"a": "4", "e": "3", "i": "1", "o": "0", "t": "7", "s":"5", }

    if letra in lista_troca:
        return lista_troca(letra)
    else:
        return letra
    
arquivo = open("D:/Python/1TDSPM/notas.txt", "r")

linha = arquivo.readline()
lista = linha.split(",")

print(lista[0], sum)