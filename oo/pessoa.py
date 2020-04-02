class Pessoa:
    def __init__(self, *filhos, nome=None, idade = 15):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar (self):
        return 'Olá '

if __name__ == '__main__':
    iotti = Pessoa(nome = 'iotti')
    filho1 = Pessoa(iotti, nome='oliver')
    print(filho1.nome)
    print(filho1.idade)
    for filho in filho1.filhos:
        print(filho1.filhos)