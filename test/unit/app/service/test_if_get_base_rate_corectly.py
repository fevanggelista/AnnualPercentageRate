import pytest
from test import tools_for_testing

from src.app.services import annual_percentage_rate_rules


@pytest.mark.parametrize(

    "input_1,  expected", [
        (-1, None),
        (0, 36),
        (36, 36),
        (37, 48),
        (48, 48),
        (59, 60),
        (60, 60),
        (100, None)
    ]

)


def test_if_get_base_rate_corectly(input_1, expected):
    result = None
    base_rate = annual_percentage_rate_rules.get_base_rate(loan_term = input_1)

    if base_rate is not None:
        result = base_rate.loan_term

    tools_for_testing.check_return(result, expected)