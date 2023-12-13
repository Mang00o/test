from example import sum
from example import multiply

def test_sum():
    assert sum([2, 3]) == 5, "Should be 5"

def test_multiply():
    assert multiply([2,3]) == 6, "Should be 6"