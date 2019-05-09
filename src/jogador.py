class Jogador:
    
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 300
        self.posicao = 0

    def temSaldoPositivo(self):
        return self.saldo > 0
    
    def pularPosicao(self, posicao):
        self.posicao += posicao