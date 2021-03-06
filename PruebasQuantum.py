import unittest
import classicalToQuantum
import math

class test_simulacion(unittest.TestCase):

    def test_Canicas(self):
        matriz = [[False, False, False, False, False, False], [False, False, False, False, False, False],
                  [False, True, False, False, False, True], [False, False, False, True, False, False],
                  [False, False, True, False, False, False], [True, False, False, False, True, False]]
        self.assertEqual(classicalToQuantum.canicas(matriz, [[6], [2], [1], [5], [3], [10]], 1), [[0], [0], [12], [5], [1], [9]])

    def test_rendijasMultiples(self):
        inicial = [[0, 0, 0, 0, 0, 0, 0, 0], [1/2, 0, 0, 0, 0, 0, 0, 0], [1/2, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1/3, 0, 1, 0, 0, 0, 0], [0, 1/3, 0, 0, 1, 0, 0, 0],
                   [0, 1/3, 1/3, 0, 0, 1, 0, 0], [0, 0, 1/3, 0, 0, 0, 1, 0], [0, 0, 1/3, 0, 0, 0, 0, 1]]

        ans = classicalToQuantum.rendijasReales(2, 8, inicial, [1, 0, 0, 0, 0, 0, 0, 0])
        ans3 = classicalToQuantum.rendijasReales(2, 10, inicial, [1, 0, 0, 0, 0, 0, 0, 0])

        self.assertEqual(ans, [0.0, 0.0, 0.0, 0.16666666666666666, 0.16666666666666666, 0.3333333333333333, 0.16666666666666666, 0.16666666666666666])
        self.assertEqual(ans3, "Las matrices no son proporcionales.")


    def test_rendijaCuantica(self):
        estado = mat = [[(0, 0), (0, 0), (1, 2), (1, 2)], [(0, 0), (1, 2), (0, 0), (1, 2)],
                [(0, 0), (1, 2), (1, 2), (0, 0)], [(0, 0), (0, 0), (1, 2), (1, 2)]]
        ans = classicalToQuantum.rendijasCuanticas(2, 4, estado, [(0, 0), (1, 2), (1, 2), (0, 0)])
        self.assertEqual(ans, [(451, -418), (451, -418), (410, -380), (451, -418)])



if __name__ == "__main__":
    unittest.main()
