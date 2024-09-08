import sys
import os
import unittest

# Añadir el directorio 'src' al path de Python para poder importar 'cuenta_bancaria'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from cuenta_bancaria import CuentaBancaria

class CuentaBancariaTest(unittest.TestCase):

    def setUp(self):
        # Método que se llama antes de cada prueba para inicializar datos comunes
        self.cuenta = CuentaBancaria("Maria", "67890", 1500, 0.02)

    def testGetTitular(self):
        valor_esperado = "Maria"
        self.cuenta.setTitular("Maria")
        valor_actual = self.cuenta.getTitular()
        self.assertEqual(valor_esperado, valor_actual)

    def testGetTitular2(self):
        valor_esperado = "Roberto"
        self.cuenta.setTitular("Roberto")
        valor_actual = self.cuenta.getTitular()
        self.assertEqual(valor_esperado, valor_actual)

    def testGetNumeroCuenta(self):
        valor_esperado = "67890"
        self.cuenta.setNumeroCuenta("67890")
        valor_actual = self.cuenta.getNumeroCuenta()
        self.assertEqual(valor_esperado, valor_actual)

    def testGetNumeroCuenta2(self):
        valor_esperado = "123456789A"
        self.cuenta.setNumeroCuenta("123456789A")
        valor_actual = self.cuenta.getNumeroCuenta()
        self.assertEqual(valor_esperado, valor_actual)

    def testGetSaldo(self):
        valor_esperado = 1500
        self.cuenta.setSaldo(1500)
        valor_actual = self.cuenta.getSaldo()
        self.assertEqual(valor_esperado, valor_actual)

    def testGetSaldo2(self):
        valor_esperado = 800
        self.cuenta.setSaldo(800)
        valor_actual = self.cuenta.getSaldo()
        self.assertEqual(valor_esperado, valor_actual)

    def testIngresar(self):
        self.cuenta.ingresar(700)
        valor_esperado = 2200
        valor_actual = self.cuenta.getSaldo()
        self.assertEqual(valor_esperado, valor_actual)

    def testRetirar(self):
        self.cuenta.retirar(600)
        valor_esperado = 900
        valor_actual = self.cuenta.getSaldo()
        self.assertEqual(valor_esperado, valor_actual)

    def testRetirarInsuficiente(self):
        self.cuenta.retirar(2000)
        valor_esperado = 1500
        valor_actual = self.cuenta.getSaldo()
        self.assertEqual(valor_esperado, valor_actual)

    def testCalcularInteres(self):
        valor_esperado = 1500 * 0.02
        valor_actual = self.cuenta.calcularInteres()
        self.assertEqual(valor_esperado, valor_actual)

    def testCalcularInteresNegativo(self):
        self.cuenta.setSaldo(-1500)
        valor_actual = self.cuenta.calcularInteres()
        self.assertEqual(0, valor_actual)

    def testSetTipoInteres(self):
        self.cuenta.setTipoInteres(0.08)
        valor_esperado = 0.08
        valor_actual = self.cuenta.getTipoInteres()
        self.assertEqual(valor_esperado, valor_actual)

    def testSetTipoInteresInvalido(self):
        self.cuenta.setTipoInteres(-0.05)
        valor_esperado = 0.02
        valor_actual = self.cuenta.getTipoInteres()
        self.assertEqual(valor_esperado, valor_actual)

if __name__ == '__main__':
    unittest.main()
