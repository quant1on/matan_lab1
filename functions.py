import numpy as np

def func_test_dichotomy_1(x: float) -> float:
    return np.sin(x) + x**2 - x

def func_test_dichotomy_2(x: float) -> float:
    return (x - 2)**2 if x <= 0 else np.sin(x) + 4

def func_test_dichotomy_3(x: float) -> float:
    return abs(x)

def func_test_find_root_1(x: float) -> float:
    return -1 * (x - 2)**3   

def func_test_find_root_2(x: float) -> float:
    return np.sin(x - 1.4) + (x - 1.4)**2

def func_test_find_root_3(x: float) -> float:
    return x**2 + 3

def func_test_find_root_4(x: float) -> float:
    return (-1 * x**2) - 3

def func_test_find_root_adv_1(x: float) -> float:
    return (x - 1.3) * (x - 2.1) * x

def func_test_find_root_adv_2(x: float) -> float:
    return (x - 2) * (x - 1)

def func_test_find_root_adv_3(x: float) -> float:
    return x**2 + 1

def func_test_find_root_adv_4(x: float) -> float:
    return (-1 * x ** 2) - 1