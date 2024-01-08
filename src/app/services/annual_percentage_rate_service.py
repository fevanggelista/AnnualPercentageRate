""" Annual Percentage Rate Service Layer module"""
from ast import Return
from email import message
# from annual_percentage_rate_rules import get_increase_by_vehicle_year, is_minimum_loan_amount_for_loan_term_valid, \
#         is_maximum_loan_amount_for_a_credit_score_valid, get_base_rate, get_range_index, get_percentage_by_range_index, \
#         get_increase_by_vehicle_mileage
from app.domain.base_rate import BaseRate, base_rate_list, range_list, vehicle_year_increase

from app.domain.dto.annual_percentage_rate_dto import AnnualPercentageRateResponse,\
    AnnualPercentageRateRequest
from app.domain.enum.base_range_enum import Range
from app.services.annual_percentage_rate_rules import get_base_rate, get_increase_by_vehicle_mileage, \
    get_increase_by_vehicle_year, get_percentage_by_range_index, get_range_index, is_maximum_loan_amount_for_a_credit_score_valid, \
    is_minimum_loan_amount_for_loan_term_valid

def get_annual_percentage_rate(request: AnnualPercentageRateRequest):
    

    if request.loan_term < 0 or request.credit_score < 0:
        return None
    
    base_rate = get_base_rate(loan_term = request.loan_term)
    range_index =  get_range_index(credit_score = request.credit_score)
    initial_percentage = get_percentage_by_range_index(base_rate, range_index)

    if initial_percentage is None:
        return __new_empty_response(request, "Base Rate not found") 
    
    if not is_minimum_loan_amount_for_loan_term_valid(base_rate.loan_term, request.amount):
        return __new_empty_response(request, "Mininum loan amount for loan term is invalid")

    if not is_maximum_loan_amount_for_a_credit_score_valid(request.credit_score, request.amount):
        return __new_empty_response(request, "Maximum loan amount for a credit score is invalid")

    increase_by_vehicle = get_increase_by_vehicle_year(request.vehicle_year)

    increase_by_vehicle_mileage = get_increase_by_vehicle_mileage(request.mileage) 

    percentage_rate = initial_percentage + increase_by_vehicle + increase_by_vehicle_mileage

    return AnnualPercentageRateResponse(
        request=request,
        annual_percentage_rate = percentage_rate, 
        messsages= __get_message_increase(increase_by_vehicle, increase_by_vehicle_mileage)
    )


def __get_message_increase(increase_by_vehicle: float, increase_by_vehicle_mileage: float):
    message = "";
    if increase_by_vehicle > 0 :
        message = "There was an increase of " + str(increase_by_vehicle) + " because vehicle year. \n "
    
    if increase_by_vehicle_mileage > 0 :
        message = message + "There was an increase of " + str(increase_by_vehicle_mileage) + " because vehicle mileage. \n "

    return message


def __new_empty_response(request: AnnualPercentageRateRequest, message: str):
    return AnnualPercentageRateResponse(
            request=request,
            annual_percentage_rate = 0, 
            messsages = message )
    


            


         


             




