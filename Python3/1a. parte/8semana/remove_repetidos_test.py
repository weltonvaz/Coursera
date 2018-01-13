from unittest import TestCase, main
from remove_repetidos import remove_repetidos

class Remove_RepetidosTestCase(TestCase):
    def test_remove_repetidos(self):
        lista = [7,3,33,12,3,3,3,7,12,100]
        lista2 =  [3, 7, 12, 33, 100]
        self.assertEqual(lista, lista2)


if __name__ == '__main__':
    main()
