#Link: https://github.com/oreoluwaowoeye/lab-10-OO-AH.git
import unittest
from calculator import *
#Partner 1: Oreoluwa Owoeye
#Partner 2: Austin Henneberg

class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self):
        self.assertEqual(add(5, 4), 9)# 3 assertions
        self.assertNotEqual(add(2, 3), 6)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(10, 1), 9)
        self.assertNotEqual(sub(5, 3), 3)
    ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,2),6)
        self.assertEqual(mul(-5,-9),45)
        self.assertEqual(mul(4,4),16)


    def test_divide(self): # 3 assertions
        self.assertEqual(div(3,9),3)
        self.assertEqual(div(2,4),2)
        self.assertEqual(div(5,5),1)
    ##########################

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
        pass

    def test_logarithm(self): # 3 assertions
        with self.assertRaises(ValueError):
            log(0,0)


    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            log(1, -1)

    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion

        with self.assertRaises(ValueError):
            log(0,5)


    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertAlmostEqual(hypotenuse(5,12),13)
        self.assertAlmostEqual(hypotenuse(7,24),25)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
            square_root(-25)


# Do not touch this
if __name__ == "__main__":
    unittest.main()