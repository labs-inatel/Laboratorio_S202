class Animal:
    def __init__(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som

    def emitir_som(self):
        print("Som do animal: " + self.som)

    def mudar_cor(self, nova_cor):
        print("Cor do animal: " + nova_cor)

class Elefante(Animal):
    def __init__(self, nome, idade, especie, cor, som, tamanho):
        super().__init__(nome, idade, especie, cor, som)
        self.tamanho = tamanho

    def trombar(self, som):
        print("Som do animal: " + som)

    def mudar_tamanho(self, novo_tamanho):
        print("Tamanho do animal: " + novo_tamanho)

nome = input("Digite o nome do animal:")
idade = int(input("Digite a idade do animal:"))
especie = input("Digite o especie do animal:")
cor = input("Digite o cor do animal:")
som = input("Digite o som do animal:")
tamanho10:
        elefante01.mudar_tamanho("pequeno")
        elefante01.trombar("Paaah")
        elefante01.mudar_cor("preto")
    else:
        elefante01.mudar = input("Digite o tamanho do animal:")

elefante01 = Elefante(nome,idade,especie,cor,som,tamanho)

if especie == "Africano":
    print("\nNome do animal:", nome, "\nIdade do animal:", idade, "anos\nEspecie do animal:", especie)
    if idade >= _tamanho("grande")
        elefante01.trombar("PAHHHHHH")
        elefante01.mudar_cor("rosa")
else:
    print("\nNome do animal:", nome, "\nIdade do animal:", idade, "anos\nEspecie do animal:", especie,
          "\nCor do animal:", cor, "\nTamanho do animal:", tamanho)
    print(elefante01.trombar(som))