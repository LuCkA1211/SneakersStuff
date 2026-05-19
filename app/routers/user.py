from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.db import get_db_session
from app.schemas.user import UserCreateRequest, UserCreateResponse, ResponseCreateUser, TokenUser, UserResponse

from app.security.auth_dependencies import get_current_user
from app.services.user import service

router = APIRouter(prefix="/user")


@router.post(
    "/register",
    response_model=ResponseCreateUser
)
async def register(
    user_request: UserCreateRequest,
    db_session: AsyncSession = Depends(get_db_session)
) -> dict[str, UserCreateResponse]:
    user = await service.create_user(db_session, user_request)
    user_response = UserCreateResponse(username=user.username)
    return {
        "message" : "user created succesfully",
        "user" : user_response }

@router.post(
    "/login",
    response_model=TokenUser
)
async def login(
    user_request_form: OAuth2PasswordRequestForm = Depends(),
    db_session: AsyncSession = Depends(get_db_session)
):
    access_token = await service.login(db_session, user_request_form.username, user_request_form.password)
    return {
        "access_token" : access_token,
        "token_type" : "bearer"
    }

@router.get(
    "/profile",
    response_model=UserResponse
)
async def profile(
    user = Depends(get_current_user)
):
    return user