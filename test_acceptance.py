from triangle import classify_triangle
import math

def test_acceptance():
    #test for an equiilateral triangle
    assert classify_triangle(3, 3, 3) == 'Equilateral'

    #test for an Isosceles triangle
    assert classify_triangle(3, 3, 4) == 'Isosceles'

    #test for a Scalene triangle
    assert classify_triangle(4, 5, 6) == 'Scalene'

    #test for an invalid triangle inequality with all positive sides
    assert classify_triangle(1, 2, 4) == 'Invalid'

    #test for an invalid triangle equality with all positive sides
    assert classify_triangle(1, 2, 3) == 'Invalid'

    #test for invalid triangle with a negative side
    assert classify_triangle(-1, 3, 3) == 'Invalid'

    #test for invalid triangle with a zero side
    assert classify_triangle(0, 4, 3) == 'Invalid'

    #test for a right prefix isosceles triangle 
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == 'Right Isosceles'