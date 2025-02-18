from src.assignment import *

def test_reverse_list():
    assert reverse_list([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert reverse_list([5]) == [5]
    assert reverse_list([]) == []
    assert reverse_list([7, 2, 4]) == [4, 2, 7]