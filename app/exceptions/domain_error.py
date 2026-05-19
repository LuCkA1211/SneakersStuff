from fastapi import status

class DomainError(Exception):
    status_code: int = status.HTTP_400_BAD_REQUEST
    error: str = "An error occured"