class FamilyDatabase:
    def __init__(self, database):
        self.db = database

    # Cria nós com base nos dados fornecidos:
    def criar_nos_pessoas(self):
        pessoas = [
            {"nome": "Alessandro", "sexo": "M", "idade": 48, "labels": ["Pessoa", "Desenhista"]},
            {"nome": "Wanderlea", "sexo": "F", "idade": 50, "labels": ["Pessoa", "Montadora"]},
            {"nome": "Ian", "sexo": "M", "idade": 15, "labels": ["Pessoa", "Estudante"]},
            {"nome": "Iza", "sexo": "F", "idade": 20, "labels": ["Pessoa", "Estudante"]},
            {"nome": "Zé Vitor", "sexo": "M", "idade": 74, "labels": ["Pessoa", "Aposentado"]},
            {"nome": "Déti", "sexo": "F", "idade": 65, "labels": ["Pessoa", "Aposentada"]},
            {"nome": "Giovani", "sexo": "M", "idade": 35, "labels": ["Pessoa", "Técnico"]},
            {"nome": "Isabela", "sexo": "F", "idade": 30, "labels": ["Pessoa", "Administrativa"]},
            {"nome": "Gabriel", "sexo": "M", "idade": 11, "labels": ["Pessoa", "Estudante"]},
            {"nome": "Julia", "sexo": "F", "idade": 13, "labels": ["Pessoa", "Estudante"]}
        ]

        for pessoa in pessoas:
            query = """
            CREATE (p:Pessoa {nome: $nome, sexo: $sexo, idade: $idade})
            SET p :%s
            """ % ":".join(pessoa["labels"])
            parameters = {
                "nome": pessoa["nome"],
                "sexo": pessoa["sexo"],
                "idade": pessoa["idade"]
            }
            self.db.execute_query(query, parameters)

    # Cria relacionamentos "PAI_DE" com base nos dados fornecidos:
    def criar_relacionamentos_pai_de(self):
        relacionamentos = [
            {"pai_nome": "Alessandro", "filho_nome": "Ian"},
            {"pai_nome": "Alessandro", "filho_nome": "Iza"},
            {"pai_nome": "Wanderlea", "filho_nome": "Ian"},
            {"pai_nome": "Wanderlea", "filho_nome": "Iza"},
            {"pai_nome": "Zé Vitor", "filho_nome": "Wanderlea"},
            {"pai_nome": "Déti", "filho_nome": "Wanderlea"},
            {"pai_nome": "Giovani", "filho_nome": "Julia"},
            {"pai_nome": "Isabela", "filho_nome": "Julia"}
        ]

        for relacionamento in relacionamentos:
            query = """
               MATCH (pai:Pessoa {nome: $pai_nome}), (filho:Pessoa {nome: $filho_nome})
               CREATE (pai)-[:PAI_DE]->(filho)
               """
            parameters = {
                "pai_nome": relacionamento["pai_nome"],
                "filho_nome": relacionamento["filho_nome"]
            }
            self.db.execute_query(query, parameters)

    # Cria relacionamentos "ESPOSO_DE" com base nos dados fornecidos:
    def criar_relacionamentos_esposo_de(self):
        relacionamentos = [
            {"marido_nome": "Alessandro", "esposa_nome": "Wanderlea", "data_casamento": "1999-08-20"},
            {"marido_nome": "Zé Vitor", "esposa_nome": "Déti", "data_casamento": "1965-05-15"},
            {"marido_nome": "Giovani", "esposa_nome": "Isabela", "data_casamento": "2003-03-10"}
        ]

        for relacionamento in relacionamentos:
            query = """
                    MATCH (marido:Pessoa {nome: $marido_nome}), (esposa:Pessoa {nome: $esposa_nome})
                    CREATE (marido)-[:ESPOSO_DE {data_casamento: $data_casamento}]->(esposa)
                    """
            parameters = {
                "marido_nome": relacionamento["marido_nome"],
                "esposa_nome": relacionamento["esposa_nome"],
                "data_casamento": relacionamento["data_casamento"]
            }
            self.db.execute_query(query, parameters)

    # Cria relacionamentos "AVO_DE" com base nos dados fornecidos:
    def criar_relacionamentos_avo_de(self):
        relacionamentos = [
            {"avo_nome": "Déti", "neto_nome": "Gabriel"},
            {"avo_nome": "Zé Vitor", "neto_nome": "Gabriel"},
            {"avo_nome": "Zé Vitor", "neto_nome": "Ian"},
            {"avo_nome": "Déti", "neto_nome": "Ian"},
            {"avo_nome": "Zé Vitor", "neto_nome": "Iza"},
            {"avo_nome": "Déti", "neto_nome": "Iza"}
        ]

        for relacionamento in relacionamentos:
            query = """
                MATCH (avo:Pessoa {nome: $avo_nome}), (neto:Pessoa {nome: $neto_nome})
                CREATE (avo)-[:AVO_DE]->(neto)
                """
            parameters = {
                "avo_nome": relacionamento["avo_nome"],
                "neto_nome": relacionamento["neto_nome"]
            }
            self.db.execute_query(query, parameters)

    # Cria relacionamentos "IRMAO_DE" com base nos dados fornecidos:
    def criar_relacionamentos_irmao_de(self):
        relacionamentos = [
            {"irmao1_nome": "Ian", "irmao2_nome": "Iza"},
            {"irmao1_nome": "Alessandro", "irmao2_nome": "Giovani"}
        ]

        for relacionamento in relacionamentos:
            query = """
                MATCH (irmao1:Pessoa {nome: $irmao1_nome}), (irmao2:Pessoa {nome: $irmao2_nome})
                CREATE (irmao1)-[:IRMAO_DE]->(irmao2)
                """
            parameters = {
                "irmao1_nome": relacionamento["irmao1_nome"],
                "irmao2_nome": relacionamento["irmao2_nome"]
            }
            self.db.execute_query(query, parameters)

    # Cria relacionamentos "SOGRO_DE" com base nos dados fornecidos:
    def criar_relacionamentos_sogro_de(self):
        relacionamentos = [
            {"sogro_nome": "Zé Vitor", "genro_nora_nome": "Alessandro"},
            {"sogro_nome": "Déti", "genro_nora_nome": "Alessandro"}
        ]

        for relacionamento in relacionamentos:
            query = """
               MATCH (sogro:Pessoa {nome: $sogro_nome}), (genro_nora:Pessoa {nome: $genro_nora_nome})
               CREATE (sogro)-[:SOGRO_DE]->(genro_nora)
               """
            parameters = {
                "sogro_nome": relacionamento["sogro_nome"],
                "genro_nora_nome": relacionamento["genro_nora_nome"]
            }
            self.db.execute_query(query, parameters)

    # Cria relacionamentos "PRIMO_DE" com base nos dados fornecidos:
    def criar_relacionamentos_primo_de(self):
        relacionamentos = [
            {"primo_nome": "Gabriel", "prima_nome": "Ian"},
            {"primo_nome": "Julia", "prima_nome": "Ian"},
            {"primo_nome": "Gabriel", "prima_nome": "Iza"},
            {"primo_nome": "Julia", "prima_nome": "Iza"}
        ]

        for relacionamento in relacionamentos:
            query = """
                MATCH (primo:Pessoa {nome: $primo_nome}), (prima:Pessoa {nome: $prima_nome})
                CREATE (primo)-[:PRIMO_DE]->(prima)
                """
            parameters = {
                "primo_nome": relacionamento["primo_nome"],
                "prima_nome": relacionamento["prima_nome"]
            }
            self.db.execute_query(query, parameters)

    # Cria relacionamentos "SOBRINHO_DE" com base nos dados fornecidos:
    def criar_relacionamentos_sobrinho_de(self):
        relacionamentos = [
            {"sobrinho_nome": "Gabriel", "tio_nome": "Alessandro"},
            {"sobrinho_nome": "Julia", "tio_nome": "Alessandro"},
            {"sobrinho_nome": "Gabriel", "tio_nome": "Wanderlea"},
            {"sobrinho_nome": "Julia", "tio_nome": "Wanderlea"},
            {"sobrinho_nome": "Ian", "tio_nome": "Giovani"},
            {"sobrinho_nome": "Iza", "tio_nome": "Giovani"}
        ]

        for relacionamento in relacionamentos:
            query = """
               MATCH (sobrinho:Pessoa {nome: $sobrinho_nome}), (tio:Pessoa {nome: $tio_nome})
               CREATE (sobrinho)-[:SOBRINHO_DE]->(tio)
               """
            parameters = {
                "sobrinho_nome": relacionamento["sobrinho_nome"],
                "tio_nome": relacionamento["tio_nome"]
            }
            self.db.execute_query(query, parameters)

    # Consulta os sobrinhos com base no nome da tia:
    def get_sobrinhos(self, tia_nome):
        query = """
             MATCH (tia:Pessoa {nome: $tia_nome})<-[:SOBRINHO_DE]-(sobrinho:Pessoa)
             RETURN sobrinho.nome AS nome
             """
        parameters = {"tia_nome": tia_nome}
        results = self.db.execute_query(query, parameters)
        return results

    # Consulta os filhos com base nos nomes do pai e da mãe:
    def get_filho(self, pai_nome, mae_nome):
        query = """
        MATCH (pai:Pessoa {nome: $pai_nome})-[:ESPOSO_DE]->(mae:Pessoa {nome: $mae_nome})
        MATCH (pai)-[:PAI_DE]->(filho:Pessoa)
        RETURN filho.nome AS nome
        """
        parameters = {"pai_nome": pai_nome, "mae_nome": mae_nome}
        results = self.db.execute_query(query, parameters)
        return results

    # Consulta os netos com base no nome do avô:
    def get_netos(self, avo_nome):
        query = """
            MATCH (avo:Pessoa {nome: $avo_nome})-[:AVO_DE]->(neto:Pessoa)
            RETURN neto.nome AS nome
            """
        parameters = {"avo_nome": avo_nome}
        results = self.db.execute_query(query, parameters)
        return results
