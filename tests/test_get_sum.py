from src.assignment import *

def test_get_sum():
    assert get_sum(1, 2) == 3
    assert get_sum(-1, -2) == -3
    assert get_sum(5, -3) == 2
    assert get_sum(0, 0) == 0
    assert get_sum(1000000, 2000000) == 3000000
