from src.assignment import *

def test_index_of_max():
    assert index_of_max([1, 2, 3, 4, 5]) == 4
    assert index_of_max([10, 20, 5, 30, 25]) == 3
    assert index_of_max([5, 5, 5, 5]) == 0
    assert index_of_max([-1, -5, -3]) == 0
    assert index_of_max([100]) == 0