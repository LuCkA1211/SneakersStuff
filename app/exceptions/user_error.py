from app.exceptions.domain_error import DomainError
from fastapi import status

class UsernameAlreadyExists(DomainError):
    status_code: int = status.HTTP_409_CONFLICT
    error: str = "Username already exists"

class EmailAlreadyExists(DomainError):
    status_code: int = status.HTTP_409_CONFLICT
    error: str = "Email already exists"

class UsernameOrEmailAlreadyExist(DomainError):
    status_code: int = status.HTTP_409_CONFLICT
    error: str = "Username or email already exist"

class InvalidCredential(DomainError):
    status_code: int = status.HTTP_401_UNAUTHORIZED
    error: str = "Invalid credential"

class UserNotAuthorized(DomainError):
    status_code: int = status.HTTP_401_UNAUTHORIZED
    error: str = "User not authorized"

class BannedUser(DomainError):
    status_code: int = status.HTTP_403_FORBIDDEN
    error: str = "User banned"