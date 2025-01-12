from main import find_root_advanced
import functions as func
import unittest

class GetFindRootAdvancedTestCase(unittest.TestCase):
    
    def test_regular_case(self):

        roots_1 = sorted(find_root_advanced(a=-2, b=5, f=func.func_test_find_root_adv_1, err=10e-7))
        roots_2 = sorted(find_root_advanced(a=0, b=3, f=func.func_test_find_root_adv_2, err=10e-7))

        true_roots_1 = [0, 1.3, 2.1]
        true_roots_2 = [1, 2]

        if (len(roots_1) != 3 or len(roots_2) != 2): self.fail()

        for i in range(3):
            self.assertAlmostEqual(first=roots_1[i], second=true_roots_1[i], delta=10e-7)

        for i in range(2):
            self.assertAlmostEqual(first=roots_2[i], second=true_roots_2[i], delta=10e-7)
    
    def test_no_roots(self):

        roots_1 = sorted(find_root_advanced(a=-2, b=3, f=func.func_test_find_root_adv_3, err=10e-7))
        roots_2 = sorted(find_root_advanced(a=-4, b=1, f=func.func_test_find_root_adv_4, err=10e-7))

        self.assertEqual(first=roots_1, second=[])
        self.assertEqual(first=roots_2, second=[])