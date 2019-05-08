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