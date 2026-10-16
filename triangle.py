"""Validate and classify triangles with numeric side lengths."""

import math


def is_valid_triangle(a, b, c) -> bool:
    """Return whether finite numeric sides form a nondegenerate triangle."""
    if not all(math.isfinite(side) and side > 0 for side in (a, b, c)):
        return False

    shortest, middle, longest = sorted((a, b, c))
    return shortest + middle > longest


def classify_triangle(a, b, c) -> str:
    """Return Invalid or a side classification, prefixed with Right if needed."""
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    shortest, middle, longest = sorted((a, b, c))

    if shortest == longest:
        shape = "Equilateral"
    elif shortest == middle or middle == longest:
        shape = "Isosceles"
    else:
        shape = "Scalene"

    # Normalize by the hypotenuse to avoid squaring large side lengths.
    squared_legs = (shortest / longest) ** 2 + (middle / longest) ** 2
    if math.isclose(squared_legs, 1.0, rel_tol=1e-9, abs_tol=0.0):
        return "Right " + shape

    return shape
