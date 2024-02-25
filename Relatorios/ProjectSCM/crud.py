class CRUD:
    def __init__(self, database):
        self.db = database

    # Cria um supermercado:
    def createSupermercado(self, nome, endereco, cnpj, faturamento, filiais):
        query = "CREATE (:Supermercado {nome: $nome, endereco: $endereco, cnpj: $cnpj, " \
                "faturamento: $faturamento, filiais: $filiais})"
        parameters = {"nome": nome, "endereco": endereco, "cnpj": cnpj, "faturamento": faturamento, "filiais": filiais}
        self.db.execute_query(query, parameters)
        print("\nSupermercado criado com sucesso!\n")

    # Lê um supermercado com base no nome:
    def readSupermercado(self, nome):
        query = "MATCH (s:Supermercado {nome: $nome}) RETURN s.nome AS nome, s.endereco AS endereco, " \
                "s.cnpj AS cnpj, s.faturamento AS faturamento, s.filiais AS filiais"
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        if results:
            supermercado = results[0]
            return supermercado
        else:
            return None

    # Atualiza o faturamento anual do supermercado com base no nome:
    def updateSupermercado(self, nome, new_faturamento):
        query = "MATCH (s:Supermercado {nome: $nome}) SET s.faturamento = $new_faturamento"
        parameters = {"nome": nome, "new_faturamento": new_faturamento}
        self.db.execute_query(query, parameters)
        print("\nInformações atualizadas com sucesso!\n")

    # Deleta um supermercado com base no nome:
    def deleteSupermercado(self, nome):
        query = "MATCH (s:Supermercado {nome: $nome}) DETACH DELETE s"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)
        print(f"\nSupermercado {nome} deletado!\n")

    # Cria um fornecedor:
    def createFornecedor(self, nome, produto, endereco, contato):
        query = "CREATE (:Fornecedor {nome: $nome, produto: $produto, endereco: $endereco, contato: $contato})"
        parameters = {"nome": nome, "produto": produto, "endereco": endereco, "contato": contato}
        self.db.execute_query(query, parameters)
        print("\nFornecedor criado com sucesso!\n")

    # Lê um fornecedor com base no nome:
    def readFornecedor(self, nome):
        query = "MATCH (f:Fornecedor {nome: $nome}) RETURN f.nome AS nome, f.produto AS produto," \
                " f.endereco AS endereco, f.contato AS contato"
        parameters = {"nome": nome}
        results = self.db.execute_query(query, parameters)
        if results:
            fornecedor = results[0]
            return fornecedor
        else:
            return None

    # Atualiza o produto, endereço e contato do fornecedor com base no nome:
    def updateFornecedor(self, nome, new_produto, new_endereco, new_contato):
        query = "MATCH (f:Fornecedor {nome: $nome}) SET f.produto = $new_produto, f.endereco = $new_endereco," \
                " f.contato = $new_contato"
        parameters = {"nome": nome, "new_produto": new_produto, "new_endereco": new_endereco,
                      "new_contato": new_contato}
        self.db.execute_query(query, parameters)
        print("\nInformações atualizadas com sucesso!\n")

    # Deleta um fornecedor com base no nome:
    def deleteFornecedor(self, nome):
        query = "MATCH (f:Fornecedor {nome: $nome}) DETACH DELETE f"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)
        print(f"\nFornecedor {nome} deletado!\n")

    # Cria o relacionamento FORNECE entre a rede de supermercados e fornecedor:
    def createFornecimento(self, nome_supermercado, nome_fornecedor):
        query = "MATCH (f:Fornecedor {nome: $nome_fornecedor}), (s:Supermercado {nome: $nome_supermercado})" \
                "CREATE (f)-[:FORNECE]->(s)"
        parameters = {"nome_supermercado": nome_supermercado, "nome_fornecedor": nome_fornecedor}
        self.db.execute_query(query, parameters)
        print(f"\n{nome_fornecedor} está fornecendo produtos para a rede de supermercados {nome_supermercado}!\n")

    # Cria o relacionamento PARCERIA entre as redes de supermercados:
    def createParceria_Supermercado(self, nome_rede1, nome_rede2):
        query = "MATCH (r1:Supermercado {nome: $nome_rede1}), (r2:Supermercado {nome: $nome_rede2}) " \
                "CREATE (r1)-[:PARCERIA]->(r2)"
        parameters = {"nome_rede1": nome_rede1, "nome_rede2": nome_rede2}
        self.db.execute_query(query, parameters)
        print(f"\n{nome_rede1} está realizando uma parceria com a rede de supermercados {nome_rede2}!\n")

    # Cria o relacionamento PARCERIA entre os fornecedores:
    def createParceria_Fornecedor(self, nome_fornecedor1, nome_fornecedor2):
        query = "MATCH (f1:Fornecedor {nome: $nome_fornecedor1}), (f2:Fornecedor {nome: $nome_fornecedor2}) " \
                "CREATE (f1)-[:PARCERIA]->(f2)"
        parameters = {"nome_fornecedor1": nome_fornecedor1, "nome_fornecedor2": nome_fornecedor2}
        self.db.execute_query(query, parameters)
        print(f"\n{nome_fornecedor1} está realizando uma parceria com o fornecedor {nome_fornecedor2}!\n")
