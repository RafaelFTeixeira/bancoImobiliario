import random
from jogador import Jogador

class Aleatorio(Jogador):
    def __init__(self, nome):
        return super().__init__(nome)
    
    def deveComprar(self, propriedade):
        return self.temSaldoPositivo() and self.temProbabilidade()

    def temProbabilidade(self):
        return random.randint(0, 2) > 1