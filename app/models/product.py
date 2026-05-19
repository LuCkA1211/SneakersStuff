from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import ForeignKey

from app.models.base import Base

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    size: Mapped[str]
    price: Mapped[float]
    product_release_date: Mapped[str]

    # 1-N (N) Relationship with product_descriptions
    id_prod_description: Mapped[int] = mapped_column(ForeignKey("product_descriptions.id"))
    prod_description: Mapped["ProductDescription"] = relationship(back_populates="products")
    
    # 1-N (N) Relationship with orders
    id_order: Mapped[int | None] = mapped_column(ForeignKey("orders.id"))
    order: Mapped["Order | None"] = relationship(back_populates="order_products")

    # 1-N (N) Relationship with users
    seller_username: Mapped[str] = mapped_column(ForeignKey("users.username"))
    seller_user: Mapped["User"] = relationship(back_populates="products_for_sale")