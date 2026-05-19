from sqlalchemy.ext.asyncio import AsyncSession

from app.models.product_description import ProductDescription
from app.repositories.product_description import ProductDescriptionRepository
from app.schemas.product_description import ProductDescriptionCreateRequest

class ProductDescriptionService:
    def __init__(self):
        self.repo = ProductDescriptionRepository()

    async def create_product_description(self, prod_desc_request: ProductDescriptionCreateRequest, db_session: AsyncSession):
        prod_desc = ProductDescription(
            brand=prod_desc_request.brand,
            model=prod_desc_request.model,
            color=prod_desc_request.color,
            release_year=prod_desc_request.release_year,
            category=prod_desc_request.category,
            insertion_date=prod_desc_request.insertion_date
        )

        # Auto-increment ID
        prod_desc = await self.repo.create(db_session, prod_desc)
        return prod_desc

service = ProductDescriptionService()