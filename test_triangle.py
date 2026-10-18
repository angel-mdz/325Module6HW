import math
from triangle import classify_triangle, is_valid_triangle

# A triangle with three equal positive sides should be Equilateral
def test_equilateral():
    assert classify_triangle(3, 3, 3) == 'Equilateral'

# A triangle with a zero-length side should be Invalid
def test_zero_side():
    assert classify_triangle(0, 3, 3) == 'Invalid'

# A triangle with a negative side should be Invalid
def test_negative_side():
    assert classify_triangle(-1, 3, 3) == 'Invalid'

# Positive sides whose two shortest lenghts sum to less than the longest are Invalid
def test_triangle_inequality_failure():
    assert classify_triangle(1, 2, 4) == 'Invalid'

# When the two shortest sides sum exactly to the longest, the triangle is Invalid
def test_degenerate_triangle():
    assert classify_triangle(1, 2, 3) == 'Invalid'

# A valid triangle with exactly two equal sides and no rihgt angle is Isoceles
def test_isosceles():
    assert classify_triangle(3, 3, 4) == 'Isosceles'

# A valid triangle with three different sides and no right angle is Scalene
def test_scalene():
    assert classify_triangle(4, 5, 6) == 'Scalene'

# A triangle with sides 3,4 ,5 is a right scalene
def test_right_scalene():
    assert classify_triangle(3, 4, 5) == 'Right Scalene'

# Equal legs of 5 and hypotenuse of 5 * math.sqrt(2) should be Right Isosceles
def test_right_isosceles_non_integer():
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == 'Right Isosceles'

