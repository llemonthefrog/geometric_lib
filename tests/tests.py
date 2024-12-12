import unittest
import math

import circle
import square
import triangle
import calculate


class SquareTests(unittest.TestCase):
    def test_area_int(self):
        print("\n[Square area test]")
        self.assertEqual(square.area(10), 100)
        self.assertEqual(square.area(9), 81)
        self.assertEqual(square.area(200), 40000)
        print("[Test passed]")

    def test_perimeter_int(self):
        print("\n[Square perimeter test]")
        self.assertEqual(square.perimeter(20), 80)
        self.assertEqual(square.perimeter(15), 60)
        self.assertEqual(square.perimeter(30), 120)
        print("[Test passed]")

    def test_area_float(self):
        print("\n[Square area test]")
        self.assertAlmostEqual(square.area(10.5), 110.25)
        self.assertAlmostEqual(square.area(9.4), 88.36)
        self.assertAlmostEqual(square.area(200.16), 40064.0256)
        print("[Test passed]")

    def test_perimeter_float(self):
        print("\n[Square perimeter test]")
        self.assertAlmostEqual(square.perimeter(20.2), 80.8)
        self.assertAlmostEqual(square.perimeter(15.15), 60.6)
        self.assertAlmostEqual(square.perimeter(30.12), 120.48)
        print("[Test passed]")

    def test_error_area_int(self):
        print("\n[Square perimeter error test]")
        with self.assertRaises(ValueError):
            square.area(-1)

    def test_error_area_type(self):
        with self.assertRaises(TypeError):
            square.area("a")

        with self.assertRaises(TypeError):
            square.area(True)
        print("[Test passed]")

    def test_error_perimeter(self):
        print("\n[Square perimeter error test]")
        with self.assertRaises(ValueError):
            square.perimeter(-1)

    def test_error_perimeter_type(self):
        with self.assertRaises(TypeError):
            square.perimeter("a")

        with self.assertRaises(TypeError):
            square.perimeter(True)
        print("[Test passed]")


class CircleTests(unittest.TestCase):
    def test_area_int(self):
        print("\n[Circle area test]")
        self.assertAlmostEqual(circle.area(10), math.pi * 10**2, places=2)
        self.assertAlmostEqual(circle.area(9), math.pi * 9**2, places=2)
        self.assertAlmostEqual(circle.area(15), math.pi * 15**2, places=2)
        print("[Test passed]")

    def test_perimeter_int(self):
        print("\n[Circle perimeter test]")
        self.assertAlmostEqual(circle.perimeter(10), 2 * math.pi * 10, places=2)
        self.assertAlmostEqual(circle.perimeter(9), 2 * math.pi * 9, places=2)
        self.assertAlmostEqual(circle.perimeter(15), 2 * math.pi * 15, places=2)
        print("[Test passed]")

    def test_area_float(self):
        print("\n[Circle area test]")
        self.assertAlmostEqual(circle.area(10.5), math.pi * 10.5**2, places=2)
        self.assertAlmostEqual(circle.area(9.4), math.pi * 9.4**2, places=2)
        self.assertAlmostEqual(circle.area(200.16), math.pi * 200.16**2, places=2)
        print("[Test passed]")

    def test_perimeter_float(self):
        print("\n[Circle perimeter test]")
        self.assertAlmostEqual(circle.perimeter(20.2), 2 * math.pi * 20.2, places=2)
        self.assertAlmostEqual(circle.perimeter(15.15), 2 * math.pi * 15.15, places=2)
        self.assertAlmostEqual(circle.perimeter(30.12), 2 * math.pi * 30.12, places=2)
        print("[Test passed]")

    def test_error_area_value(self):
        print("\n[Circle perimeter error test]")
        with self.assertRaises(ValueError):
            circle.area(-1)

    def test_error_area_type(self):
        with self.assertRaises(TypeError):
            circle.area("a")

        with self.assertRaises(TypeError):
            circle.area(True)
        print("[Test passed]")

    def test_error_perimeter(self):
        print("\n[Circle perimeter error test]")
        with self.assertRaises(ValueError):
            circle.perimeter(-1)

    def test_error_perimeter_type(self):
        with self.assertRaises(TypeError):
            circle.perimeter("a")

        with self.assertRaises(TypeError):
            circle.perimeter(True)
        print("[Test passed]")


