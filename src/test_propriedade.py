import unittest
from propriedade import Propriedade
from impulsivo import Impulsivo

class PropriedadeTest(unittest.TestCase):

    def setUp(self):
        self.nome = "Morumbi"
        self.valorDaVenda = 250
        self.valorDoAluguel = 25
        self.propriedade = Propriedade(self.nome, self.valorDaVenda, self.valorDoAluguel)

    def test_deve_criar_uma_propriedade(self):
        propriedadeEsperada = {
            'nome': self.nome,
            'valorDaVenda': self.valorDaVenda,
            'valorDoAluguel': self.valorDoAluguel,
            'proprietario': None
        }

        self.assertEqual(propriedadeEsperada, self.propriedade.__dict__)

    def test_deve_inserir_um_proprietario(self):
        self.propriedade.proprietario = Impulsivo("Jogador1")

        self.assertIsNotNone(self.propriedade.proprietario)
    
    def test_deve_validar_se_a_propriedade_pertence_ao_um_jogador(self):
        jogador = Impulsivo('Azul')
        self.propriedade.proprietario = jogador

        pertence = self.propriedade.pertence(jogador)

        self.assertTrue(pertence)

    def test_deve_validar_se_a_propriedade_nao_pertence_ao_um_jogador(self):
        jogador = Impulsivo('Azul')

        pertence = self.propriedade.pertence(jogador)

        self.assertFalse(pertence)

if __name__ == "__main__":
  unittest.main()