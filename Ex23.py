print("==== Programa do Triângulo ====")
print()

altura = int(input("Digite a altura do triângulo: "))
print()

for a in range(altura + 1):
    for b in range(a):
        print("*", end="")
    print()
print()
print("==== Fim do Programa ====")