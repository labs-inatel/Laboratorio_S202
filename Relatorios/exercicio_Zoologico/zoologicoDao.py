from bson.objectid import ObjectId
from zoologico import Animal


class ZoologicoDAO:
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def createAnimal(self, animal: Animal) -> str:
        try:
            habitat_id = ObjectId()
            cuidador_id = ObjectId()

            animal_doc = {
                "nome": animal.nome,
                "especie": animal.especie,
                "idade": animal.idade,
                "habitat": [{
                    "id": habitat_id,
                    "nome": animal.habitat.nome,
                    "tipoAmbiente:": animal.habitat.tipoAmbiente,
                    "cuidador": [{
                        "id": cuidador_id,
                        "nome": animal.habitat.cuidador.nome,
                        "documento": animal.habitat.cuidador.documento
                    }]
                }]
            }
            result = self.collection.insert_one(animal_doc)
            animal_doc['id'] = result.inserted_id
            animal_doc['habitat'][0]['id'] = habitat_id
            animal_doc['habitat'][0]['cuidador'][0]['id'] = cuidador_id
            print(f"Animal created with id: {animal.id}")
            return animal.id
        except Exception as error:
            print(f"An error occurred while creating animal: {error}")

    def readAnimal(self, id: str) -> dict:
        try:
            animal = self.collection.find_one({"_id": ObjectId(id)})
            if animal:
                print(f"Animal found: {animal}")
                return animal
            else:
                print(f"No animal found with id {id}")
        except Exception as error:
            print(f"An error occurred while reading animal: {error}")

    def updateAnimal(self, animal: Animal) -> str:
        try:
            animal_doc = {
                "nome": animal.nome,
                "especie": animal.especie,
                "idade": animal.idade,
                "habitat": [{
                    "id": animal.habitat.id,
                    "nome": animal.habitat.nome,
                    "tipoAmbiente:": animal.habitat.tipoAmbiente,
                    "cuidador": [{
                        "id": animal.habitat.cuidador.id,
                        "nome": animal.habitat.cuidador.nome,
                        "documento": animal.habitat.cuidador.documento
                    }]
                }]
            }
            result = self.collection.update_one({"_id": ObjectId(animal.id)}, {"$set": animal_doc})
            if result.modified_count:
                print(f"Animal {animal.id} updated with name {animal.nome}, especie {animal.especie}, "
                      f"age {animal.idade} and habitat {animal.habitat}")
            else:
                print(f"No animal found with id {animal.id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating animal: {error}")

    def deleteAnimal(self, id: str) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(id)})
            if result.deleted_count:
                print(f"Animal {id} deleted")
            else:
                print(f"No animal found with id {id}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting book: {error}")
