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

## Running the unit tests

From the project folder in Git Bash:

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install -r requirements.txt
python -m pytest test_triangle.py -v
```

If `.venv` already exists, skip the creation command. To run all available
tests, use `python -m pytest -v`.

## Equivalence classes and boundaries

| Class or boundary | Example | Expected result |
|---|---|---|
| Negative side | `(-1, 3, 3)` | `Invalid` |
| Zero-length boundary | `(0, 3, 3)` | `Invalid` |
| Positive sides below the triangle-inequality threshold | `(1, 2, 4)` | `Invalid` |
| Degenerate equality boundary | `(1, 2, 3)` | `Invalid` |
| Valid, all sides equal | `(3, 3, 3)` | `Equilateral` |
| Valid, exactly two sides equal, non-right | `(3, 3, 4)` | `Isosceles` |
| Valid, all sides different, non-right | `(4, 5, 6)` | `Scalene` |
| Right, all sides different | `(3, 4, 5)` | `Right Scalene` |
| Right, two sides equal, non-integer hypotenuse | `(5, 5, 5 * math.sqrt(2))` | `Right Isosceles` |

The triangle inequality requires a strict greater-than comparison: sums below
or equal to the longest side are invalid, and sums above it can form valid
triangles. The non-integer right-triangle case exercises floating-point
rounding in the Pythagorean check. String assertions still use `==` because
the returned labels must match exactly.

## Copilot Review Log

GitHub Copilot autocomplete drafted the unit-test bodies. Suggestions were
reviewed against the assignment specification before finalizing them.

| Test | Copilot-suggested? | Kept / edited / rejected | Why |
|---|---|---|---|
| `test_equilateral` | Yes | Kept | Three equal positive sides require `Equilateral`. |
| `test_zero_side` | Yes | Edited | Changed `(0, 3, 4)` to `(0, 3, 3)` as an optional boundary refinement. The original expected result was correct; this was not a Copilot mistake. |
| `test_negative_side` | Yes | Kept | A negative side requires `Invalid`. |
| `test_triangle_inequality_failure` | Yes | Edited | Suggested `(1, 2, 3)` tested equality rather than the requested strict failure. Changed to `(1, 2, 4)`. |
| `test_degenerate_triangle` | Yes | Kept | `(1, 2, 3)` exercises the explicitly invalid equality boundary. |
| `test_isosceles` | Yes | Edited | Final review corrected the saved expected label from `Isoceles` to the specification's `Isosceles`, along with the test name. |
| `test_scalene` | Yes | Edited | Copilot incorrectly expected `Scalene` for `(3, 4, 5)`, which requires `Right Scalene`. Changed inputs to the non-right triangle `(4, 5, 6)`. |
| `test_right_scalene` | Yes | Kept | `(3, 4, 5)` has different sides and satisfies the Pythagorean theorem. |
| `test_right_isosceles_non_integer` | Yes | Kept | Equal legs and a hypotenuse of `5 * math.sqrt(2)` require `Right Isosceles`; covers the required non-integer case. |

Verification: all nine unit tests passed in the project's virtual environment.

## AI-use disclosure

OpenAI Codex assisted with interpreting the assignment, planning, and drafting
the Part 1 implementation and documentation. Part 1 was checked with direct
example calls. 
GitHub Copilot autocomplete drafted the Part 2 unit tests;
the student reviewed the suggestions with Codex assistance against the
specification, corrected input-selection and expected-label errors, and ran
all nine tests successfully. 
Codex also helped with environment setup and
the README coverage explanation and review log. The student-authored
acceptance criteria and acceptance test are still pending.
