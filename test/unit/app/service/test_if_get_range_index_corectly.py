import pytest
from test import tools_for_testing

from domain.enum.base_range_enum import Range
from src.app.services import annual_percentage_rate_rules


@pytest.mark.parametrize(
    "input_1,  expected", [
        (-1, Range.THIRD),
        (0, Range.THIRD),
        (500, Range.THIRD),
        (600, Range.SECOND),
        (699, Range.SECOND),
        (700, Range.FIRST),
        (99999, Range.FIRST)
    ]
)


def test_if_get_range_index_corectly(input_1, expected):
    result = annual_percentage_rate_rules.get_range_index(credit_score = input_1)
    tools_for_testing.check_return(result.value, expected.value)
