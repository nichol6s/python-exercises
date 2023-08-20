matriz = [[0 for coluna in range(3)] for linha in range(7)]

for linha in range(7):
    num = int(input(f"Digite o {linha+1}º número: "))
    
    matriz[linha][0] = num
    
    matriz[linha][1] = sum([matriz[coluna][0] for coluna in range(linha+1)])
    
    matriz[linha][2] = matriz[linha][1] / (linha+1)

print("Número   Soma   Média")
for i in range(6, -1, -1):
    print(f"   {matriz[i][0]}      {matriz[i][1]}      {matriz[i][2]}")
