from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.db import get_db_session
from app.models.user import User
from app.schemas.product_description import ProductDescriptionCreateRequest, ProductDescriptionCreateResponse
from app.security.auth_dependencies import is_admin
from app.services.product_description import service as product_description_service

router = APIRouter(prefix="/admin")

@router.get("/")
async def home(
    admin: User = Depends(is_admin)
):
    return { "message" : f"Welcome back {admin.username}" }

@router.post(
    "/product_description",
    response_model=ProductDescriptionCreateResponse
)
async def create_product_description(
    product_description_request: ProductDescriptionCreateRequest,
    admin: User = Depends(is_admin),
    db_session: AsyncSession = Depends(get_db_session)
) -> ProductDescriptionCreateResponse:
    return await product_description_service.create_product_description(product_description_request, db_session)