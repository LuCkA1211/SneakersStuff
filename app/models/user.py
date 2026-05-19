from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base

class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str]
    surname: Mapped[str]
    password: Mapped[str]
    address: Mapped[str]
    city: Mapped[str]
    ban: Mapped[bool]
    admin: Mapped[bool]

    # 1-N (1) Relationship with orders
    orders_made: Mapped[list["Order"]] = relationship(back_populates="buyer_user")

    # 1-N (1) Relationship with payment methods
    payment_methods: Mapped[list["PaymentMethod"]] = relationship(back_populates="card_holder_user")

    # 1-N (1) Relationship with reviews made
    reviews_made: Mapped[list["Review"]] = relationship(
        foreign_keys="[Review.reviewer_username]",
        back_populates="reviewer_user"
    )

    # 1-N (1) Relationship with reviews received
    reviews_received: Mapped[list["Review"]] = relationship(
        foreign_keys="[Review.reviewed_username]",
        back_populates="reviewed_user"
    )

    # 1-N (1) Relationship with report made
    reports_made: Mapped[list["Report"]] = relationship(
        foreign_keys="[Report.reporter_username]",
        back_populates="reporter_user"
    )

    # 1-N (1) Relationship with report received
    reports_received: Mapped[list["Report"]] = relationship(
        foreign_keys="[Report.reported_username]",
        back_populates="reported_user"
    )

    # 1-N (1) Relationship with requests made
    requests_made: Mapped[list["Request"]] = relationship(back_populates="applicant_user")

    # 1-N (1) Relationship with products
    products_for_sale: Mapped[list["Product"]] = relationship(back_populates="seller_user")