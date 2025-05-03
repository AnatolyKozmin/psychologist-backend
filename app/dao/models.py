from datetime import datetime 
from typing import Optional, List 
from sqlalchemy import Integer, Text, ForeignKey, DateTime, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import time, date 
from dao.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(Integer, unique=True)
    username: Mapped[str | None]
    first_name: Mapped[str]
    last_name: Mapped[str | None]

    # ОТНОШЕНИЯ 
    bookings: Mapped[List["Booking"]] = relationship(back_populates="user")


class Doctor(Base):
    __tablename__ = "doctors"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    patronmic: Mapped[Optional[str]]
    special: Mapped[str]
    work_experience: Mapped[int] = mapped_column(Integer, nullable=False)
    adress: Mapped[str]
    description: Mapped[str] = mapped_column(Text)
    photo: Mapped[str]
    visit_card: Mapped[str]

    # ОТНОШЕНИЯ 
    bookings: Mapped[List["Booking"]] = relationship(back_populates="doctor")


class Booking(Base):
    __tablename__ = "booking"

    id: Mapped[str] = mapped_column(primary_key=True)
    doctor_id: Mapped[int] = mapped_column(ForeignKey("doctors.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    day_booking: Mapped[date] = mapped_column(nullable=False)
    time_bookings: Mapped[time] = mapped_column(nullable=False)
    booking_status: Mapped[str]
    created_ad: Mapped[datetime] = mapped_column(
        DateTime, 
        default=datetime.utcnow,
        nullable=False
    )

    # ОТНОШЕНИЯ
    doctor: Mapped["Doctor"] = relationship(back_populates="bookings")
    user: Mapped["User"] = relationship(back_populates="bookings")