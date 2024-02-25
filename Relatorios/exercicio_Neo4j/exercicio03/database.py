from neo4j import GraphDatabase


class Database:
    # Initializes the connection to the Neo4j database, using the provided URI, username and password information:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        print("\nDatabase successfully connected!\n")

    # Close the connection to the database:
    def close(self):
        self.driver.close()

    # Run a Cypher query against the database, with the query and given parameters:
    def execute_query(self, query, parameters=None):
        data = []
        with self.driver.session() as session:
            results = session.run(query, parameters)
            for record in results:
                data.append(record)  # Collect query result records

            return data

    # Run a Cypher query to delete all nodes and relationships from the database:
    def drop_all(self):
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")
