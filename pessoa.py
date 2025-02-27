class Pessoa:
    def __init__(self, nome, data_nascimento, codigo,trabalhando = False, estudando = True, salario = 0,):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__codigo = codigo
        self._salario = salario
        self._trabalhando = trabalhando
        self._estudando = estudando

    def get_nome(self):
        return self.__nome
    def get_data_nascimento(self):
        return self.__data_nascimento
    def get_codigo(self):
        return self.__codigo
    def get_salario(self):
        return self._salario
    def get_trabalhando(self):
        return self._trabalhando
    def get_estudando(self):
        return self._estudando
    def set_salario(self, valor):
        if valor >= 0:
            self._salario = valor
        else:
            print(f'Salário inválido!')
    def apresentar(self):
        print (f'<Pessoa: \n'
                f'Meu nome é: ', self.get_nome(), '; \n'
                f'Nasci em: {self.get_data_nascimento()};\n'
                f'Meu código é: {self.get_codigo()};\n.>;')

    def set_(self, valor):
        if valor >= 0:
            self._salario = valor
        else:
            print(f'Salário inválido!')

    def set_estudar(self, status):
        if self.get_estudando() and self.get_trabalhando() and status:
            print(f'Trabalhando e estudando, então recebeu um aumento.')
            self.set_salario(1518 + 200)
            print(f'O salário atual é: {self.get_salario()} ')
        elif self.get_estudando and status:
            print(f'Já está estudando')
        elif self.get_trabalhando and not status:
            print(f'Agora está estudando')
        else:
            print(f'Não está estudando!\n')

    def set_trabalhar(self, status):
        if self.get_trabalhando and status:
            print(f'Já está trabalhando!')
            print(f'salario: {self.get_salario()}')
        elif not self.get_trabalhando and not status:
            print(f'Não está trabalhando!')
        elif not self.get_trabalhando and status:
            self.__trabalhando = status
            self.set_salario(1518)
        else:
            self.set_trabalhar = status
            self.set_salario(0)


p1 = Pessoa('<Abner>', '01/02/2008', '13', estudando = True, trabalhando = False)

p2 = Pessoa('<Bruno>', '27/06/2008', '2', estudando = False, trabalhando = True)


p3 = Pessoa('<Vitor>', '27/09/2007', '29', estudando = False, trabalhando = True)

p4 = Pessoa('<Vinícius>', '26/03/2008', '29', estudando = True, trabalhando = True)

p5 = Pessoa('<Gabriele>', '27/10/2007','8', estudando = True, trabalhando = False)



class Bebe(Pessoa):
    def __init__(self, nome, data_nascimento, codigo):
        super().__init__(nome, data_nascimento, codigo)
        self.fome = True
        self.chorando = True
        self.dormindo = False

    def apresentar(self):
        print(f'<Bebe: {self.nome};\n {self.data_nascimento};\n {self.codigo}.\n>')

        if self.fome:
            print(f'O bebê está com fome!')
        else:
            print(f'O bebê não está com fome!')
        if self.chorando:
            print(f'O bebê está chorando!')
        else:
            print(f'O bebê não está chorando!')
        if self.dormindo:
            print(f'O bebê está dormindo!')
        else:
            print(f'O bebê não está dormindo!')

    def mamar(self):
        if self.fome:
            print('O bebê está mamando!')
            self.fome = False
            self.chorando = False
        else:
            print(f'O bebê não quer mamar')
    def chorar(self):
        if self.fome:
            print(f'O bebê está chorando porque está com fome!')
            self.dormindo = False
        else:
            print(f'Ele está dormindo!')
    def dormir(self):
        if self.fome:
            print(f'O bebê está com fome, então não está dormindo!')
            self.chorando = True
        else:
            print(f'O bebê está dormindo!')
            self.dormindo = True
    def acordar(self):
        if self.dormindo:
            self.fome = True
            self.chorando = True
            print(f'O bebê acordou pois está com fome!')
            self.dormindo = False
        else:
            print(f'O bebê já está acordado!')

bebe01 = Bebe("Bruno","27/06/2023","02")
bebe02 =Bebe("Júlia","22/03/2024", "01")