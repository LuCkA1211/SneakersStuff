from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.db import get_db_session
from app.models.user import User
from app.security.jwt import decode_access_token
from app.services.user import service
from app.exceptions.user_error import UserNotAuthorized

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db_session: AsyncSession = Depends(get_db_session)
) -> User:
    username = decode_access_token(token)
    user = await service.get_by_username(db_session, username)
    if not user:
        raise UserNotAuthorized()
    return user

async def is_admin(
    current_user: User = Depends(get_current_user)
):
    if not current_user.admin:
        raise UserNotAuthorized()
    return current_user