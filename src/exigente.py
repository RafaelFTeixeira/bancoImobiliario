from jogador import Jogador

class Exigente(Jogador):
    
    def __init__(self, nome):
        return super().__init__(nome)

    def deveComprar(self, propriedade):
        return self.temSaldoPositivo() and propriedade.valorDoAluguel >= 50
    