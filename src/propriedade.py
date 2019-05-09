class Propriedade:

    def __init__(self, nome, valorDaVenda, valorDoAluguel):
        self.nome = nome
        self.valorDaVenda = valorDaVenda
        self.valorDoAluguel = valorDoAluguel
        self.proprietario = None

    def estaVendida(self):
        return None != self.proprietario

    def pertence(self, jogador):
        return self.estaVendida() and self.proprietario.nome == jogador.nome