print("==== Programa do Triângulo 2.0 ====")
print()

altura = int(input("Digite a altura do triângulo: "))
print()

for a in range(altura + 1):
    for b in range(a):
        print("*", end="")
    print()
for a in range(altura -1, 0, -1):
    for b in range(a):
        print("*", end="")
    print()
print()
print("==== Fim do Programa! ====")