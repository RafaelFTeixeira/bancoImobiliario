import unittest
from jogador import Jogador

class JogadorTest(unittest.TestCase):

    def setUp(self):
      self.nomeDoJogador = "Teixeiract"
      self.jogador = jogador = Jogador(self.nomeDoJogador)

    def test_deve_criar_um_jogador_com_nome(self):
      self.assertEqual(self.nomeDoJogador, self.jogador.nome)

    def test_deve_criar_um_jogador_com_saldo_de_300(self):
        self.assertEqual(300, self.jogador.saldo)

    def test_deve_iniciar_com_a_posicao_zero(self):
      self.assertEqual(0, self.jogador.posicao)
  
    def test_deve_pular_casa(self):
      posicaoEsperada = 0

      self.jogador.pularPosicao(6, 2)

      self.assertEqual(posicaoEsperada, self.jogador.posicao)

    def test_deve_validar_se_esta_falido(self):
      self.jogador.saldo = 0

      self.assertTrue(self.jogador.estaFalido())

if __name__ == "__main__":
  unittest.main()