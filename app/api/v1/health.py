from fastapi import APIRouter

from app.core.config import settings
from app.schemas.health import HealthResponse

router = APIRouter(tags=["health"])

@router.get("/health",response_model=HealthResponse, summary="Check the health of the application")
def get_health() -> HealthResponse:
    return HealthResponse(
        status="healthy",
        version=settings.app_version,
        app_name=settings.app_name,
    )