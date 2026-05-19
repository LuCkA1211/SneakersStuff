from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

from app.utility.config import settings

echo = False
pool_pre_ping = True

def get_engine():
    return create_async_engine(
        url=settings.DATABASE_URL,
        pool_pre_ping=pool_pre_ping,
        echo=echo
    )

AsyncSessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=get_engine(),
    class_=AsyncSession
)

async def get_db_session():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except SQLAlchemyError:
            await session.rollback()
            raise
        finally:
            await session.close()