from src.assignment import *

def test_change():
    lst = [1, 2, 3, 4, 5]
    change(lst, 1, 3)
    assert lst == [1, 4, 3, 2, 5]

    lst = [10, 20, 30]
    change(lst, 0, 2)
    assert lst == [30, 20, 10]