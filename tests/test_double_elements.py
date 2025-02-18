from src.assignment import *

def test_double_elements():
    assert double_elements([1, 2, 3]) == [2, 4, 6]
    assert double_elements([0, -1, -2]) == [0, -2, -4]
    assert double_elements([]) == []
    assert double_elements([100]) == [200]