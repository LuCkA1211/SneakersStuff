from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import ForeignKey

from app.models.base import Base

class Request(Base):
    __tablename__ = "requests"

    id: Mapped[int] = mapped_column(primary_key=True)
    brand_request: Mapped[str]
    model_request: Mapped[str]
    colour_request: Mapped[str]
    release_year_request: Mapped[str]
    date_of_request: Mapped[str]

    # 1-N (N) Relationship with users
    applicant_username: Mapped[str] = mapped_column(ForeignKey("users.username"))
    applicant_user: Mapped["User"] = relationship(back_populates="requests_made")