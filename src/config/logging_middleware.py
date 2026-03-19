from fastapi import Request
from src.config.logger import logger
import time

async def log_requests(request: Request, call_next):
    start = time.time()

    logger.bind(
        method=request.method,
        path=request.url.path
    ).info("Incoming request")

    response = await call_next(request)

    duration = time.time() - start

    logger.bind(
        method=request.method,
        path=request.url.path,
        status_code=response.status_code,
        duration=round(duration, 3)
    ).info("Request completed")

    return response