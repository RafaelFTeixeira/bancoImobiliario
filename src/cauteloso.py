from jogador import Jogador

class Cauteloso(Jogador):

    def __init__(self, nome):
        return super().__init__(nome)

    def deveComprar(self, propriedade):
        return self.temSaldoPositivo() and (self.saldo - propriedade.valorDaVenda) >= 80