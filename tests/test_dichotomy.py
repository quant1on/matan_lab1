from main import dichotomy_search
import functions as func
import unittest

class GetDichotomyTestCase(unittest.TestCase):

    def test_regular_case(self):
        
        self.assertAlmostEqual(first=dichotomy_search(a=-2, b=5,
                                f=func.func_test_dichotomy_1, err=10e-7),
                                second=0.0, delta=10e-5)
        
        self.assertAlmostEqual(first=dichotomy_search(a=-10, b=1.5,
                                f=func.func_test_dichotomy_2, err=10e-7),
                                second=0.0, delta=10e-5)

        self.assertAlmostEqual(first=dichotomy_search(a=-3, b=6,
                                f=func.func_test_dichotomy_3, err=10e-7),
                                second=0.0, delta=10e-5)
    def test_left_overlap(self):

        self.assertAlmostEqual(first=dichotomy_search(a=0, b=5,
                                f=func.func_test_dichotomy_1, err=10e-7),
                                second=0.0, delta=10e-5)
        
        self.assertAlmostEqual(first=dichotomy_search(a=0, b=1.5,
                                f=func.func_test_dichotomy_2, err=10e-7),
                                second=0.0, delta=10e-5)

        self.assertAlmostEqual(first=dichotomy_search(a=0, b=6,
                                f=func.func_test_dichotomy_3, err=10e-7),
                                second=0.0, delta=10e-5)

    def test_right_overlap(self):

        self.assertAlmostEqual(first=dichotomy_search(a=-2, b=0,
                                f=func.func_test_dichotomy_1, err=10e-7),
                                second=0.0, delta=10e-5)
        
        self.assertAlmostEqual(first=dichotomy_search(a=-10, b=0,
                                f=func.func_test_dichotomy_2, err=10e-7),
                                second=0.0, delta=10e-5)

        self.assertAlmostEqual(first=dichotomy_search(a=-3, b=0,
                                f=func.func_test_dichotomy_3, err=10e-7),
                                second=0.0, delta=10e-5)