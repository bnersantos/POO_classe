class Animal:
    def __init__(self, nome, especie, data_nascimento, cor, peso, sexo):
        # __ = privado
        # _ = protegido
        self.__nome = nome,
        self.__especie = especie,
        self.__data_nascimento = data_nascimento,
        self._cor = cor,
        self._peso = peso,
        self._sexo = sexo,

    def get_nome(self):
        return self.__nome
    def get_especie(self):
        return self.__especie
    def get_data_nascimento(self):
        return self.__data_nascimento
    def get_cor(self):
        return self._cor
    def get_peso(self, peso):
        if peso > 0:
            self._peso = peso
        else:
            print(f'O peso deve ser maior que 0')
    def get_sexo(self):
        return self._sexo

    def apresentar(self):
        print(f'O animal se chama {self.__nome}', f'é da espécie: {self.__especie}',
            f'nasceu em {self.__data_nascimento}', f'e da cor: {self._cor}',
            f'está com o peso:{self._peso} em kgs',
            f'e do sexo {self._sexo}')


class Gato(Animal):
    def __init__(self, nome, especie, data_nascimeto , cor, peso, sexo, raca):
        super().__init__(nome, especie, data_nascimeto, cor, peso, sexo)
        self.__raca = raca
        self.saude = True
        self.fome = True
        self.miando = True
        self.dormindo = False

    def apresentar(self):
        print(f'Este é meu gato(a),\n'
            f'nome dele é: {self.get_nome()};\n',
            f'nasceu em {self.get_data_nascimento()};\n',
            f'é da raça: {self.__raca}; \n',
            f'e está pesando: {self.get_peso()};\n'
            f'e é do sexo: {self.get_sexo()}.')
    def set_bem_estar(self):
        if self.saude:
            print(f'O gato está bem e saudável')
        else:
            print(f'O gato está doente e precisar ir ao veterinário!')
    def set_miar(self):
        if not self.saude or self.fome:
            print(f'O gato está miando!')
        else:
            print(f'Não tem nada de errado com o gato, ele não está miando!')

    def set_dormir(self):
        if not self.fome:
            self.dormindo = True
            print(f'O gato está dormindo!')
        elif self.dormindo:
            print(f'O gato ja á está dormindo!')
        else:
            print(f'O gato não está dormindo, pois está com fome!')

    def set_acordar(self):
        if self.dormindo:
            print(f'O gato acordou pois está com fome!')
            self.dormindo = False
            self.fome = True
        else:
            print(f'O gato já está acordado!')

    def set_brincar(self):
        if not self.fome and not self.dormindo and self.saude:
            print(f'O gato está brincando com seu novelo de lã!')
        else:
            print(f'O gato não está brincando, porque pode estar com fome, dormindo ou doente!')
    def set_comer(self):
        if self.fome:
            print(f'O gato está comendo')
            self.fome = False
        else:
            print(f'O gato não está com fome!')

gato01 = Gato('Mingau','gato', '27/06/2022', 'preto', '5.00', 'macho','siamês')
gato02 = Gato('Mel','gato', '27/09/2023', 'laranja', '6.00', 'fêmea','persa')
