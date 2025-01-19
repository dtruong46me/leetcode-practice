# tests/test_2025_01_19.py
import pytest
from solutions.solve_25_19_01 import Solution

@pytest.mark.parametrize("heightMap, expected", [
    (
        [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]],
        4
    ),
    (
        [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]],
        10
    )
])
def test_trapRainWater(heightMap, expected):
    assert Solution().trapRainWater(heightMap) == expected
