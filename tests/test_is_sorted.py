from src.assignment import *

def test_isSorted():
    assert isSorted([1, 2, 3, 4, 5]) == True
    assert isSorted([5, 4, 3, 2, 1]) == False
    assert isSorted([1, 1, 2, 2, 3, 3]) == True
    assert isSorted([1]) == True
    assert isSorted([]) == True