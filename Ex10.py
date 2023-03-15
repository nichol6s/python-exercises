a= int(input("Digite o valor das cartas: "))
valor_cartas = int(a)

if valor_cartas <= 11:
    print("Sem dúvida compre mais uma carta!")
elif valor_cartas > 11 and valor_cartas <= 15:
    print("Há um risco, mas aconselho a comprar mais uma carta")
elif valor_cartas > 15 and valor_cartas <= 20:
    print("Aconselho a parar de jogar!")
elif valor_cartas == 21:
     print("Você já venceu, não precisa comprar mais nada :D")
else:
    print("Você perdeu :( ")


