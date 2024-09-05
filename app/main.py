from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI
from fastapi.responses import ORJSONResponse

from app.config import settings
from app.database import db_helper

from .auth.router import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


router = APIRouter()

app = FastAPI(
    lifespan=lifespan,
    default_response_class=ORJSONResponse,
)

app.include_router(
    router,
    prefix=settings.api.prefix,
)
router.include_router(router=auth_router)
