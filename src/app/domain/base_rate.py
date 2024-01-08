""" Sample Request Module """
from pydantic import BaseModel, Field, validator

from app.domain.enum.base_range_enum import Range

class BaseRate(BaseModel):
    """This is a model of base rate"""
    loan_term:int = Field(..., description='Loan Term')
    percentage_first_range:float = Field(..., description='Percentage of first range of credt scor')
    percentage_second_range:float = Field(..., description='Percentage of second range of credt score')
    percentage_third_range:float = Field(..., description='Percentage of third range of credt score')

    @validator('loan_term')
    def loan_term_must_be_positive_number(cls, v):
        if v < 0 :
            raise ValueError('Loan Term must be positive number')
        return v

    @validator('loan_term')
    def loan_term_must_be_bigger_or_equal_fist_loan_term(cls, v):
        if v <= 0 :
            raise ValueError('Loan Term must be bigger or equal than fist_loan_term param')
        return v

class BaseRange(BaseModel):
    """This is a model of base range"""
    loan_term:int = Field(..., description='Loan Term')
    range_index:Range = Field(..., description='Number that represent the range of credit score on base rate table')
    credit_score_start:int = Field(..., description='Start of range of credit score')


class MinimumLoanAmount(BaseModel):
    """This is a model of base range"""
    loan_term:int = Field(..., description='Loan Term')
    minimum_loan_amount:float = Field(..., description='The minimum loan amount')

class MaximumLoanAmount(BaseModel):
    """This is a model of base range"""
    credit_score:int = Field(..., description='Loan Term')
    maximum_loan_amount:float = Field(..., description='The minimum loan amount')



base_rate_list = [BaseRate(loan_term = 36, percentage_first_range = 4.75, percentage_second_range = 5.75, percentage_third_range= 12.75), 
                  BaseRate(loan_term = 48, percentage_first_range = 5, percentage_second_range = 6, percentage_third_range = 13.25), 
                  BaseRate(loan_term = 60, percentage_first_range = 5.5, percentage_second_range = 6.65, percentage_third_range = 0)]

range_list = [BaseRange(loan_term = 36, range_index = Range.THIRD, credit_score_start = 0),
              BaseRange(loan_term = 48, range_index = Range.SECOND, credit_score_start = 600),
              BaseRange(loan_term = 60, range_index = Range.FIRST, credit_score_start = 700)]

minimum_loan_amount_list = [ MinimumLoanAmount(loan_term = 36, minimum_loan_amount = 5000),
                             MinimumLoanAmount(loan_term = 48, minimum_loan_amount = 10000),
                             MinimumLoanAmount(loan_term = 60, minimum_loan_amount = 15000)]


maximum_loan_amount_list = [ MaximumLoanAmount(credit_score = 0, maximum_loan_amount = 50000),
                             MaximumLoanAmount(credit_score = 600, maximum_loan_amount = 75000),
                             MaximumLoanAmount(credit_score = 700, maximum_loan_amount = 100000)]


vehicle_year_increase = (2015, 1.0)

vehicle_mileage_increase = (100000, 2.0)



