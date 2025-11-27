from fastapi import FastAPI
from src.core.config import settings

from src.api.routes import tags

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

#app.include_router(authors.router, prefix="/authors", tags=["authors"])
#app.include_router(posts.router, prefix="/posts", tags=["posts"])
app.include_router(tags.router, prefix="/tags", tags=["tags"])

