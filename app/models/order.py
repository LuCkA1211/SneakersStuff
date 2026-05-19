from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import ForeignKey

from app.models.base import Base

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    order_date: Mapped[str]

    # 1-N (1) Relationship with products
    order_products: Mapped[list["Product"]] = relationship(back_populates="order")

    # 1-N (N) Relationship with users
    buyer_user: Mapped["User"] = relationship(back_populates="orders_made")
    buyer_username: Mapped[str] = mapped_column(ForeignKey("users.username"))