class Carro:
    def __init__(self, *motor, aceleracao= None,freagem= None):
        self.aceleracao = list(aceleracao)
        self.freagem =list(freagem)

        velocidade = aceleracao() - freagem()
        velocidade +=0

        if __name__ == '__main__':
            aceleracao=(7)
            freagem=(3)
            print(velocidade)








