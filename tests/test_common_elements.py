from src.assignment import *

def test_common_elements():
    assert common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert common_elements(["a", "b", "c"], ["c", "d", "e"]) == ["c"]
    assert common_elements([1, 2, 3], [4, 5, 6]) == []
    assert common_elements([], [1, 2, 3]) == []
    assert common_elements([1, 1, 2, 2], [1, 2, 3]) == [1, 2]