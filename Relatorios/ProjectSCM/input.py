from crud import CRUD
from database import Database

# Cria uma instância da classe Database, passando os dados de conexão para o banco de dados Neo4j:
db = Database("bolt://3.238.139.67:7687", "neo4j", "art-effects-sheeting")

# Cria uma instância da classe CRUD para interagir com o banco de dados:
crud_db = CRUD(db)


class Input:
    @staticmethod
    # Cadrasta uma nova rede de supermercados:
    def cadastrar_rede():
        nome = input('Digite o nome da rede de supermercados: ')
        endereco = input('Digite o endereço da rede de supermercados: ')
        cnpj = input('Digite o CNPJ da rede de supermercados: ')
        faturamento = input('Digite o valor do faturamento anual: ')
        filiais = int(input('Digite o número de filiais da rede de supermercados: '))
        crud_db.createSupermercado(nome, endereco, cnpj, faturamento, filiais)

    @staticmethod
    # Mostra informações sobre uma rede de supermercados específica:
    def mostrar_informacoes_rede():
        nome_rede = input('Digite o nome da rede de supermercados que deseja visualizar: ')
        supermercado = crud_db.readSupermercado(nome_rede)
        if supermercado:
            print('\nInformações da rede de supermercados:\n')
            print(f"Nome: {supermercado['nome']}")
            print(f"Endereço: {supermercado['endereco']}")
            print(f"Faturamento: {supermercado['faturamento']}")
            print(f"Filiais: {supermercado['filiais']}\n")
        else:
            print('\nRede de supermercados não encontrada.\n')

    @staticmethod
    # Atualiza faturamento anual da rede de supermercados:
    def atualizar_rede():
        nome_rede = input('Digite o nome da rede de supermercados que deseja atualizar: ')
        novo_faturamento = input('Digite o novo valor de faturamento anual: ')
        crud_db.updateSupermercado(nome_rede, novo_faturamento)

    @staticmethod
    # Deleta uma rede de supermercados específica:
    def deletar_rede():
        nome_rede = input('Digite o nome da rede de supermercados que deseja deletar: ')
        crud_db.deleteSupermercado(nome_rede)

    @staticmethod
    # Cadastra um novo fornecedor:
    def cadastrar_fornecedor():
        nome = input('Digite o nome do fornecedor: ')
        produto = input('Digite o produto fornecido: ')
        endereco = input('Digite o endereço do fornecedor: ')
        contato = input('Digite o contato do fornecedor: ')
        crud_db.createFornecedor(nome, produto, endereco, contato)

    @staticmethod
    # Mostra informações sobre um fornecedor específico:
    def mostrar_informacoes_fornecedor():
        nome_fornecedor = input('Digite o nome do fornecedor que deseja visualizar: ')
        fornecedor = crud_db.readFornecedor(nome_fornecedor)
        if fornecedor:
            print('\nInformações do fornecedor:\n')
            print(f"Nome: {fornecedor['nome']}")
            print(f"Produto fornecido: {fornecedor['produto']}")
            print(f"Endereco: {fornecedor['endereco']}")
            print(f"Contato: {fornecedor['contato']}\n")
        else:
            print('\nFornecedor não encontrado.\n')

    @staticmethod
    # Atualiza produto, endereco e contato do fornecedor:
    def atualizar_fornecedor():
        nome_fornecedor = input('Digite o nome do fornecedor que deseja atualizar: ')
        novo_produto = input('Digite o novo produto fornecido: ')
        novo_endereco = input('Digite o novo endereco do fornecedor: ')
        novo_contato = input('Digite o novo contato do fornecedor: ')
        crud_db.updateFornecedor(nome_fornecedor, novo_produto, novo_endereco, novo_contato)

    @staticmethod
    # Deleta um fornecedor específico:
    def deletar_fornecedor():
        nome_fornecedor = input('Digite o nome do fornecedor que deseja deletar: ')
        crud_db.deleteFornecedor(nome_fornecedor)

    @staticmethod
    # Cria o relacionamento FORNECE entre rede de supermercado específica e fornecedor:
    def fornece():
        nome_fornecedor = input('Digite o nome do fornecedor: ')
        nome_rede = input(f'Digite o nome da rede de supermercados onde o fornecedor {nome_fornecedor} será indicado: ')
        crud_db.createFornecimento(nome_rede, nome_fornecedor)

    @staticmethod
    # Cria o relacionamento PARCERIA entre redes de supermercados:
    def parceria_supermercados():
        nome_rede1 = input('Digite o nome da rede de supermercados: ')
        nome_rede2 = input(f'Digite o nome da rede de supermercados que faz parceria com a rede {nome_rede1}: ')
        crud_db.createParceria_Supermercado(nome_rede1, nome_rede2)

    @staticmethod
    # Cria o relacionamento PARCERIA entre fornecedores:
    def parceria_fornecedores():
        nome_fornecedor1 = input('Digite o nome do fornecedor: ')
        nome_fornecedor2 = input(f'Digite o nome do fornecedor faz parceria o fornecedor {nome_fornecedor1}: ')
        crud_db.createParceria_Fornecedor(nome_fornecedor1, nome_fornecedor2)

    @staticmethod
    def sair():
        db.drop_all()
        db.close()
