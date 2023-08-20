def calcular_media(notas):
  """
  Calcula a média de uma lista de notas.

  Args:
    notas: Uma lista de notas.

  Returns:
    Uma float com a média das notas.
  """
  media = sum(notas) / len(notas)
  return media

def main():
  """
  O programa principal.
  """
  print("Bem-vindo ao programa de cálculo de médias!")

  opcao = input("Escolha uma opção: (B)imestre, (A)no ou (C)urso: ").upper()

  if opcao == "B":
    notas = []
    for i in range(3):
      nota = float(input("Digite a nota da avaliação {}: ".format(i + 1)))
      notas.append(nota)

    media = calcular_media(notas)
    print("A média do bimestre é {}.".format(media))

  elif opcao == "A":
    notas = []
    for i in range(4):
      nota = float(input("Digite a nota do bimestre {}: ".format(i + 1)))
      notas.append(nota)

    media = calcular_media(notas)
    print("A média do ano é {}.".format(media))

  elif opcao == "C":
    notas = []
    for i in range(2):
      nota = float(input("Digite a nota final da disciplina {}: ".format(i + 1)))
      notas.append(nota)

    media = calcular_media(notas)
    print("A média final da disciplina é {}.".format(media))

  else:
    print("Opção inválida.")

if __name__ == "__main__":
  main()
