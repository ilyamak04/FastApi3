from contextlib import asynccontextmanager
from fastapi import FastAPI, ApiRouter
from app.config import settings


from app.database import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


router = ApiRouter()
app = FastAPI()

app.include_router(
    router,
    prefix=settings.api.prefix,
    host=settings.run.host,
    port=settings.run.port,
)
