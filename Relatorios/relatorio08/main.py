from database import Database
from crud import GameDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://44.202.107.164:7687", "neo4j", "film-market-suspect")
db.drop_all()

# Criando uma instância da classe GameDatabase para interagir com o banco de dados
game_db = GameDatabase(db)


class Game:
    # Create players:
    @staticmethod
    def createPlayers(name):
        game_db.create_player(name)

    createPlayers("Luiza")
    createPlayers("Jonas")
    createPlayers("Wilker")
    createPlayers("Pedro")

    # Create matches:
    @staticmethod
    def createMatches(match_name, match_result, match_scores):
        game_db.create_match(match_name, match_result, match_scores)

    # Create match:
    match_scores = [{"Luiza": 10}, {"Jonas": 8}, {"Wilker": 12}, {"Pedro": 9}]

    createMatches("Game", "player 3 win", match_scores)

    @staticmethod
    def getPlayers():
        print("\nPlayers:")
        print(f"{game_db.get_players()}\n")

    # Get list of players:
    getPlayers()

    @staticmethod
    def createRelationships(player1, player2):
        game_db.create_relationship(player1, player2)

    # Create relationships:
    createRelationships("Luiza", "Jonas")
    createRelationships("Luiza", "Wilker")
    createRelationships("Jonas", "Wilker")
    createRelationships("Pedro", "Jonas")

    @staticmethod
    def playerHistory(player):
        history = game_db.get_player_history(player)
        print(f"Player: {player}\nHistory:{history}\n")

    # Get player history
    playerHistory("Luiza")
    playerHistory("Jonas")
    playerHistory("Wilker")
    playerHistory("Pedro")

    @staticmethod
    def getMatches():
        print(game_db.get_matches())

    # Get list of matches
    getMatches()

    @staticmethod
    def updatePlayer(player, new_name):
        game_db.update_player(player, new_name)

    # Update player:
    updatePlayer("Luiza", "Lulu")
    updatePlayer("Jonas", "Jon")
    updatePlayer("Wilker", "Wil")
    updatePlayer("Pedro", "Pedrinho")

    # Get new list of players:
    getPlayers()

    @staticmethod
    def deletePlayer(player):
        game_db.delete_player(player)

    # Delete player:
    deletePlayer("Jon")

    @staticmethod
    def deleteMatch(match):
        game_db.delete_match(match)

    # Delete match:
    deleteMatch("Game")