class TriangleTest(unittest.TestCase):
    def test_area_int(self):
        print("\n[Triangle area test]")
        self.assertEqual(triangle.area(1, 2, 3), 3)
        self.assertEqual(triangle.area(6, 6, 6), 9)
        self.assertEqual(triangle.area(9, 9, 8), 13)
        print("[Test passed]")

    def test_perimeter_int(self):
        print("\n[Triangle perimeter test]")
        self.assertEqual(triangle.perimeter(1, 2, 3), 6)
        self.assertEqual(triangle.perimeter(6, 6, 6), 18)
        self.assertEqual(triangle.perimeter(9, 9, 9), 27)
        print("[Test passed]")

    def test_area_float(self):
        print("\n[Triangle area test]")
        self.assertAlmostEqual(triangle.area(2, 2, 3), 3.5)
        self.assertAlmostEqual(triangle.area(6, 6, 9), 10.5)
        self.assertAlmostEqual(triangle.area(9, 9, 9), 13.5)
        print("[Test passed]")

    def test_perimeter_float(self):
        print("\n[Triangle perimeter test]")
        self.assertAlmostEqual(triangle.perimeter(1, 2.2, 3.5), 6.7)
        self.assertAlmostEqual(triangle.perimeter(6, 6, 6.12), 18.12)
        self.assertAlmostEqual(triangle.perimeter(9, 9.15, 9.173), 27.323)
        print("[Test passed]")

    def test_error_area(self):
        print("\n[Triangle area error test]")
        with self.assertRaises(ValueError):
            triangle.area(-20, 10, 10)
        with self.assertRaises(ValueError):
            triangle.area(10, -20, 10)
        with self.assertRaises(ValueError):
            triangle.area(10, 10, -20)

    def test_error_area_type(self):
        with self.assertRaises(TypeError):
            triangle.area("a", 10, 10)
        with self.assertRaises(TypeError):
            triangle.area(10, "a", 10)
        with self.assertRaises(TypeError):
            triangle.area(10, 10, "a")

        with self.assertRaises(TypeError):
            triangle.area(True, 10, 10)
        with self.assertRaises(TypeError):
            triangle.area(10, True, 10)
        with self.assertRaises(TypeError):
            triangle.area(10, 10, True)

    def test_error_perimeter(self):
        print("\n[Triangle perimeter error test]")
        with self.assertRaises(ValueError):
            triangle.perimeter(-20, 10, 10)
        with self.assertRaises(ValueError):
            triangle.perimeter(10, -20, 10)
        with self.assertRaises(ValueError):
            triangle.perimeter(10, 10, -20)

    def test_error_perimeter_type(self):
        with self.assertRaises(TypeError):
            triangle.perimeter("a", 10, 10)
        with self.assertRaises(TypeError):
            triangle.perimeter(10, "a", 10)
        with self.assertRaises(TypeError):
            triangle.perimeter(10, 10, "a")

        with self.assertRaises(TypeError):
            triangle.perimeter(True, 10, 10)
        with self.assertRaises(TypeError):
            triangle.perimeter(10, True, 10)
        with self.assertRaises(TypeError):
            triangle.perimeter(10, 10, True)


class CalcTest(unittest.TestCase):
    def test_basic_case1(self):
        print("\n[Basic calc case]")
        self.assertEqual(
            calculate.calc("circle", "perimeter", [10]),
            "perimeter of circle is 62.83185307179586"
        )
        print("[Test passed]")

    def test_basic_case2(self):
        print("\n[Basic calc case]")
        self.assertEqual(
            calculate.calc("circle", "area", [10]),
            "area of circle is 314.1592653589793"
        )
        print("[Test passed]")

    def test_basic_case3(self):
        print("\n[Basic calc case]")
        self.assertEqual(
            calculate.calc("triangle", "area", [10, 10, 10]),
            "area of triangle is 15.0"
        )
        print("[Test passed]")

    def test_invalid_figure(self):
        with self.assertRaises(AssertionError):
            calculate.calc('hexagon', 'area', [5])

    def test_invalid_function(self):
        with self.assertRaises(AssertionError):
            calculate.calc('circle', 'volume', [5])
    def test_invalid_size_for_circle(self):
        with self.assertRaises(TypeError):
            calculate.calc('circle', 'area', 'five')

    def test_invalid_size_for_square(self):
        with self.assertRaises(TypeError):
            calculate.calc('square', 'perimeter', [5, 5])

    def test_invalid_size_for_triangle(self):
        with self.assertRaises(TypeError):
            calculate.calc('triangle', 'area', [5])