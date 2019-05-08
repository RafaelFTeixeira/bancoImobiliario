import unittest
from exigente import Exigente
from propriedade import Propriedade

class ImpulsivoTest(unittest.TestCase):

  def setUp(self):
    self.exigente = Exigente("Rafael T")
    self.propriedade = Propriedade("Santo Amaro", 260, 50)

  def test_deve_poder_comprar_quando_houver_saldo(self):
    deveComprar = self.exigente.deveComprar(self.propriedade)

    self.assertTrue(deveComprar)

  def test_nao_deve_poder_comprar_quando_nao_houver_saldo(self):
    self.exigente.saldo = 0

    deveComprar = self.exigente.deveComprar(self.propriedade)

    self.assertFalse(deveComprar)

  def test_deve_poder_comprar_quando_a_propriedade_tenha_um_aluguel_a_partir_que_50(self):
    deveComprar = self.exigente.deveComprar(self.propriedade)

    self.assertTrue(deveComprar)

  def test_nao_deve_poder_comprar_quando_o_aluguel_da_propriedade_for_menor_que_50(self):
    self.propriedade = Propriedade("Santo Amaro", 260, 49)

    deveComprar = self.exigente.deveComprar(self.propriedade)

    self.assertFalse(deveComprar)

if __name__ == "__main__":
  unittest.main()