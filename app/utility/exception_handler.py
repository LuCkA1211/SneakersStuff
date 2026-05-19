from starlette.responses import JSONResponse

from fastapi import Request, FastAPI

from app.exceptions.domain_error import DomainError
from sqlalchemy.exc import OperationalError

def exc_handler(app: FastAPI):

    @app.exception_handler(DomainError)
    async def domain_error_handler(request: Request, exc: DomainError):
        return JSONResponse(
            status_code=exc.status_code,
            content={ "detail" : exc.error }
        )
    
    @app.exception_handler(OperationalError)
    async def operational_error_handler(request: Request, exc: OperationalError):
        return JSONResponse(
            status_code=503,
            content={ "detail" : "Database error" }
        )