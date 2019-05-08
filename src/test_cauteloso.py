import unittest
from cauteloso import Cauteloso
from propriedade import Propriedade

class ImpulsivoTest(unittest.TestCase):

  def setUp(self):
    self.cauteloso = Cauteloso("Rafael T")
    self.propriedade = Propriedade("Santo Amaro", 220, 50)

  def test_deve_poder_comprar_quando_houver_saldo(self):
    deveComprar = self.cauteloso.deveComprar(self.propriedade)

    self.assertTrue(deveComprar)

  def test_nao_deve_poder_comprar_quando_nao_houver_saldo(self):
    self.cauteloso.saldo = 0

    deveComprar = self.cauteloso.deveComprar(self.propriedade)

    self.assertFalse(deveComprar)

  def test_deve_poder_comprar_quando_o_saldo_restante_fica_com_sobra_a_partir_de_80(self):
    deveComprar = self.cauteloso.deveComprar(self.propriedade)

    self.assertTrue(deveComprar)

  def test_nao_deve_poder_comprar_quando_o_saldo_restante_fica_menos_de_80(self):
    self.propriedade = Propriedade("Santo Amaro", 221, 50)

    deveComprar = self.cauteloso.deveComprar(self.propriedade)

    self.assertFalse(deveComprar)

if __name__ == "__main__":
  unittest.main()