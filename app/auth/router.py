from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from ..config import settings
from .config import auth_backend
from .dependencies import get_user_manager
from .models import User

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router = APIRouter(prefix=settings.api.v1.auth, tags=["Auth"])

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
)
