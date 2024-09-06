from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI
from fastapi.responses import ORJSONResponse

from app.auth.router import auth_router, users_router

from .config import settings
from .database import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


app = FastAPI(
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
)
main_router = APIRouter()

main_router.include_router(auth_router)
main_router.include_router(users_router)


app.include_router(main_router, prefix=settings.api.prefix_v1)
