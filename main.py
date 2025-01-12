import numpy
import typing as tp

def dichotomy_search(a: float, b: float, f: tp.Callable, err: float) -> float:
    epsilon = err / 2
    while (b - a) / 2 > err:
        y_k = (a + b - epsilon) / 2
        z_k = (a + b + epsilon) / 2
        if f(y_k) <= f(z_k):
            b = z_k
        else:
            a = y_k
    return (a + b) / 2

def find_root(a: float, b: float, f: tp.Callable, err: float) -> float:
    pass

def find_root_advanced(a: float, b: float, f: tp.Callable, err: float, part_range: tp.Optional[float] = None) -> tp.List[float]:
    if part_range is None: part_range = err * 100
    pass