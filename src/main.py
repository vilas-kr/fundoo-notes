from fastapi import FastAPI

from src.config.database import Base, engine
from src.config.logging_middleware import log_requests
from src.routes import user_routes, note_routes

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.middleware("http")(log_requests)

app.include_router(user_routes.router)
app.include_router(note_routes.router)