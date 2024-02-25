from database import Database
from query import SocialDatabase

# Cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j:
db = Database("bolt://54.175.222.248:7687", "neo4j", "cheeks-mixture-equations")
db.drop_all()

# Cria uma instância da classe SocialDatabase para interagir com o banco de dados:
social_db = SocialDatabase(db)


class Social:
    # Função para criar os nós de usuarios:
    @staticmethod
    def criar_usuarios():
        social_db.createUser()

    # Função para criar os nós de postagens:
    @staticmethod
    def criar_postagens():
        social_db.createPost()

    # Função para criar os relacionamentos "AMIGO":
    @staticmethod
    def criar_amizade():
        social_db.createFriendship()

    # Função para criar os relacionamentos "POSTOU":
    @staticmethod
    def criar_postou():
        social_db.createPosted()

    @staticmethod
    def get_Friends(nome):
        friends_bob = social_db.getFriends(nome)
        return friends_bob

    @staticmethod
    def getUserByPost(post):
        postagem = social_db.getUserByPost(post)
        return postagem

    @staticmethod
    def getUsersOver35WhoPosted():
        users_Over35 = social_db.getUserOver35Posted()
        return users_Over35

    @staticmethod
    def findOldestUser():
        oldest = social_db.getOldestUser()
        return oldest

    @staticmethod
    def countUsersOver30():
        users_Over30 = social_db.countUsersOver30()
        return users_Over30

    @staticmethod
    def calculateAverageAge():
        media = social_db.calculateAverageAge()
        return media


# Cria uma instância da Classe Social para realizar as consultas:
social = Social()

# Chama a função para criar nós:
social.criar_usuarios()
social.criar_postagens()

# Chama as funções para criar relacionamentos:
social.criar_amizade()
social.criar_postou()

# Pergunta: Quem é amigo de Bob?
friends_of_bob = social.get_Friends("Bob")
print("Amigos de Bob:", friends_of_bob)

# Pergunta: Quem postou a 'Postagem 2'?
user_of_post = social.getUserByPost("Memórias da Tarde")
print("Usuário da Postagem 2:", user_of_post)

# Pergunta: Quem tem mais de 35 anos e fez uma postagem?
users = social.getUsersOver35WhoPosted()
print("Usuários com mais de 35 anos que fizeram uma postagem:", users)

# Pergunta: Quem é o usuário mais velho?
oldest_user = social.findOldestUser()
print("Usuário mais velho:", oldest_user["nome_usuario"], "- Idade:", oldest_user["idade"])

# Quantos usuários têm mais de 30 anos?
users_over_30 = social.countUsersOver30()
print("Número de usuários com mais de 30 anos:", users_over_30)

# Qual é a média de idade dos usuários?
average_age = social.calculateAverageAge()
print("Média de idade dos usuários:", average_age)
