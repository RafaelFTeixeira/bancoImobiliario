import unittest
from impulsivo import Impulsivo

class ImpulsivoTest(unittest.TestCase):

  def setUp(self):
    self.impulsivo = Impulsivo("R Teixeira")

  def test_deve_poder_comprar_quando_houver_saldo(self):
    self.assertTrue(self.impulsivo.deveComprar({}))

  def test_nao_deve_poder_comprar_quando_nao_houver_saldo(self):
    self.impulsivo.saldo = 0

    self.assertFalse(self.impulsivo.deveComprar({}))

if __name__ == "__main__":
  unittest.main()