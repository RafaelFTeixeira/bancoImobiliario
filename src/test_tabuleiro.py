import unittest
from tabuleiro import Tabuleiro
from impulsivo import Impulsivo
from aleatorio import Aleatorio

class TabuleiroTest(unittest.TestCase):

    def setUp(self):
        self.tabuleiro = Tabuleiro()

    def test_deve_obter_jogador_por_nome(self):
        nomeDoJogador = 'Azul'
        jogadorEsperado = Impulsivo(nomeDoJogador)

        jogadorEncontrado = self.tabuleiro.obterJogador(nomeDoJogador)

        assert jogadorEsperado.__eq__(jogadorEncontrado)
    
    def test_deve_descontar_do_saldo_do_jogador_que_esta_na_posicao_da_propriedade_vendida(self):
        jogador = Impulsivo('Azul')
        propriedade = self.tabuleiro.propriedades[0]
        propriedade.proprietario = Aleatorio('Vermelho')
        saldoEsperado = jogador.saldo - propriedade.valorDoAluguel

        self.tabuleiro.pagarAluguel(propriedade, jogador)

        self.assertEqual(saldoEsperado, jogador.saldo)

    def test_deve_acrescentar_o_saldo_do_proprietario_que_teve_o_aluguel_pago(self):
        jogador = Impulsivo('Azul')
        propriedade = self.tabuleiro.propriedades[0]
        propriedade.proprietario = Aleatorio('Vermelho')
        proprietario = self.tabuleiro.obterJogador('Vermelho')
        saldoEsperado = proprietario.saldo + propriedade.valorDoAluguel

        self.tabuleiro.pagarAluguel(propriedade, jogador)

        self.assertEqual(saldoEsperado, proprietario.saldo)

    def test_deve_pagar_aluguel_quando_esta_vendida(self):
        jogador = Impulsivo('Azul')
        propriedade = self.tabuleiro.propriedades[0]
        propriedade.proprietario = Aleatorio('Vermelho')

        temQuePagarAluguel = self.tabuleiro.temQuePagarAluguel(propriedade, jogador)

        self.assertTrue(temQuePagarAluguel)

    def test_deve_pagar_aluguel_quando_o_proprietario_for_diferente_da_vez_do_jogador(self):
        jogador = Impulsivo('Azul')
        propriedade = self.tabuleiro.propriedades[0]
        propriedade.proprietario = Aleatorio('Vermelho')

        temQuePagarAluguel = self.tabuleiro.temQuePagarAluguel(propriedade, jogador)

        self.assertTrue(temQuePagarAluguel)

    def test_nao_deve_pagar_aluguel_quando_nao_esta_vendida(self):
        jogador = Impulsivo('Azul')
        propriedade = self.tabuleiro.propriedades[0]

        temQuePagarAluguel = self.tabuleiro.temQuePagarAluguel(propriedade, jogador)

        self.assertFalse(temQuePagarAluguel)
    
    def test_deve_pagar_aluguel_quando_o_proprietario_for_diferente_da_vez_do_jogador(self):
        jogador = Impulsivo('Azul')
        propriedade = self.tabuleiro.propriedades[0]
        propriedade.proprietario = jogador

        temQuePagarAluguel = self.tabuleiro.temQuePagarAluguel(propriedade, jogador)

        self.assertFalse(temQuePagarAluguel)


if __name__ == "__main__":
  unittest.main()