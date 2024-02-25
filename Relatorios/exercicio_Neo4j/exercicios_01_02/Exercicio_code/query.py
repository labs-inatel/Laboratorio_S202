class SocialDatabase:
    def __init__(self, database):
        self.db = database

    # Cria nós usuários com base nos dados fornecidos:
    def createUser(self):
        usuarios = [
            {"nome": "Alice", "idade": 25, "labels": ["Usuario"]},
            {"nome": "Bob", "idade": 30, "labels": ["Usuario"]},
            {"nome": "Charlie", "idade": 35, "labels": ["Usuario"]},
            {"nome": "David", "idade": 40, "labels": ["Usuario"]},
            {"nome": "Eve", "idade": 45, "labels": ["Usuario"]}
        ]

        for usuario in usuarios:
            query = """
            CREATE (u:Usuario {nome: $nome, idade: $idade})
            SET u :%s
            """ % ":".join(usuario["labels"])
            parameters = {
                "nome": usuario["nome"],
                "idade": usuario["idade"]
            }
            self.db.execute_query(query, parameters)

    # Cria nós postagens com base nos dados fornecidos:
    def createPost(self):
        postagens = [
            {"titulo": "Observações do Amanhecer", "conteudo": "Conteúdo da Observações do Amanhecer",
             "labels": ["Postagem"]},
            {"titulo": "Memórias da Tarde", "conteudo": "Conteúdo da Memórias da Tarde", "labels": ["Postagem"]},
            {"titulo": "Segredos da Noite", "conteudo": "Segredos da Noite", "labels": ["Postagem"]}
        ]

        for postagem in postagens:
            query = """
              CREATE (p:Postagem {titulo: $titulo, conteudo: $conteudo})
              SET p :%s
              """ % ":".join(postagem["labels"])
            parameters = {
                "titulo": postagem["titulo"],
                "conteudo": postagem["conteudo"]
            }
            self.db.execute_query(query, parameters)

    # Cria relacionamentos "AMIGO" com base nos dados fornecidos:
    def createFriendship(self):
        relacionamentos = [
            {"amigo1_nome": "Alice", "amigo2_nome": "Bob"},
            {"amigo1_nome": "Bob", "amigo2_nome": "Charlie"},
            {"amigo1_nome": "Charlie", "amigo2_nome": "David"},
            {"amigo1_nome": "David", "amigo2_nome": "Eve"}
        ]

        for relacionamento in relacionamentos:
            query = """
               MATCH (amigo1:Usuario {nome: $amigo1_nome}), (amigo2:Usuario {nome: $amigo2_nome})
               CREATE (amigo1)-[:AMIGO]->(amigo2)
               """
            parameters = {
                "amigo1_nome": relacionamento["amigo1_nome"],
                "amigo2_nome": relacionamento["amigo2_nome"]
            }
            self.db.execute_query(query, parameters)

    # Cria relacionamentos "POSTOU" com base nos dados fornecidos:
    def createPosted(self):
        relacionamentos = [
            {"usuario_nome": "Alice", "titulo": "Observações do Amanhecer"},
            {"usuario_nome": "Bob", "titulo": "Memórias da Tarde"},
            {"usuario_nome": "Charlie", "titulo": "Segredos da Noite"}
        ]

        for relacionamento in relacionamentos:
            query = """
                    MATCH (usuario:Usuario {nome: $usuario_nome}), (postagem:Postagem {titulo: $titulo})
                    CREATE (usuario)-[:POSTOU]->(postagem)
                    """
            parameters = {
                "usuario_nome": relacionamento["usuario_nome"],
                "titulo": relacionamento["titulo"],
            }
            self.db.execute_query(query, parameters)

    # Encontra os amigos de um usuário específico
    def getFriends(self, username):
        query = """
        MATCH (:Usuario {nome: $username})-[:AMIGO]->(amigo:Usuario)
        RETURN amigo.nome AS nome_amigo
        """
        parameters = {"username": username}
        result = self.db.execute_query(query, parameters)
        friends = result[0]["nome_amigo"]
        return friends

    # Encontra o usuário que fez uma postagem específica
    def getUserByPost(self, post):
        query = """
        MATCH (usuario:Usuario)-[:POSTOU]->(:Postagem {titulo: $post})
        RETURN usuario.nome AS nome_usuario
        """
        parameters = {"post": post}
        result = self.db.execute_query(query, parameters)
        user = result[0]["nome_usuario"]
        return user

    # Encontra os usuários com mais de 35 anos que fizeram uma postagem
    def getUserOver35Posted(self):
        query = """
        MATCH (usuario:Usuario)-[:POSTOU]->(:Postagem)
        WHERE usuario.idade > 35
        RETURN usuario.nome AS nome_usuario
        """
        result = self.db.execute_query(query)
        users = [record["nome_usuario"] for record in result]
        return users

    # Encontra o usuário mais velho
    def getOldestUser(self):
        query = """
        MATCH (usuario:Usuario)
        RETURN usuario.nome AS nome_usuario, usuario.idade AS idade
        ORDER BY idade DESC
        LIMIT 1
        """
        result = self.db.execute_query(query)
        user = result[0]
        return user

    # Conta quantos usuários têm mais de 30 anos
    def countUsersOver30(self):
        query = """
        MATCH (usuario:Usuario)
        WHERE usuario.idade > 30
        RETURN COUNT(usuario) AS total
        """
        result = self.db.execute_query(query)
        count = result[0]["total"]
        return count

    # Calcula a média de idade dos usuários
    def calculateAverageAge(self):
        query = """
        MATCH (usuario:Usuario)
        RETURN AVG(usuario.idade) AS media_idade
        """
        result = self.db.execute_query(query)
        average = result[0]["media_idade"]
        return average
