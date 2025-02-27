class Pessoa:
    def __init__(self, nome, data_nascimento, codigo,trabalhando = False, estudando = True, salario = 0,):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.codigo = codigo
        self.salario = salario
        self.trabalhando = trabalhando
        self.estudando = estudando



    def apresentar(self):
        print (f'<Pessoa: \n'
                f'Meu nome é: {self.nome}; \n'
                f'Nasci em: {self.data_nascimento};\n'
                f'Meu código é: {self.codigo}.>;')

        # if self.estudando:
        #     print(f'Estou Estudando;')
        # else:
        #     print(f'Não estou estudando;')
        #
        # if self.trabalhando:
        #     print(f'Estou trabalhando>.')
        # else:
        #     print(f'Não está trabalhando>.')


    def estudar(self):
        if self.estudando and self.trabalhando:
            print(f'Trabalhando e estudando, então recebeu um aumento.')
            self.salario += 200
            print(f'O salário atual é: {self.salario} ')
        elif self.estudando:
            print(f'Está apenas estudando')
        else:
            print(f'Não está estudando!\n')

    def trabalhar(self):
        if self.trabalhando:
            print(f'Trabalhando!')
            self.salario += 1518
            print(f'salario: {self.salario}')
        else:
            print(f'Não está trabalhando!')


p1 = Pessoa('<Abner>', '01/02/2008', '13', estudando = True, trabalhando = False)
p1.apresentar()
p1.estudar()
p1.trabalhar()

p2 = Pessoa('<Bruno>', '27/06/2008', '2', estudando = False, trabalhando = True)
p2.apresentar()
p2.estudar()
p2.trabalhar()

p3 = Pessoa('<Vitor>', '27/09/2007', '29', estudando = False, trabalhando = True)
p3.apresentar()
p3.trabalhar()
p3.estudar()

p4 = Pessoa('<Vinícius>', '26/03/2008', '29', estudando = True, trabalhando = True)
p4.apresentar()
p4.trabalhar()
p4.estudar()

p5 = Pessoa('<Gabriele>', '27/10/2007','8', estudando = True, trabalhando = False)
p5.apresentar()
p5.trabalhar()
p5.estudar()

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