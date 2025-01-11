import numpy as np

def func_test_dichotomy_1(x: float) -> float:
    return np.sin(x) + x**2 - x

def func_test_dichotomy_2(x: float) -> float:
    return (x - 2)**2 if x <= 0 else np.sin(x) + 4

def func_test_dichotomy_3(x: float) -> float:
    return abs(x)
