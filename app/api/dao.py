from datetime import date, timedelta, datetime, time, timezone
from typing import List
from fastapi import HTTPException
from loguru import logger
from sqlalchemy import select, and_, func 
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from dao.base import BaseDAO
from dao.models import User, Doctor, Booking


class UserDAO(BaseDAO[User]):
    model = User

    @classmethod
    async def get_user_id(cls, session: AsyncSession, telegram_id: int) -> int | None:
        query = select(cls.model.id).filter_by(telegram_id=telegram_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()
    

class BookingDAO(BaseDAO[Booking]):
    model = Booking 

    @classmethod 
    async def count_user_booking(cls, session: AsyncSession, user_id: int) -> int:
        query = select(func.count()).where(cls.model.user_id == user_id)
        result = await session.execute(query)
        return result.scalar_one()
    
    @classmethod 
    async def get_user_bookings_with_doctor_info(cls, session: AsyncSession, user_id: int):
        query = (
            select(cls.model)
            .options(joinedload(cls.model.doctor))
            .where(cls.model.user_id == user_id)
            .order_by(cls.model.day_booking, cls.model.time_booking)
        )
        result = await session.execute(query)
        result_draft = result.unique().scalars().all()
        data_list = []
        for info in result_draft():
            data_list.append({
                'id': info.id,
                'day_booking': info.time_booking.strftime("%Y-%m-%d"),
                'time_booking': info.time_booking.strftime("%H:%M"),
                'special': info.doctor.special,
                'doctor_full_name': f'{info.doctor.first_name} {info.doctor.last_name} {info.doctor.patronymic}',
            })
        return data_list
    
   


class DoctorDAO(BaseDAO[Doctor]):
    model = Doctor 

    @classmethod
    async def create_time_for_reception(cls, session: AsyncSession, doctor_id: int):
        query = select(cls.model).where(doctor_id == id)
        result = await session.execute(query)
        
        