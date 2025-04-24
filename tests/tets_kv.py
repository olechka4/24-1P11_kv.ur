import unittest
from main import cvyr
class TestKv(unittest.TestCase):
    def test_1(self):
        a, b, c = 4, 2, -2
        disk = 36
        x1 = -1
        x2 = 0.5
        res = cvyr(a, b, c)
        self.assertEqual(len(res), 4, "Неверное количество элементов")
        self.assertEqual(res[0], "Дискриминант > 0, квадратное уравнение имеет 2 корня")
        self.assertEqual(res[1], disk, "Неверный дискриминант")
        self.assertEqual(res[2], x1, "Неверный корень 1")
        self.assertEqual(res[3], x2, "Неверный корень 2")