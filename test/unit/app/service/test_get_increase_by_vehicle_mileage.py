import pytest
from test import tools_for_testing

from src.app.services import annual_percentage_rate_rules


@pytest.mark.parametrize(
    "input_1,  expected", [
        (105000, 2),
        (999, 0),
    ]
)


def test_get_increase_by_vehicle_mileage(input_1, expected):
    result = annual_percentage_rate_rules.get_increase_by_vehicle_mileage(vehicle_mileage=input_1)
    tools_for_testing.check_return(result, expected)