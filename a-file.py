import unittest

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

class TestFuncionesMatematicas(unittest.TestCase):

    def test_suma_positivos(self):
        self.assertEqual(suma(2, 3), 5)

    def test_suma_negativos(self):
        self.assertEqual(suma(-2, -3), -5)

    def test_suma_mezclados(self):
        self.assertEqual(suma(-2, 3), 1)

    def test_resta_positivos(self):
        self.assertEqual(resta(5, 3), 2)

    def test_resta_negativos(self):
        self.assertEqual(resta(-5, -3), -2)

    def test_resta_mezclados(self):
        self.assertEqual(resta(5, -3), 8)

    def test_suma_cero(self):
        self.assertEqual(suma(0, 0), 0)

    def test_resta_cero(self):
        self.assertEqual(resta(0, 0), 0)

    def test_suma_cero_uno(self):
        self.assertEqual(suma(0, 1), 1)

    def test_resta_cero_uno(self):
        self.assertEqual(resta(0, 1), -1)

if __name__ == '__main__':
    unittest.main()
