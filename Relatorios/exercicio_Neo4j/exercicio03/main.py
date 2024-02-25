from database import Database
from crud import TeacherCRUD

# Create an instance of the Database class, passing the connection data to the Neo4j database:
db = Database("bolt://3.89.120.110:7687", "neo4j", "facilitation-receptacles-entrance")
db.drop_all()

# Create an instance of the TeacherCRUD class to interact with the database:
teacher_db = TeacherCRUD(db)

class Teacher:
    # Create teacher:
    @staticmethod
    def createTeachers(name, ano_nasc, cpf):
        teacher_db.create(name, ano_nasc, cpf)

    # Read teacher based on name:
    @staticmethod
    def readTeachers(name):
        getTeacher = teacher_db.read(name)
        return getTeacher

    # Updates teacher's cpf based on name:
    @staticmethod
    def updateTeachers(name, new_cpf):
        teacher_db.update(name, new_cpf)

    # Delete teacher based on name:
    @staticmethod
    def deleteTeachers(name):
        teacher_db.delete(name)


# Create an instance of the Social Class to perform the interactions:
teacher = Teacher()

# Create Teacher "Chris Lima":
teacher.createTeachers("Chris Lima", 1956, "189.052.396-66")

# Read Teacher "Chris Lima":
Match = teacher.readTeachers("Chris Lima")
print("Found teacher info:", Match)

# Update cpf of teacher "Chris Lima":
teacher.updateTeachers("Chris Lima", "162.052.777-77")

# Read Teacher "Chris Lima":
Update = teacher.readTeachers("Chris Lima")
print("Teacher:", Update)

# Delete Teacher "Chris Lima":
teacher.deleteTeachers("Chris Lima")
