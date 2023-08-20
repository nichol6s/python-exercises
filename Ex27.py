numeros = [34, 67, 12, 9, 52, 13, 126, 42, 1, -128, -54, 87]

soma = sum(numeros)
print("A soma de todos os elementos da lista é:", soma)
print()

produto = 1
for num in numeros:
    produto *= num
print("O produto de todos os elementos da lista é:", produto)
print()

blocos = [numeros[i:i+3] for i in range(0, len(numeros), 3)]
print("A lista agrupada em blocos de 3 números é:", blocos)
print()

blocos = [numeros[i:i+3] for i in range(0, len(numeros), 3)]
somas = [sum(bloco) for bloco in blocos]
print("A soma dos números em cada bloco é:", somas)
print()

maior = max(numeros)
print("O maior número da lista é:", maior)
print()

segundo_maior = sorted(numeros, reverse=True)[1]
print("O segundo maior número da lista é:", segundo_maior)
print()

menor = min(numeros)
print("O menor número da lista é: ", menor)
print()

segundo_menor = sorted(numeros)[1]
print("O segundo menor número da lista é:", segundo_menor)