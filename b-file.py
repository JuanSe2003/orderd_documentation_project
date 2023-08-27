import unittest

def concatenar_cadenas(a, b):
    return a + b

def agregar_elemento(lista, elemento):
    lista.append(elemento)
    return lista

def obtener_elemento(lista, indice):
    return lista[indice]

class TestOperaciones(unittest.TestCase):

    def test_concatenar_cadenas(self):
        self.assertEqual(concatenar_cadenas("Hola", " Mundo"), "Hola Mundo")

    # def test_repetir_cadena(self):
    #     self.assertEqual(repetir_cadena("Hola", 3), "HolaHolaHola")

    def test_agregar_elemento(self):
        self.assertEqual(agregar_elemento([1, 2, 3], 4), [1, 2, 3, 4])

    def test_obtener_elemento(self):
        self.assertEqual(obtener_elemento([1, 2, 3, 4], 2), 3)

    def test_concatenar_cadenas_vacias(self):
        self.assertEqual(concatenar_cadenas("", ""), "")

    # def test_repetir_cadena_vacia(self):
    #     self.assertEqual(repetir_cadena("", 5), "")

    def test_agregar_elemento_a_lista_vacia(self):
        self.assertEqual(agregar_elemento([], "Hola"), ["Hola"])

    def test_obtener_elemento_fuera_de_rango(self):
        with self.assertRaises(IndexError):
            obtener_elemento([1, 2, 3], 5)

    # def test_repetir_cadena_numero_negativo(self):
    #     with self.assertRaises(ValueError):
    #         repetir_cadena("Hola", -2)

    def test_agregar_elemento_none(self):
        self.assertEqual(agregar_elemento([1, 2, 3], None), [1, 2, 3, None])

if __name__ == '__main__':
    unittest.main()
