import unittest

def invertir_lista(lista):
    return lista[::-1]

def es_palindromo(palabra):
    return palabra == palabra[::-1]

def contar_ocurrencias(lista, elemento):
    return lista.count(elemento)

def obtener_valor(dicc, clave, default=None):
    return dicc.get(clave, default)

def combinar_diccionarios(dicc1, dicc2):
    combinado = dicc1.copy()
    combinado.update(dicc2)
    return combinado

class TestOperacionesAdicionales(unittest.TestCase):

    def test_invertir_lista(self):
        self.assertEqual(invertir_lista([1, 2, 3, 4]), [4, 3, 2, 1])

    def test_es_palindromo_verdadero(self):
        self.assertTrue(es_palindromo("anilina"))

    def test_es_palindromo_falso(self):
        self.assertFalse(es_palindromo("python"))

    def test_contar_ocurrencias(self):
        self.assertEqual(contar_ocurrencias([1, 2, 3, 2, 2, 4], 2), 3)

    def test_obtener_valor_existente(self):
        dicc = {"nombre": "Juan", "edad": 30}
        self.assertEqual(obtener_valor(dicc, "nombre"), "Juan")

    def test_obtener_valor_inexistente(self):
        dicc = {"nombre": "Juan", "edad": 30}
        self.assertEqual(obtener_valor(dicc, "ciudad", "Desconocido"), "Desconocido")

    def test_combinar_diccionarios(self):
        dicc1 = {"nombre": "Juan"}
        dicc2 = {"edad": 30}
        esperado = {"nombre": "Juan", "edad": 30}
        self.assertEqual(combinar_diccionarios(dicc1, dicc2), esperado)

if __name__ == '__main__':
    unittest.main()
