class Carro:
    def __init__(self, velocidade= None, aceleracao=None, freagem=None):
        self.aceleracao = aceleracao
        self.freagem = freagem
        self.velocidade = velocidade

if __name__ == 'carro':
    calculodavelocidade1 = Carro(aceleracao=10)
    calculodavelocidade2 = Carro(freagem=20)
    velocidade = ((calculodavelocidade1.aceleracao) - (calculodavelocidade2.freagem))
    if velocidade <(-1):
        velocidade = 0
    print(velocidade)