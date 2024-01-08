"""Sample controller module"""

from fastapi import APIRouter, Depends, HTTPException

from app.domain.dto.annual_percentage_rate_dto import AnnualPercentageRateRequest, \
                                                        AnnualPercentageRateResponse

from app.services.annual_percentage_rate_service import get_annual_percentage_rate                                                

router = APIRouter()

@router.get("/annual-percentage-rate", response_model=AnnualPercentageRateResponse)
async def get_by_model(request: AnnualPercentageRateRequest = Depends()):
    """ Doc String"""
    
    response = get_annual_percentage_rate(request)

    if response.annual_percentage_rate == 0:
        raise HTTPException(status_code=404, detail=response.messsages)

    return response