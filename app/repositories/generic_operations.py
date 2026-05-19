from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from typing import Optional

from app.database.db import get_db_session

class GenericRepository():

    async def create(
        self,
        db_session: AsyncSession,
        obj: object
    ) -> Optional[object]:
        db_session.add(obj)
        await db_session.flush()
        await db_session.refresh(obj)
        return obj