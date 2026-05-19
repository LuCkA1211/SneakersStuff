from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, OperationalError

from app.repositories.generic_operations import GenericRepository
from app.models.user import User

class UserRepository(GenericRepository):
    
    async def get_by_username(self, db_session: AsyncSession, username: str):
        query = select(User).where(User.username == username)
        user = await db_session.execute(query)
        return user.scalars().first()