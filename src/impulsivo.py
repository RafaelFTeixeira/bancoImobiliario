from jogador import Jogador

class Impulsivo(Jogador):

    def __init__(self, nome):
        super().__init__(nome)

    def deveComprar(self, propriedade):
        return self.temSaldoPositivo()