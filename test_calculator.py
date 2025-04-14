#Link: https://github.com/oreoluwaowoeye/lab-10-OO-AH.git
import unittest
from calculator import *
#Partner 1: Oreoluwa Owoeye
#Partner 2: Austin Henneberg


class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        pass

    def test_subtract(self): # 3 assertions
        pass
    ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,2),6)
        self.assertEqual(mul(-5,-9),45)
        self.assertEqual(mul(4,4),16)


    def test_divide(self): # 3 assertions
        self.assertEqual(div(9,3),3)
        self.assertEqual(div(4,2),2)
        self.assertEqual(div(5,5),1)
    ##########################

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        pass

    def test_logarithm(self): # 3 assertions
        pass

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        pass
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion

        with self.assertRaises(ValueError):
            log(0,-2)
        pass

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertAlmostEqual(hypotenuse(4,6),7.2)
        self.assertAlmostEqual(hypotenuse(5,8),8.89)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
            square_root(-25)
        self.assertEqual(square_root(1),1)
        self.assertAlmostEqual(square_root(2),1.4)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()