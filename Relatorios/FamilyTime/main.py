from database import Database
from query import FamilyDatabase

# Cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j:
db = Database("bolt://3.83.235.5:7687", "neo4j", "carburetors-chases-foreheads")
db.drop_all()

# Cria uma instância da classe FamilyDatabase para interagir com o banco de dados:
family_db = FamilyDatabase(db)


class Family:
    # Função para criar os nós de pessoas:
    @staticmethod
    def criar_nos_pessoas():
        family_db.criar_nos_pessoas()

    # Função para criar os relacionamentos "PAI_DE":
    @staticmethod
    def criar_relacionamentos_pai_de():
        family_db.criar_relacionamentos_pai_de()

    # Função para criar os relacionamentos "ESPOSO_DE":
    @staticmethod
    def criar_relacionamentos_esposo_de():
        family_db.criar_relacionamentos_esposo_de()

    # Função para criar os relacionamentos "AVO_DE":
    @staticmethod
    def criar_relacionamentos_avo_de():
        family_db.criar_relacionamentos_avo_de()

    # Função para criar os relacionamentos "IRMAO_DE":
    @staticmethod
    def criar_relacionamentos_irmao_de():
        family_db.criar_relacionamentos_irmao_de()

    # Função para criar os relacionamentos "SOGRO_DE":
    @staticmethod
    def criar_relacionamentos_sogro_de():
        family_db.criar_relacionamentos_sogro_de()

    # Função para criar os relacionamentos "PRIMO_DE":
    @staticmethod
    def criar_relacionamentos_primo_de():
        family_db.criar_relacionamentos_primo_de()

    # Função para criar os relacionamentos "SOBRINHO_DE":
    @staticmethod
    def criar_relacionamentos_sobrinho_de():
        family_db.criar_relacionamentos_sobrinho_de()

    # Chama o método getSobrinhos da classe FamilyDatabase:
    @staticmethod
    def getSobrinhos(tia_nome):
        # Chama o método get_sobrinhos para obter os nomes dos sobrinhos com base no nome da tia:
        nome_sobrinhos = family_db.get_sobrinhos(tia_nome)
        return nome_sobrinhos

    # Chama o método getFilho da classe FamilyDatabase:
    @staticmethod
    def getFilho(pai_nome, mae_nome):
        # Chama o método get_filho para obter o nome do filho com base nos nomes do pai e da mãe:
        nome_filho = family_db.get_filho(pai_nome, mae_nome)
        return nome_filho

    # Chama o método getNetos da classe FamilyDatabase:
    @staticmethod
    def getNetos(avo_nome):
        # Chama o método get_netos para obter os nomes dos netos com base no nome do avô:
        nome_netos = family_db.get_netos(avo_nome)
        return nome_netos


# Cria uma instância da Classe Family para realizar as consultas:
family = Family()

# Chama a função para criar nós:
family.criar_nos_pessoas()

# Chama as funções para criar relacionamentos:
family.criar_relacionamentos_pai_de()
family.criar_relacionamentos_esposo_de()
family.criar_relacionamentos_avo_de()
family.criar_relacionamentos_irmao_de()
family.criar_relacionamentos_sogro_de()
family.criar_relacionamentos_primo_de()
family.criar_relacionamentos_sobrinho_de()

# Consulta: Quais são os sobrinhos de Wanderlea?
sobrinho = family.getSobrinhos("Wanderlea")
print("Os sobrinhos de Wanderlea são:", sobrinho)

# Consulta: Quem é o filho de Giovani e Isabela?
filho = family.getFilho("Giovani", "Isabela")
print("O filho de Giovani e Isabela é:", filho)

# Consulta: Quais são os netos de Zé Vitor?
neto = family.getNetos("Zé Vitor")
print("Os netos de Zé Vitor são:", neto)
