"""
Tests for our array class
"""

from cgi import test
from array_class import Array

# 1D tests (Task 4)


def test_str_1d():
    liste = Array((4,), 1, 2, 3, 4)
    #print(str(liste))
    assert "[1, 2, 3, 4]" == str(liste)
    


def test_add_1d():
    a = Array((4,), 1, 2, 3, 4)
    b = Array((3,), 2, 2, 0)
    c = 10

    test1 = Array((4,), 3, 4, 3, 4)
    test2 = Array((4,), 11, 12, 13, 14) 
    test3 = Array((3,), 12, 12, 10)

    assert a + b == test1
    assert a + c == test2
    assert b + c == test3
    assert a.__add__(False) == NotImplemented
    assert a.__add__(Array((2,), False, True)) == NotImplemented


def test_sub_1d():
    a = Array((4,), 1, 2, 3, 4)
    b = Array((3,), 2, 2, 0)
    c = 10

    test1 = Array((4,), 1, 0, -3, 4)
    test2 = Array((4,), 9, 8, 7, 6) 
    test3 = Array((3,), 8, 8, 10)

    assert a - b == test1
    assert a - c == test2
    assert b - c == test3
    assert a.__sub__(False) == NotImplemented
    assert a.__sub__(Array((2,), False, True)) == NotImplemented

  


def test_mul_1d():
    a = Array((4,), 1, 2, 3, 4)
    b = Array((3,), 2, 2, 0)
    c = 10

    test1 = Array((4,), 2, 4, 0, 4)
    test2 = Array((4,), 10, 20, 30, 40) 
    test3 = Array((3,), 20, 20, 0)

    assert a * b == test1
    assert a * c == test2
    assert b * c == test3
    assert a.__mul__(False) == NotImplemented
    assert a.__mul__(Array((2,), False, True)) == NotImplemented
    


def test_eq_1d():
    a = Array((4,), 1, 2, 3, 4)
    b = Array((3,), 2, 2, 0)
    c = Array((4,), 1, 2, 3, 4)

    assert a != b 
    assert a == c



def test_same_1d():
    a = Array((4,), 1, 2, 3, 4)
    b = Array((4,), 2, 2, 5, 6)
    c = 3

    d = Array((4,), False, True, False, False)
    e = Array((4,), False, False, True, False)

    assert a.is_equal(b) == d
    assert a.is_equal(c) == e    


def test_smallest_1d():
    a = Array((4,), 1, 2, 3, 4)
    b = Array((4,), 2, 0, 5, 6)
    
    assert a.min_element() == 1
    assert b.min_element() == 0


def test_mean_1d():
    a = Array((4,), 1, 2, 3, 4)
    b = Array((4,), 2, 0, 5, 6)

    assert a.mean_element() == 2.5
    assert b.mean_element() == 3.25



# 2D tests (Task 6)


def test_add_2d():
    a = Array((3,2), 8, 3, 4, 1, 6, 1)
    b = Array((4,2), 1, 2, 3, 4, 5, 6, 7, 8)
    c = 10
    

    test1 = Array((4,2), 9, 5, 7, 5, 11, 7, 7, 8)
    test2 = Array((3,2), 18, 13, 14, 11, 16, 11)
    test3 = Array((4,2), 11, 12, 13, 14, 15, 16, 17, 18)
   
    assert a + b == test1
    assert b + a == test1
    assert a + c == test2
    assert c + a == test2
    assert b + c == test3
    assert a.__add__(False) == NotImplemented
    assert a.__add__(Array((2, 2), False, True, False, True)) == NotImplemented


def test_mult_2d():
    a = Array((3,2), 8, 3, 4, 1, 6, 1)
    b = Array((4,2), 1, 2, 3, 4, 5, 6, 7, 8)
    c = 10

    test1 = Array((4,2), 8, 6, 12, 4, 30, 6, 7, 8)
    test2 = Array((3,2), 80, 30, 40, 10, 60, 10)
    test3 = Array((4,2), 10, 20, 30, 40, 50, 60, 70, 80)

    assert a * b == test1
    assert b * a == test1
    assert a * c == test2
    assert c * a == test2
    assert b * c == test3
    assert a.__mul__(False) == NotImplemented
    assert a.__mul__(Array((2, 2), False, True, False, True)) == NotImplemented



def test_same_2d():
    a = Array((3,2), 8, 3, 4, 1, 6, 1)
    b = Array((3,2), 1, 2, 4, 5, 6, 7)
    a_kopi = Array((3,2), 8, 3, 4, 1, 6, 1)

    test1 = Array((3,2), False, False, True, False, True, False)
    test2 = Array((3,2), True, True, True, True, True, True, True, True)

    assert a.is_equal(b) == test1
    assert a.is_equal(a_kopi) == test2



def test_mean_2d():
    a = Array((3,2), 8, 3, 4, 1, 6, 1)
    b = Array((5,2), 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

    assert a.mean_element() == 3.8333333333333335
    assert b.mean_element() == 1


if __name__ == "__main__":
    """
    Note: Write "pytest" in terminal in the same folder as this file is in to run all tests
    (or run them manually by running this file).
    Make sure to have pytest installed (pip install pytest, or install anaconda).
    """

    # Task 4: 1d tests
    test_str_1d()
    test_add_1d()
    test_sub_1d()
    test_mul_1d()
    test_eq_1d()
    test_mean_1d()
    test_same_1d()
    test_smallest_1d()

    # Task 6: 2d tests
    test_add_2d()
    test_mult_2d()
    test_same_2d()
    test_mean_2d()
