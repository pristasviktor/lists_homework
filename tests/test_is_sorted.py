from src.assignment import *

def test_is_sorted():
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([5, 4, 3, 2, 1]) == False
    assert is_sorted([1, 1, 2, 2, 3, 3]) == True
    assert is_sorted([1]) == True
    assert is_sorted([]) == True