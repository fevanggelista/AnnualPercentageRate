import pytest
from test import tools_for_testing


from domain.base_rate import BaseRate
from domain.enum.base_range_enum import Range
from src.app.services import annual_percentage_rate_rules

base_rate_list = [BaseRate(loan_term = 36, percentage_first_range = 4.75, percentage_second_range = 5.75, percentage_third_range= 12.75), 
                  BaseRate(loan_term = 48, percentage_first_range = 5, percentage_second_range = 6, percentage_third_range = 13.25), 
                  BaseRate(loan_term = 60, percentage_first_range = 5.5, percentage_second_range = 6.65, percentage_third_range = 0)]


@pytest.mark.parametrize(
    "input_1,  input_2, expected", [
        (base_rate_list[0], Range.THIRD, 12.75),
        (base_rate_list[0], Range.SECOND, 5.75),
        (base_rate_list[0], Range.FIRST, 4.75),
        (base_rate_list[1], Range.THIRD, 13.25),
        (base_rate_list[1], Range.SECOND, 6),
        (base_rate_list[1], Range.FIRST, 5),
        (base_rate_list[2], Range.THIRD, None),
        (base_rate_list[2], Range.SECOND, 6.65),
        (base_rate_list[2], Range.FIRST, 5.5)
    ]
)


def test_if_get_percentage_by_range_index_corectly(input_1, input_2, expected):
    result = annual_percentage_rate_rules.get_percentage_by_range_index(base_rate= input_1, range_index = input_2)
    tools_for_testing.check_return(result, expected)
