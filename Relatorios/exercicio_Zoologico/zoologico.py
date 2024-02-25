from bson import ObjectId


class Animal:
    # Classe que representa a entidade Animal
    def __init__(self, id=None, nome=None, especie=None, idade=None, habitat=None):
        self.id = str(ObjectId())
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.habitat = habitat

class Cuidador:
    # Classe que representa a entidade Cuidador
    def __init__(self, id=None, nome=None, documento=None):
        self.id = str(ObjectId())
        self.nome = nome
        self.documento = documento

class Habitat:
    # Classe que representa a entidade Habitat
    def __init__(self, id=None, nome=None, tipoAmbiente=None, cuidador=None):
        self.id = str(ObjectId())
        self.nome = nome
        self.tipoAmbiente = tipoAmbiente
        self.cuidador = cuidador
