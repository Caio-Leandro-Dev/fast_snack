hamb = 0
batata = 0
refri = 0

while True:
    print('++++++ MENU ++++++')
    print('1 - Novo pedido')
    print('2 - Consultar pedido')
    print('3 - Sair')

    escolha = input('Escolha uma opção: ')

    if escolha == "1":
        while True:
            print('-------------')
            print('++ MONTAGEM DE PEDIDO ++')
            print('1 - HAMBURGUER')
            print('2 - BATATA FRITA')
            print('3 - REFRIGERANTE')
            print('4 - FINALIZAR PEDIDO')

            opcao = input('Escolha uma opção: ')

            if opcao == "1":
                hamb += 1
                print("Hambúrguer adicionado ao carrinho!")

            elif opcao == "2":
                batata += 1
                print("Batata frita adicionada ao carrinho!")

            elif opcao == "3":
                refri += 1
                print("Refrigerante adicionado ao carrinho!")

            elif opcao == "4":
                print("Pedido finalizado!")
                break

            else:
                print("Opção inválida!")

    elif escolha == "2":
        print('== PEDIDO ATUAL ==')
        print(f'HAMBÚRGUERES: {hamb}')
        print(f'BATATAS FRITAS: {batata}')
        print(f'REFRIGERANTES: {refri}')
        print('-----------------')

    elif escolha == "3":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")
