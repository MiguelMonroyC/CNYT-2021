import unittest
import CalculadoraComplejos
import math

class TestCalculadora(unittest.TestCase):
   def test_adicion(self):
      r1 = CalculadoraComplejos.adicion([4, 6],[1, -5])
      r2 = CalculadoraComplejos.adicion([76, 23], [-80, 30])
      r3 = CalculadoraComplejos.adicion([50, 6], [18, -5])
      self.assertEqual(r1, [5, 1])
      self.assertEqual(r2, [-4, 53])
      self.assertEqual(r3, [68, 1])

   def test_resta(self):
      r1 = CalculadoraComplejos.inversavector(4, 18)
      r2 = CalculadoraComplejos.inversavector(50, 6)
      r3 = CalculadoraComplejos.inversavector(45, 15)
      self.assertEqual(r1, (-4, -18))
      self.assertEqual(r2, (-50, -6))
      self.assertEqual(r3, (-45, -15))

   def test_multiplicacionvactor(self):
      r = CalculadoraComplejos.multiplicacionvector((4, 6), 4)
      self.assertEqual(r, (16, 22))

   def test_sumaMatrices(self):
      r1 = CalculadoraComplejos.adicionmatrices([[(1, 1), (2, -3)], [(4, 2), (2, 4)]], [[(1, 0), (1, 0)], [(1, 0), (1, 0)]])
      r2 = CalculadoraComplejos.adicionmatrices([[(1, 3), (2, 3)], [(1, 3), (2, 3)]], [[(1, 0), (3, 6)], [(1, 0), (3, 6)]])
      self.assertEqual(r1, [[(2, 1), (3, -3)], [(5, 2), (3, 4)]])
      self.assertEqual(r2, [[(2, 3), (5, 9)], [(2, 3), (5, 9)]])

   def test_inversaMatriz(self):
      r1 = CalculadoraComplejos.inversamatriz([[(1,1),(2,-3)],[(4,2),(2,4)]])
      r2 = CalculadoraComplejos.inversamatriz([[(1,1),(0,3)],[(-1,2),(-2,4)]])
      self.assertEqual(r1,[[(-1,-1),(-2,3)],[(-4,-2),(-2,-4)]])
      self.assertEqual(r2,[[(-1,-1),(0,-3)],[(1,-2),(2,-4)]])

   def multiplicacionEscalarMatrices(self):
      r1 = CalculadoraComplejos.multiplicacionmatriz([[(1, 1), (2, -3)], [(4, 2), (2, 4)]], (1, 1))
      r2 = CalculadoraComplejos.multiplicacionmatriz([[(1, 1), (2, -3)], [(4, 2), (2, 4)]], (2, 3))
      self.assertEqual(r1, [[(0, 2), (5, -1)], [(2, 6), (-2, 6)]])
      self.assertEqual(r2, [[(-1, 5), (13, 0)], [(2, 16), (-8, 14)]])

   def test_traspuesta(self):
      r1 = CalculadoraComplejos.transpuesta([[(1, 1), (2, -3)], [(4, 2), (2, 4)]])
      r2 = CalculadoraComplejos.transpuesta([[(1, 1), (2, -3), (5, 4)], [(4, 2), (2, 4), (4, 5)]])
      self.assertEqual(r1, [[(1, 1), (4, 2)], [(2, -3), (2, 4)]])
      self.assertEqual(r2, [[(1, 1), (4, 2)], [(2, -3), (2, 4)], [(5, 4), (4, 5)]])

   def test_conjugadoVector(self):
      r1 = CalculadoraComplejos.conjugadavector([(1, 2), (1, -2), (1, 5)])
      r2 = CalculadoraComplejos.conjugadavector([(1, 3), (3, 2), (3, -9)])
      self.assertEqual(r1, [(1, -2), (1, 2), (1, -5)])
      self.assertEqual(r2, [(1, -3), (3, -2), (3, 9)])

   def test_conjugadoMatriz(self):
      r1 = CalculadoraComplejos.conjugadamatriz([[(1, 2), (2, 1)], [(1, -2), (2, -3)], [(3, 4), (3, -1)]])
      r2 = CalculadoraComplejos.conjugadamatriz([[(1, 1), (2, 2), (1, 1)], [(2, 2), (3, -3), (2, 3)]])
      self.assertEqual(r1, [[(1, -2), (2, -1)], [(1, 2), (2, 3)], [(3, -4), (3, 1)]])
      self.assertEqual(r2, [[(1, -1), (2, -2), (1, -1)], [(2, -2), (3, 3), (2, -3)]])

   def test_matrizAdjunta(self):
      r1 = CalculadoraComplejos.adjuntamatriz([[(1, 1), (2, -3)], [(4, 2), (2, 4)]])
      r2 = CalculadoraComplejos.adjuntamatriz([[(1, 1), (2, 3)], [(4, 2), (1, 4)], [(1, 0), (3, -4)]])
      self.assertEqual(r1, [[(1, -1), (4, -2)], [(2, 3), (2, -4)]])
      self.assertEqual(r2, [[(1, -1), (4, -2), (1, 0)], [(2, -3), (1, -4), (3, 4)]])
