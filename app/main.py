from fastapi import FastAPI
from app.utility.lifespan import lifespan
from app.utility.exception_handler import exc_handler
from app.routers.user import router as user_router
from app.routers.admin import router as admin_router

app = FastAPI(lifespan=lifespan)
app.include_router(user_router)
app.include_router(admin_router)
exc_handler(app)