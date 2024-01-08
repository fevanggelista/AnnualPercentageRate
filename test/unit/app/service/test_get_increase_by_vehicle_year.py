import pytest
from test import tools_for_testing

from src.app.services import annual_percentage_rate_rules


@pytest.mark.parametrize(
    "input_1,  expected", [
        (2013, 1),
        (2015, 0),
        (2016, 0),
    ]
)


def test_get_increase_by_vehicle_year(input_1, expected):
    result = annual_percentage_rate_rules.get_increase_by_vehicle_year(vehicle_year=input_1)
    tools_for_testing.check_return(result, expected)