horas = int(input("Quantas horas voce trabalha por mes? "))
valor = int(input("Quanto voce ganha por hora? "))
desconto = int(input("Qual o seu percentual de desconto? "))

salario_bruto = horas * valor
total_desconto = (salario_bruto * desconto) / 100
salario_liquido = salario_bruto - total_desconto

print("Salário Bruto: R$ ", salario_bruto)
print("Salário liquido: R$ ", salario_liquido) 
print("Total a ser descontado: R$ ", total_desconto)
print()
print("Fim :D")