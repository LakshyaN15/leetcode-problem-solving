"""
Tests for: <number>. <Title>
Run from repo root:  pytest -q
Run just this file:  pytest path/to/test_two_sum.py
"""
import pytest

# Adjust the import to match your file/path:
from template_solution import Solution


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_two_sum(nums, target, expected):
    assert Solution().twoSum(nums, target) == expected
