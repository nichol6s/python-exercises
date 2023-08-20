def fibonacci(numero):
  if numero == 0:
    return 0
  elif numero == 1:
    return 1
  else:
    return fibonacci(numero - 1) + fibonacci(numero - 2)

numero = int(input("Digite um número entre 1 e 100: "))

if numero > 100:
  print("O número é muito grande.")
else:
  print("A sequência de Fibonacci é:")
  for i in range(numero):
    print(fibonacci(i))
