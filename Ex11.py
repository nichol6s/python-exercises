jogador1 = int(input("Digite o número de blocos empilhados pelo jogador 1: "))
jogador2 = int(input("Digite o número de blocos empilhados pelo jogador 2: "))
jogador3 = int(input("Digite o número de blocos empilhados pelo jogador 3: "))

if jogador1 > jogador2 and jogador3:
    print("Jogador 1 venceu!")
elif jogador2 > jogador1 and jogador3:
    print("Jogador 2 venceu!")
elif jogador3 > jogador1 and jogador2:
    print("Jogador 3 venceu!")
else:
    print("Houve um empate entre os primeiros jogadores.")

if jogador1 == jogador2 and jogador3 != jogador3:
    print("Houve um empate entre os jogadores 1 e 2.")
elif jogador1 == jogador3 and jogador1 != jogador2:
    print("Houve um empate entre os jogadores 1 e 3.")
elif jogador2 == jogador3 and jogador2 != jogador1:
    print("Houve um empate entre os jogadores 2 e 3.")
elif jogador1 == jogador2 and jogador1 == jogador3:
    print("Houve um empate entre todos os jogadores.")
else:
    print("Não houve empate.")