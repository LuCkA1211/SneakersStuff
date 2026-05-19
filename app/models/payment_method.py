from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import ForeignKey

from app.models.base import Base

# Assuming that the only possible payment method is the credit card
class PaymentMethod(Base):
    __tablename__ = "payment_method"

    card_number: Mapped[int] = mapped_column(primary_key=True)
    expiry: Mapped[str]
    cvv: Mapped[int]
    card_holder_name: Mapped[str]

    # 1-N Relationship with user
    card_holder_username: Mapped[str] = mapped_column(ForeignKey("users.username"))
    card_holder_user: Mapped["User"] = relationship(back_populates="payment_methods")