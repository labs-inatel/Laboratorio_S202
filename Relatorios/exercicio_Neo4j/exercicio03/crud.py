class TeacherCRUD:

    def __init__(self, database):
        self.db = database

    # Create Teacher:
    def create(self, name, ano_nasc, cpf):
        query = "CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)
        print("Successfully created teacher!\n")

    # Read Teacher based on name:
    def read(self, name):
        query = "MATCH (t:Teacher {name: $name}) RETURN t.name AS nome_teacher, t.ano_nasc AS ano_nasc, t.cpf AS cpf"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        teacher = results[0]["nome_teacher"], results[0]["ano_nasc"], results[0]["cpf"]
        return teacher

    # Updates teacher's cpf based on name:
    def update(self, name, new_cpf):
        query = "MATCH (t:Teacher {name: $name}) SET t.cpf = $new_cpf"
        parameters = {"name": name, "new_cpf": new_cpf}
        self.db.execute_query(query, parameters)
        print("\nSuccessfully updated teacher!\n")

    # Delete Teacher based on name:
    def delete(self, name):
        query = "MATCH (t:Teacher {name: $name}) DETACH DELETE t"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
        print(f"\nTeacher {name} deleted!")
