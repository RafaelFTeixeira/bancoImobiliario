import unittest
from jogador import Jogador

class JogadorTest(unittest.TestCase):

    def test_deve_criar_um_jogador_com_nome(self):
      nomeDoJogador = "Teixeiract"

      jogador = Jogador(nomeDoJogador)

      assert nomeDoJogador == jogador.nome

    def test_deve_criar_um_jogador_com_saldo_de_300(self):
        jogador = Jogador("Ferreira")

        assert 300 == jogador.saldo

if __name__ == "__main__":
  unittest.main()