from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String


class Base(DeclarativeBase):
    pass


class CompanyLogoDailyDB(Base):
    __tablename__ = "active"
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    domain: Mapped[str] = mapped_column(String(30), nullable=False, index=True)
    active_flag: Mapped[int] = mapped_column(nullable=False, index=True, default=0)
    hit_rate: Mapped[int] = mapped_column(nullable=False, index=False)
