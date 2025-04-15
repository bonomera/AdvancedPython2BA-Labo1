import pytest
import utils

def test_fact():
    assert main.fact(5) == 120
    pass

def test_roots():
    assert main.roots(1, 0, 1) == 1
    pass

def test_integrate():
    assert main.integrate('x ** 2 - 1', -1, 1) == 0
    pass
