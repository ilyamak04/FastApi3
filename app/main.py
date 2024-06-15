from fastapi import FastAPI, ApiRouter
from app.config import settings


router = ApiRouter()
app = FastAPI()

app.include_router(
    router,
    prefix=settings.api.prefix,
    host=settings.run.host,
    port=settings.run.port,
)
