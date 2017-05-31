import numpy as np

def test_numpy_partition():
    in_ar = np.array([3,2,-1,10])
    parti = np.partition(in_ar,1)
    assert parti[1] == 2 

def test_division():
    assert 3./2 == 1.5

def test_addition():
    assert 1 + 1 == 2

def test_soustraction():
    assert 3 - 1 == 2
