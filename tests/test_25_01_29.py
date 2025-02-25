# tests/test_2025_29_01.py
import pytest
from solutions.solve_25_29_01 import Solution

@pytest.mark.parametrize("grid, expected", [
    (
        [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]],
        7
    ),
    (
        [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]],
        1
    )
])
def test_findMaxFish(grid, expected):
    assert Solution().findMaxFish(grid) == expected
