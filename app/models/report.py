from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import ForeignKey

from app.models.base import Base

class Report(Base):
    __tablename__ = "reports"

    id: Mapped[int] = mapped_column(primary_key=True)
    report_detail: Mapped[str]
    report_date: Mapped[str]

    # 1-N Relationship with user (reported)
    reported_username: Mapped[str] = mapped_column(ForeignKey("users.username"))
    reported_user: Mapped["User"] = relationship(
        foreign_keys=[reported_username],
        back_populates="reports_received"
    )

    # 1-N Relationship with user (reporter)
    reporter_username: Mapped[str] = mapped_column(ForeignKey("users.username"))
    reporter_user: Mapped["User"] = relationship(
        foreign_keys=[reporter_username],
        back_populates="reports_made"
    )