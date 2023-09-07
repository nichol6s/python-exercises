# Ler o arquivo a.csv, adicionar 1,0 ponto na nota de cada aluno e gravar no arquivo b.csv

# Abrir o arquivo de origem para leitura
with open('a.csv', 'r') as source_file:
    lines = source_file.readlines()

modified_lines = []

# Processar cada linha do arquivo de origem
for line in lines:
    name, grade = line.strip().split(';')
    new_grade = float(grade.replace(',', '.')) + 1.0
    modified_lines.append(f'{name}; {new_grade:.1f}\n')

# Abrir o arquivo de destino para escrita
with open('b.csv', 'w') as dest_file:
    dest_file.writelines(modified_lines)

print("Arquivo b.csv gerado com sucesso.", )
