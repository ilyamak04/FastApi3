from fastapi_users import FastAPIUsers

from .config import auth_backend
from .dependencies import get_user_manager
from .models import User

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)
