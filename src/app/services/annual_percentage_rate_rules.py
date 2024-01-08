""" Annual Percentage Rate Service Layer module"""

from app.domain.base_rate import BaseRate, base_rate_list, range_list, vehicle_year_increase, maximum_loan_amount_list, minimum_loan_amount_list, vehicle_year_increase, vehicle_mileage_increase
from app.domain.enum.base_range_enum import Range



def __return_none_if_less_than_or_equal_to_zero(number: float):
    if number <= 0:
        return None
    return number
    

def is_minimum_loan_amount_for_loan_term_valid(loan_term: int, amount: float):
    minimum_loan_amount_list_sorted = sorted(minimum_loan_amount_list, key=lambda list: list.loan_term, reverse = True)
    for item in minimum_loan_amount_list_sorted:
        if loan_term <= item.loan_term and amount >= item.minimum_loan_amount:
            return True

    return False


def is_maximum_loan_amount_for_a_credit_score_valid(credit_score: int, amount: float):
    maximum_loan_amount_list_sorted = sorted(maximum_loan_amount_list, key=lambda list: list.credit_score, reverse = True)
    for item in maximum_loan_amount_list_sorted:
        if credit_score <= item.credit_score :
            maximum_loan_amount = item.maximum_loan_amount

    if maximum_loan_amount is None:
        return False

    if amount <= maximum_loan_amount:
        return True

    return False


def get_increase_by_vehicle_year(vehicle_year: int):
    if vehicle_year < vehicle_year_increase[0]:
        return vehicle_year_increase[1]
    return 0


def get_increase_by_vehicle_mileage(vehicle_mileage: int):
    if vehicle_mileage > vehicle_mileage_increase[0]:
        return vehicle_mileage_increase[1]
    return 0

def get_base_rate(loan_term):
    base_rate = None

    if loan_term < 0:
        return base_rate 
    
    base_rate_list_sorted = sorted(base_rate_list, key=lambda list: list.loan_term, reverse = True)
    for BaseRate in base_rate_list_sorted:
        if loan_term <= BaseRate.loan_term :
            base_rate = BaseRate
    return base_rate


def get_range_index(credit_score):
    range_index = Range.THIRD

    if credit_score < 0:
        return range_index 

    for item in range_list:
        if credit_score >= item.credit_score_start:
            range_index = item.range_index  
    
    return range_index
                       

def get_percentage_by_range_index(base_rate: BaseRate, range_index: Range):
    if range_index.value == Range.FIRST.value:
        return __return_none_if_less_than_or_equal_to_zero(base_rate.percentage_first_range)

    elif range_index.value  == Range.SECOND.value:
        return __return_none_if_less_than_or_equal_to_zero(base_rate.percentage_second_range)

    elif range_index.value  == Range.THIRD.value:
        return __return_none_if_less_than_or_equal_to_zero(base_rate.percentage_third_range)



 


 