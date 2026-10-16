# 325Module6HW

## Triangle classifier

`triangle.py` provides `is_valid_triangle(a, b, c)` and
`classify_triangle(a, b, c)`. Inputs are numeric side lengths; parsing text or
handling nonnumeric objects is outside this interface. Nonpositive and nonfinite
lengths, failed triangle inequalities, and degenerate triangles return `False`
from validation and `"Invalid"` from classification.

Valid triangles are classified as `"Equilateral"`, `"Isosceles"`, or `"Scalene"`.
Right triangles receive the prefix `"Right "`. Side equality uses exact equality.
The right-angle check uses `math.isclose` with relative tolerance `1e-9` and zero
absolute tolerance, after dividing each side by the longest side. This checks
the Pythagorean relation while allowing floating-point rounding and avoiding
overflow from squaring large lengths.

An equilateral triangle has three 60-degree angles. A right triangle must have
a 90-degree angle, so an equilateral triangle cannot be right.

## AI-use disclosure

OpenAI Codex assisted with interpreting the assignment, planning, and drafting
the Part 1 implementation and documentation. Part 1 was checked with direct
example calls;
