class Animal:
    def __init__(self, nome, raca, data_nascimento, cor, peso, porte, sexo):
        self.nome = nome,
        self.raca = raca,
        self.data_nascimento = data_nascimento,
        self.cor = cor,
        self.peso = peso,
        self.porte = porte,
        self.sexo = sexo,

    def apresentar(self):
        print(f'O animal se chama {self.nome}', f'é da raça: {self.raca}',
            f'nasceu em {self.data_nascimento}', f'e da cor: {self.cor}',
            f'está com o peso:{self.peso} em kgs',
            f'é do porte: {self.porte}', f'e do sexo {self.sexo}')

class Gato(Animal):
    def __init__(self, nome, raca, data_nascimeto , cor, peso, sexo):
        super().__init__(nome, raca, data_nascimeto, cor, peso, sexo)
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
            print(f'O gata está dormindo!')
        else:
            print(f'O gato não está dormindo, pois está com fome!')

    def acordar(self):
        if self.dormindo:
            self.fome = True
            print(f'O gato acordou pois está com fome!')
            self.dormindo = False
        else:
            print(f'O gato já está acordado!')

    def brincar(self):
        if not self.fome and not self.dormindo and self.saude:
            print(f'O gato está brincando com seu novelo de lã!')
        else:
            print(f'O gato não está brincando, porque pode estar com fome, dormindo ou doente!')

gato01 = Gato('Mingau','siamês', '27/06/2022', 'preto', '5.00', 'macho')
gato02 = Gato('Mel','persa', '27/09/2023', 'laranja', '6.00', 'fêmea')
