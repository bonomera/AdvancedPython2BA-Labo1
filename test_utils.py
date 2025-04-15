import pytest
import utils as main

def test_fact():
    assert main.fact(5) == 120
    pass

def test_roots():
    assert main.roots(1, 0, 1) == (1j, -1j)

    pass

def test_integrate():
    assert main.integrate('x ** 2 - 1', -1, 1) == (-1.3333333333333335, 1.4802973661668755e-14)
    pass
