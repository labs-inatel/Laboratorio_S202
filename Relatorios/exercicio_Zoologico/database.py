import pymongo

class Database:
    def __init__(self, database, collection):
        self.collection = collection
        self.db = None
        self.clusterConnection = None
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "mongodb+srv://testeBD2:bOCXyW1lEFtqN0z6@zoologico.vzaocau.mongodb.net/test"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Database connected successfully!")
        except Exception as e:
            print(e)

    def disconnect(self):
        # Método para se desconectar do banco de dados
        try:
            self.db.close()
            print("Database disconnected successfully!")
        except Exception as e:
            print(f"An error occurred while disconnected Database", e)
