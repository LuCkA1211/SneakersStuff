from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

class ProductDescription(Base):
    __tablename__ = "product_descriptions"

    id: Mapped[int] = mapped_column(primary_key=True)
    brand: Mapped[str]
    model: Mapped[str]
    color: Mapped[str]
    release_year: Mapped[int]
    category: Mapped[str]
    insertion_date: Mapped[str]  # Simplification

    # 1-N (1) Relationship with product
    products: Mapped[list["Product"]] = relationship(back_populates="prod_description")