from src.assignment import *

def test_count_element():
    assert count_element([1, 2, 2, 3, 4, 2], 2) == 3
    assert count_element(["a", "b", "a", "c"], "a") == 2
    assert count_element([5, 6, 7], 10) == 0
    assert count_element([], 1) == 0