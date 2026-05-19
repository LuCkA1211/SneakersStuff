from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import ForeignKey

from app.models.base import Base

class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    rating: Mapped[int]
    comment: Mapped[str]

    # 1-N Relationship with users (reviewed)
    reviewed_username: Mapped[str] = mapped_column(ForeignKey("users.username"))
    reviewed_user: Mapped["User"] = relationship(
        foreign_keys=[reviewed_username],
        back_populates="reviews_received"
    )

    # 1-N Relationship with users (reviewer)
    reviewer_username: Mapped[str] = mapped_column(ForeignKey("users.username"))
    reviewer_user: Mapped["User"] = relationship(
        foreign_keys=[reviewer_username],
        back_populates="reviews_made"
    )