def fatorial(numero):
  if numero <= 1:
    return 1
  else:
    return numero * fatorial(numero - 1)

numero = int(input("Digite um número: "))

if numero > 64:
  print("O número é muito grande para ser calculado.")
else:
  print("O fatorial de {} é {}".format(numero, fatorial(numero)))
