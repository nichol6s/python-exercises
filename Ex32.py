matriz = [['' for colunas in range(4)] for linha in range(5)]

letra = 'a'

for linha in range(5):
    for coluna in range(4):
        matriz[linha][coluna] = letra
        letra = chr(ord(letra) + 1)

for linha in matriz:
    print(linha)
