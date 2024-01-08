# API to get Annual Percentage Rate (APR) for a vehicle loan

## Service with one HTTP endpoint that returns the annual percentage rate (APR) for a vehicle loan

## Tech
- [FastApi] - Modern, fast (high-performance), web framework for building APIs with Pyton 3.6+!
- [Pydantic] -  Provides a dataclass decorator which creates python dataclasses with input data parsing and validation.
- [uvicorn] - Lightning-fast ASGI server implementation, using uvloog and httptools.

## Installation

### Using CMD:
python -m venv pythonenv
.\pythonenv\Scripts\activate
cd src
python -m pip install --upgrade pip
pip install -r ../requirements.txt
uvicorn app.main:app

### Using Docker:

docker build -t apr_api
docker run -d --name c_apr_api -p 8000:8000 apr_api

## Documentation

- Swagger documentation: http://localhost:docs
- Redoc documentation: http://localhost:redocs

## Pytest
- https://code.visualstudio.com/docs/python/testing
