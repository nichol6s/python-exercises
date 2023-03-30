print("Programa do teste dos triangulos")
print()

altura = int(input("Digite a altura dos triangulo: "))
print()

for a in range(altura + 1):
    for b in range (a):
        print("*", end="")  
    print()
for a in range (altura - 1, 0, -1):
    for b in range(a):
        print("*", end="")  
    print()
print()
print("=== Fim do Progama! ===")