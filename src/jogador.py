class Jogador:
    
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 300

    def temSaldoPositivo(self):
        return self.saldo > 0