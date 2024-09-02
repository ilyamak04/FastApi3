from typing import TYPE_CHECKING

from fastapi import Depends
from fastapi_users.authentication import BearerTransport
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)
from sqlalchemy import ForeignKey, Integer
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import Mapped, mapped_column

from ..models import Base

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession

bearer_transport = BearerTransport(
    # TODO: update url
    tokenUrl="auth/jwt/login"
)


class AccessToken(Base, SQLAlchemyBaseAccessTokenTable):
    __tablename__ = "access_token"
    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("user.id", ondelete="cascade"), nullable=False
    )

    @classmethod
    def get_db(cls, session: AsyncSession):
        return SQLAlchemyAccessTokenDatabase(session, cls)
