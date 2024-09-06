from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.auth.models import AccessToken, User
from app.database import db_helper

from .service import UserManager


async def get_user_db(session: AsyncSession = Depends(db_helper.session_getter)):
    yield SQLAlchemyUserDatabase(session, User)


async def get_access_token_db(
    session: AsyncSession = Depends(db_helper.session_getter),
):
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
