from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi import APIRouter
from app.config import settings
from fastapi.responses import ORJSONResponse

from app.database import db_helper


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
