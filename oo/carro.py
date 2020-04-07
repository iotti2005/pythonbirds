class Carro:
    def __init__(self, *velocidade, aceleracao=None, freagem = None):
        self.aceleracao = aceleracao
        self.freagem = freagem
        self.velocidade = list(velocidade)


if __name__ == '__main__':
    calculodavelocidade1 = Carro(aceleracao=10)
    calculodavelocidade2 = Carro(freagem=3)
    velocidade=((calculodavelocidade1.aceleracao)-(calculodavelocidade2.freagem))
    print(velocidade)
