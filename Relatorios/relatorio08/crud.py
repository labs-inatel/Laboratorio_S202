class GameDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, name):
        query = "CREATE (:Player {name: $name})"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    def create_match(self, match_name, match_result, match_scores):
        score_list = []
        for score in match_scores:
            player_name, player_score = next(iter(score.items()))
            score_dict = {"player_name": str(player_name), "score": int(player_score)}
            score_list.append(score_dict)

        query1 = "CREATE (:Match {name: $match_name, result: $match_result})"
        parameters1 = {"match_name": match_name, "match_result": match_result}
        self.db.execute_query(query1, parameters1)

        query2 = """
        UNWIND $score_list AS score
        MATCH (p:Player {name: score.player_name})
        MATCH (m:Match {name: $match_name})
        CREATE (p)-[:PLAYED_IN {score: score.score}]->(m)
        """
        parameters2 = {"match_name": match_name, "score_list": score_list}
        self.db.execute_query(query2, parameters2)

    def create_relationship(self, player1_name, player2_name):
        query = """
        MATCH (p1:Player {name: $player1_name})
        MATCH (p2:Player {name: $player2_name})
        CREATE (p1)-[:FRIENDS_WITH]->(p2)
        """
        parameters = {"player1_name": player1_name, "player2_name": player2_name}
        self.db.execute_query(query, parameters)

    def get_players(self):
        query = "MATCH (p:Player) RETURN p.name AS name, p.id AS id"
        results = self.db.execute_query(query)
        return results

    def get_player_history(self, player_name):
        query = """
        MATCH (p:Player {name: $player_name})-[ps:PLAYED_IN]->(m:Match)
        RETURN m.name AS match_name, m.result AS match_result, ps.score AS player_score
        """
        parameters = {"player_name": player_name}
        results = self.db.execute_query(query, parameters)
        return results

    def get_matches(self):
        query = "MATCH (m:Match) RETURN m.name AS name, m.result AS result"
        results = self.db.execute_query(query)
        return results

    def update_player(self, player_name, new_name):
        query = "MATCH (p:Player {name: $player_name}) SET p.name = $new_name"
        parameters = {"player_name": player_name, "new_name": new_name}
        self.db.execute_query(query, parameters)

    def delete_player(self, player_name):
        query = "MATCH (p:Player {name: $player_name}) DETACH DELETE p"
        parameters = {"player_name": player_name}
        self.db.execute_query(query, parameters)
        print(f"Player {player_name} deleted")

    def delete_match(self, match_name):
        query = "MATCH (m:Match {name: $match_name}) DETACH DELETE m"
        parameters = {"match_name": match_name}
        self.db.execute_query(query, parameters)
        print(f"Match {match_name} deleted")
