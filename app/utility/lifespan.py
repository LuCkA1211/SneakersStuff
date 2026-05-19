from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.database.db import get_engine
from app.models.base import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield
    await engine.dispose()