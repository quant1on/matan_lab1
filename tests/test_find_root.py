from main import find_root
import functions as func
import unittest

class GetFindRootTestCase(unittest.TestCase):

    def test_regular_case(self):

        self.assertAlmostEqual(first=find_root(a=-3, b=5, f=func.func_test_find_root_1,
                                err=10e-7), second=2, delta=10e-7)
        
        self.assertAlmostEqual(first=find_root(a=1, b=4, f=func.func_test_find_root_2,
                                err=10e-7), second=1.4, delta=10e-7)
        
    def test_left_overlap(self):

        self.assertAlmostEqual(first=find_root(a=2, b=5, f=func.func_test_find_root_1,
                                err=10e-7), second=2, delta=10e-7)
        
        self.assertAlmostEqual(first=find_root(a=1.4, b=4, f=func.func_test_find_root_2,
                                err=10e-7), second=1.4, delta=10e-7)
        
    def test_right_overlap(self):

        self.assertAlmostEqual(first=find_root(a=-3, b=2, f=func.func_test_find_root_1,
                                err=10e-7), second=2, delta=10e-7)
        
        self.assertAlmostEqual(first=find_root(a=1, b=1.4, f=func.func_test_find_root_2,
                                err=10e-7), second=1.4, delta=10e-7)
        
    def test_no_roots(self):

        self.assertIsNone(obj=find_root(a=-2, b=4, f=func.func_test_find_root_3, err=10e-7))

        self.assertIsNone(obj=find_root(a=-3, b=2, f=func.func_test_find_root_4, err=10e-7))