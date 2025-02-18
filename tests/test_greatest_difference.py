from src.assignment import *

def test_greatest_neighbour_difference():
    assert greatest_neighbour_difference([1, 3, 6, 10]) == 4
    assert greatest_neighbour_difference([10, 20, 30, 5]) == 25
    assert greatest_neighbour_difference([5, 5, 5, 5]) == 0
    assert greatest_neighbour_difference([100]) == 0
    assert greatest_neighbour_difference([]) == 0