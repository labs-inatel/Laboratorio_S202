from bson import ObjectId
from database import Database
from zoologico import Animal, Cuidador, Habitat
from zoologicoDao import ZoologicoDAO


class ZoologicoCLI:
    # Classe que representa a interface de linha de comando para gerenciar o zoológico
    def __init__(self):
        self.database = Database("zoologico", "animais")
        self.zoologico_dao = ZoologicoDAO(self.database)

    def menu(self):
        while True:
            # Método para exibir o menu de opções
            print("\nMenu de interação com o Zoologico:")
            print("1 - Criar Animal")
            print("2 - Ler Animal")
            print("3 - Atualizar Animal")
            print("4 - Deletar Animal")
            print("0 - Sair")

            opcao = int(input("\nDigite o número respectivo a opção desejada: "))
            zooDao = self.zoologico_dao

            if opcao == 1:
                animal = self.create_Animal()
                if animal:
                    zooDao.createAnimal(animal)
                    print("Animal criado com sucesso!")

            elif opcao == 2:
                id = input("Digite o ID do animal: ")
                animal = zooDao.readAnimal(id)
                if animal:
                    print(animal)
                    print("Animal encontrado com sucesso!")
                else:
                    print("Animal não encontrado.")

            elif opcao == 3:
                result = self.update_Animal()
                zooDao.updateAnimal(result)
                print("Animal atualizado com sucesso!")

            elif opcao == 4:
                id = input("Digite o ID do animal: ")
                animal = zooDao.readAnimal(id)
                if animal:
                    print(animal)
                    zooDao.deleteAnimal(id)
                    print("Animal deletado com sucesso!")
                else:
                    print("Animal não encontrado.")

            elif opcao == 0:
                self.database.disconnect()
                print("Saindo...")
                break
            else:
                print("Opção inválida. Tente novamente.")

    def create_Animal(self):
        # Método input para criar um novo animal:
        nome = input("Digite o nome do animal: ")
        especie = input("Digite a espécie do animal: ")
        idade = int(input("Digite a idade do animal: "))
        habitat = self.createHabitat()

        animal = Animal(str(ObjectId()), nome, especie, idade, habitat)
        animal.habitat.id = str(ObjectId())
        animal.habitat.cuidador.id = str(ObjectId())
        return animal

    def createCuidador(self):
        # Método input para criar um novo cuidador:
        nome = input("Digite o nome do cuidador: ")
        documento = input("Digite o documento do cuidador: ")

        cuidador = Cuidador(str(ObjectId()), nome, documento)
        return cuidador

    def createHabitat(self):
        # Método input para criar um novo habitat:
        nome = input("Digite o nome do habitat: ")
        tipoAmbiente = input("Digite o tipo de ambiente: ")
        cuidador = self.createCuidador()

        habitat = Habitat(str(ObjectId()), nome, tipoAmbiente, cuidador)
        return habitat

    def update_Animal(self):
        animal_id = input("Digite o ID do animal a ser atualizado: ")

        # obtém o animal existente do banco de dados
        animal = self.zoologico_dao.readAnimal(animal_id)
        if animal is None:
            print(f"Não foi possível encontrar um animal com o ID {animal_id}")
            return None

        # Método input para atualizar dados do animal:
        nome = input("Digite o nome do animal: ")
        especie = input("Digite a espécie do animal: ")
        idade = int(input("Digite a idade do animal: "))
        habitat = self.updateHabitat()

        up_animal = Animal(animal, nome, especie, idade, habitat)
        return up_animal

    def updateCuidador(self):
        cuidador_id = input("Digite o ID do cuidador a ser atualizado: ")

        # obtém o cuidador existente do banco de dados
        cuidador = self.zoologico_dao.readAnimal(cuidador_id)
        if cuidador is None:
            print(f"Não foi possível encontrar um cuidador com o ID {cuidador_id}")
            return None

        # Método input para atualizar dados do cuidador:
        nome = input("Digite o nome do novo cuidador: ")
        documento = input("Digite o documento do novo cuidador: ")

        up_cuidador = Cuidador(cuidador, nome, documento)
        return up_cuidador

    def updateHabitat(self):
        habitat_id = input("Digite o ID do habitat a ser atualizado: ")

        # obtém o habitat existente do banco de dados
        habitat = self.zoologico_dao.readAnimal(habitat_id)
        if habitat is None:
            print(f"Não foi possível encontrar um habitat com o ID {habitat_id}")
            return None

        # Método input para atualizar dados do habitat:
        nome = input("Digite o nome do animal: ")
        tipoAmbiente = input("Digite a espécie do animal: ")
        cuidador = self.updateCuidador()

        up_habitat = Habitat(habitat, nome, tipoAmbiente, cuidador)
        return up_habitat


zoologico_cli = ZoologicoCLI()
zoologico_cli.menu()
