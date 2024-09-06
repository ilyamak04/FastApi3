from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from app.auth.models import User
from app.auth.schemas import UserCreate, UserRead
from app.config import settings

from .config import auth_backend
from .dependencies import get_user_manager

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

auth_router = APIRouter(prefix=settings.api.v1.auth, tags=["Auth"])
auth_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
)
auth_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
)
