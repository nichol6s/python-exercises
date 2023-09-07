# Ler o arquivo notas.csv, mostrar as linhas na tela individualmente, calcular médias e somas, e gravar em notas_calculadas.csv

# Função para calcular a média
def calcular_media(notas):
    return sum(notas) / len(notas)

# Abrir o arquivo de origem para leitura
with open('notas.csv', 'r') as source_file:
    lines = source_file.readlines()

calculated_lines = []

# Processar cada linha do arquivo de origem
for line in lines:
    data = line.strip().split(',')
    name = data[0].strip()
    grades = [float(grade.strip()) for grade in data[1:]]
    total = sum(grades)
    mean = calcular_media(grades)

    # Mostrar a linha na tela
    print("Linha:", line.strip())
    
    # Mostrar os resultados na tela
    print("Nome:", name)
    print("Notas:", ", ".join(data[1:]))
    print("Soma das notas:", total)
    print("Média das notas:", mean)
    print()

    calculated_line = f'{name}, {", ".join(data[1:])}, {total:.1f}, {mean:.2f}\n'
    calculated_lines.append(calculated_line)

# Abrir o arquivo de destino para escrita
with open('notas_calculadas.csv', 'w') as dest_file:
    dest_file.writelines(calculated_lines)

print("Arquivo notas_calculadas.csv gerado com sucesso.")
