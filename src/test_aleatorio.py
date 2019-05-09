import unittest
from unittest.mock import MagicMock
from aleatorio import Aleatorio

class ImpulsivoTest(unittest.TestCase):

  def setUp(self):
    self.aleatorio = Aleatorio("Rafael T")
    self.aleatorio.temProbabilidade = MagicMock(return_value=True)

  def test_deve_poder_comprar_quando_houver_saldo(self):
    deveComprar = self.aleatorio.deveComprar({})

    self.assertTrue(deveComprar)

  def test_nao_deve_poder_comprar_quando_nao_houver_saldo(self):
    self.aleatorio.saldo = 0

    deveComprar = self.aleatorio.deveComprar({})

    self.assertFalse(deveComprar)

  def test_deve_poder_comprar_quando_com_probabilidade_a_partir_de_50_por_cento(self):
    deveComprar = self.aleatorio.deveComprar({})

    self.assertTrue(deveComprar)

if __name__ == "__main__":
  unittest.main()