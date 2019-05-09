import random
from impulsivo import Impulsivo
from aleatorio import Aleatorio
from exigente import Exigente
from cauteloso import Cauteloso
from propriedade import Propriedade

class Tabuleiro:

    def __init__(self):
        self.propriedades = [
            Propriedade('Morumbi', 300, 100),
            Propriedade('Santo Amaro', 200, 50)
        ]
        self.jogadores = [
            Impulsivo('Azul'),
            Aleatorio('Vermelho'),
            Exigente('Verde'),
            Cauteloso('Amarelo')
        ]

    def iniciar(self):
        for rodada in range(0, 250):
            for vezDoJogador in jogadores:
                posicao = __rodarDado()
                vezDoJogador.pularPosicao(posicao)
                propriedade = self.propriedades[vezDoJogador.posicao]
                if self.temQuePagarAluguel(propriedade, vezDoJogador):
                    pagarAluguel()

    def temQuePagarAluguel(self, propriedade, vezDoJogador):
        return propriedade.estaVendida() and propriedade.proprietario != vezDoJogador

    def __rodarDado():
        return random.randint(1, 6)
    
    def pagarAluguel(self, propriedade, vezDoJogador):
        vezDoJogador.saldo -= propriedade.valorDoAluguel
        proprietario = self.obterJogador(propriedade.proprietario.nome)
        proprietario.saldo += propriedade.valorDoAluguel

    def obterJogador(self, nome):
        return next(jogador for jogador in self.jogadores if jogador.nome == nome)