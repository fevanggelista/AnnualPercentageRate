import pytest
from test import tools_for_testing

from src.app.services import annual_percentage_rate_rules




@pytest.mark.parametrize(

    "input_1, input_2, expected", [
        (0, 50000, True),
        (600, 75000, True),
        (700, 100000, True),
        (700, 100001, False),
        (600, 750001, False),
        (200, 500001, False),
    ]

)


def test_is_maximum_loan_amount_for_a_credit_score_valid(input_1, input_2, expected):
    result = annual_percentage_rate_rules.is_maximum_loan_amount_for_a_credit_score_valid(credit_score=input_1, amount=input_2)
    tools_for_testing.check_return(result, expected)