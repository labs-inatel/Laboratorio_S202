from input import Input


class Menu:
    @staticmethod
    # Menu de interação:
    def menu():
        while True:
            print('---------- MENU ----------')
            print('1. Cadastrar rede de supermercados')
            print('2. Mostrar informações de uma rede de supermercados')
            print('3. Atualizar rede de supermercados')
            print('4. Deletar rede de supermercados')
            print('5. Cadastrar fornecedor')
            print('6. Mostrar informações de um fornecedor')
            print('7. Atualizar fornecedor')
            print('8. Deletar fornecedor')
            print('9. Indicar fornecedor para rede de supermercados específica')
            print('10. Criar uma parceria enre redes de supermercados específicas')
            print('11. Criar uma parceria entre fornecedores específicos')
            print('0. Sair\n')

            opcao = input('Digite a opção desejada: ')
            if opcao == '1':
                Input.cadastrar_rede()
            elif opcao == '2':
                Input.mostrar_informacoes_rede()
            elif opcao == '3':
                Input.atualizar_rede()
            elif opcao == '4':
                Input.deletar_rede()
            elif opcao == '5':
                Input.cadastrar_fornecedor()
            elif opcao == '6':
                Input.mostrar_informacoes_fornecedor()
            elif opcao == '7':
                Input.atualizar_fornecedor()
            elif opcao == '8':
                Input.deletar_fornecedor()
            elif opcao == '9':
                Input.fornece()
            elif opcao == '10':
                Input.parceria_supermercados()
            elif opcao == '11':
                Input.parceria_fornecedores()
            elif opcao == '0':
                print('Encerrando o programa...')
                Input.sair()
                break
            else:
                print('Opção inválida. Tente novamente.')


# Iniciando o menu:
menu = Menu()
menu.menu()
