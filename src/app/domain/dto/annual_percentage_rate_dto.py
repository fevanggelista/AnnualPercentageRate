""" Sample Request Module """
from typing import Optional
from pydantic import BaseModel, Field


class AnnualPercentageRateRequest(BaseModel):
    """This is a model to request a annual percentage rate"""
    amount:float = Field(..., description='Amount')
    loan_term:int = Field(..., description='Loan Term in months')
    credit_score:int = Field(..., description='Credit Score')
    vehicle_year:int = Field(..., description='Vehicle Year')
    mileage: float= Field(..., description= 'Vehicle Mileage')
    


class AnnualPercentageRateResponse(BaseModel):
    """This is a model for annual percentage rate response"""
    request: AnnualPercentageRateRequest
    annual_percentage_rate:float = Field(..., description='Annual Percentage Rate')
    messsages:Optional[str] = Field(..., description='Annual Percentage Rate')
