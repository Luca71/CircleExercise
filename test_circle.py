import pytest
from math import pi, pow
from circleExercise import Circle

@pytest.fixture
def circle_test():
    return Circle(8)

def test_circle_init(circle_test):
    assert circle_test._radius == 8
    assert circle_test._diameter == 16
    assert circle_test._area == pi * pow(8, 2)

def test_circle_area(circle_test):
    assert circle_test.circle_area() == pi * pow(8, 2)

def test_print_circle(circle_test):
    assert str(circle_test) == "This is a Circle:\nRadius: 8\nDiameter: 16\nArea: 201.06192982974676\n"

def test_circles_add(circle_test):
    other_circle = Circle(2)
    new_circle = circle_test + other_circle
    assert new_circle._radius == 10

def test_circles_bigger(circle_test):
    other_circle = Circle(2)
    is_bigger = circle_test > other_circle
    is_not_bigger = other_circle > circle_test
    assert is_bigger == True
    assert is_not_bigger == False

def test_circles_equal(circle_test):
    other_circle = Circle(8)
    assert circle_test == other_circle

def test_circles_sort():
    circles_list = [Circle(8), Circle(2), Circle(5), Circle(20)]
    circles_list.sort()
    assert circles_list[0]._radius == 2
    assert circles_list[1]._radius == 5
    assert circles_list[2]._radius == 8
    assert circles_list[3]._radius == 20
