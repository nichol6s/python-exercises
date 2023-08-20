def pg(numero):
    if numero == 1:
        return [1]
    else:
        return pg(numero - 1) + [3 * numero]
    
numero = int(input("Digite um numero: "))

print("A progressão geometrica de 1 até {} é {}".format(numero, pg(numero)))


