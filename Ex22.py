'''print("==== Programa do Retângulo ====")
print()

comprimento = int(input("Digite o valor do comprimento do retângulo: "))
altura = int(input("Digite o valor da altura do retângulo: "))
print()

for a in range(altura):
    for b in range(comprimento):
        print("*", end="")
    print()
print()
print("==== Fim do Programa ====") '''

x = 0

while x < 5:
    i = 0
    while i < 10:
        print("*", end="")
        i = i + 1
    print()
    x = x + 1
   
print("Fim")

