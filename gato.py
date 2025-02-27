class Animal:
    def __init__(self, nome, especie, data_nascimento, cor, peso, sexo):
        self.nome = nome,
        self.especie = especie,
        self.data_nascimento = data_nascimento,
        self.cor = cor,
        self.peso = peso,
        self.sexo = sexo,

    def apresentar(self):
        print(f'O animal se chama {self.nome}', f'é da espécie: {self.especie}',
            f'nasceu em {self.data_nascimento}', f'e da cor: {self.cor}',
            f'está com o peso:{self.peso} em kgs',
            f'e do sexo {self.sexo}')

class Gato(Animal):
    def __init__(self, nome, especie, data_nascimeto , cor, peso, sexo, raca):
        super().__init__(nome, especie, data_nascimeto, cor, peso, sexo)
        self.raca = raca
        self.saude = True
        self.fome = True
        self.miando = True
        self.dormindo = False

    def apresentar(self):
        print(f'Este é meu gato(a),\n'
            f'nome dele é: {self.nome};\n',
            f'nasceu em {self.data_nascimento};\n',
            f'é da raça: {self.raca}; \n',
            f'e está pesando: {self.peso};\n'
            f'e é do sexo: {self.sexo}.')
    def bem_estar(self):
        if self.saude:
            print(f'O gato está bem e saudável')
        else:
            print(f'O gato está doente e precisar ir ao veterinário!')
    def miar(self):
        if not self.saude or self.fome:
            print(f'O gato está miando!')
        else:
            print(f'Não tem nada de errado com o gato, ele não está miando!')

    def dormir(self):
        if not self.fome:
            self.dormindo = True
            print(f'O gato está dormindo!')
        elif self.dormindo:
            print(f'O gato ja á está dormindo!')
        else:
            print(f'O gato não está dormindo, pois está com fome!')

    def acordar(self):
        if self.dormindo:
            print(f'O gato acordou pois está com fome!')
            self.dormindo = False
            self.fome = True
        else:
            print(f'O gato já está acordado!')

    def brincar(self):
        if not self.fome and not self.dormindo and self.saude:
            print(f'O gato está brincando com seu novelo de lã!')
        else:
            print(f'O gato não está brincando, porque pode estar com fome, dormindo ou doente!')
    def comer(self):
        if self.fome:
            print(f'O gato está comendo')
            self.fome = False
        else:
            print(f'O gato não está com fome!')

gato01 = Gato('Mingau','gato', '27/06/2022', 'preto', '5.00', 'macho','siamês')
gato02 = Gato('Mel','gato', '27/09/2023', 'laranja', '6.00', 'fêmea','persa')
