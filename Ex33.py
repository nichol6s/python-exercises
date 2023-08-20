carros = []

while True:
    print("Menu Principal:")
    print("(C) Cadastrar")
    print("(L) Listar")
    print("(P) Procurar")
    print("(S) Sair")
    opcao = input("Digite a sua opção: ").upper()[0]

    if opcao == "C":
        marca = input("Digite a marca: ")
        modelo = input("Digite o modelo: ")
        ano = int(input("Digite o ano: "))
        placa = input("Digite a placa: ")
        cadastro = {"Marca": marca, "Modelo": modelo, "Ano": ano, "Placa": placa} 
        carros.append(cadastro)
        print("Carro cadastrado com sucesso!")
        print()
    elif opcao == "L":
        print("{:<40}{:^10}{:>30}{:>40}".format("Marca", "Modelo", "Ano", "Placa"))
        for carro in carros:
            print("{:<40}{:^10}{:>30}{:>40}".format(carro["Marca"], carro["Modelo"], carro["Ano"], carro["Placa"]))
        print("\n"*3)

    elif opcao == "P":
        placa_busca = input("Digite a placa do carro: ")
        for carro in carros:
            if placa == placa_busca:
                    print()
                    print("Carro encontrado! escolha uma opção")
                    print("(A) Alterar")
                    print("(X) Excluir")
                    print("(R) Retornar ao menu principal")
                    opcao_submenu = input("Digite a sua opção: ").upper()[0]

                    if opcao_submenu == "A":
                        marca = input("Digite a nova marca: ")
                        modelo = input("Digite o novo modelo: ")
                        ano = int(input("Digite o novo ano: "))
                        placa = input("Digite a nova placa: ")
                        print("Carro alterado com sucesso!")

                    elif opcao_submenu == "X":
                        carros.remove(carro)
                        print("Carro excluído com sucesso!")

                    elif opcao_submenu == "R":
                        break
            
    elif opcao == "S":
        print("Encerrando o programa...")
        break

