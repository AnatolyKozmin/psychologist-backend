from typing import List, Any, TypeVar, Generic 
from pydantic import BaseModel
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.future import select
from sqlalchemy import update as sqlalchemy_update, delete as sqlalchemy_delete, func
from loguru import logger
from sqlalchemy.ext.asyncio import AsyncSession
from app.dao.database import Base

# Объявляем типовой параметр Т с ограничением, что это наследник Base
T = TypeVar("T", bound=Base)

class BaseDAO(Generic[T]):
    model: type[T]

    @classmethod
    async def find_one_or_none_by_id(cls, data_id: int, session: AsyncSession):
        logger.info(f"Поиск {cls.model.__name__} с ID: {data_id}")
        try:
            query = select(cls.model).filter_by(id=data_id)
            result = await session.execute(query)
            record = result.scalar_one_or_none()
            if record: 
                logger.info(f"Запись с ID {data_id} найдена.")
            else: 
                logger.info(f"Запись с ID {data_id} не найдена")
            return record
        except SQLAlchemyError as e:
            logger.info(f"Ошибка при поиске записи с ID {data_id}: {e}")
            raise
        