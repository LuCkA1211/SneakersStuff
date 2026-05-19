from app.schemas.user import UserCreateRequest
from app.repositories.user import UserRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from app.models.user import User
from app.security.hashing import hash_password, verify_password
from app.security.jwt import create_access_token

from app.exceptions.user_error import UsernameOrEmailAlreadyExist, InvalidCredential, BannedUser

class UserService:
    
    def __init__(self):
        self.repo = UserRepository()

    async def create_user(self, db_session: AsyncSession, user_request: UserCreateRequest) -> User:
        
        hashed_password = hash_password(user_request.password)
        user = User(
            username=user_request.username,
            email=user_request.email,
            name=user_request.name,
            surname=user_request.surname,
            password=hashed_password,
            address=user_request.address,
            city=user_request.city,
            ban=False,
            admin=False
        )

        try:
            user = await self.repo.create(db_session, user)
        except IntegrityError:
            raise UsernameOrEmailAlreadyExist()
        
        return user
    
    async def login(self, db_session: AsyncSession, username: str, password: str):
        
        user = await self.get_by_username(db_session, username)
        
        if not user or not verify_password(password, user.password):
            raise InvalidCredential()
        if user.ban:
            raise BannedUser()
        access_token = create_access_token(
            data={ "sub" : user.username }
        )
        return access_token
    
    async def get_by_username(self, db_session: AsyncSession, username: str):
        user = await self.repo.get_by_username(db_session, username)
        return user
        
service = UserService()