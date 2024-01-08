import pytest
from test import tools_for_testing

from src.app.services import annual_percentage_rate_rules


@pytest.mark.parametrize(
    "input_1, input_2,  expected", [
        (24, 5000.0, True),
        (36, 5000.0, True),
        (48, 10000.0, True),
        (60, 15000.0, True),
        (60, 16000.0, True),
        (36, 3000.0, False),
        (48, 9000.0, False),
        (60, 14000.0, False)
    ]
)


def test_is_minimum_loan_amount_for_loan_term_valid(input_1, input_2, expected):
    result = annual_percentage_rate_rules.is_minimum_loan_amount_for_loan_term_valid(loan_term=input_1, amount=input_2)
    tools_for_testing.check_return(result, expected)