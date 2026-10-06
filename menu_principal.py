while True:
    escolha="0"
    opcao="0"
    hamb= 0
    batata= 0
    refri= 0
    
    if escolha == "0": 
          print('++++++MENU++++++')
          print('1-novo pedido')
          print('2-consultar pedido')
          print('3-sair')
          escolha = input('escolha uma opção: ')

          
          if escolha == "1":
            print('-------------')
            print('++MONTAGEM DE PEDIDO++')
            print('1-HAMBURGUER')
            print('2-BATATA FRITA')
            print('3-REFRIGERANTE')       
            print('4-FINALIZAR PEDIDO')
            opcao = input('escolha uma opção: ')
            if opcao == "1":
                 print("Hamburguer adicionado ao carrinho")
                 hamb= (hamb) + 1              
                 opcao = input('escolha uma opção: ')

            if opcao == "2":
                 print("Batata Frita adicionado ao carrinho")
                 batata= (batata)+1
                 opcao = input('escolha uma opção: ')

            if opcao == "3":
                 print("Refrigerante adicionado ao carrinho")
                 refri= (refri)+1
                 opcao = input('escolha uma opção: ')

            if opcao == "4":
                 print("Montagem Adicionado")
                 escolha="0"

                                 
    if escolha == "2": 
          print('== PEDIDO ATUAL ==')
          print (f'HAMBURGUERES: {hamb}')
          print (f'BATATAS FRITAS: {batata}')
          print (f'REFRIGERANTES: {refri}')

          print('-----------------')
          print('++++++MENU++++++')
          print('1-novo pedido')
          print('2-consultar pedido')
          print('3-sair')
          escolha = input('escolha uma opção: ')