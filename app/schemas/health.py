from typing import Literal

from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    status: Literal["healthy", "unhealthy"] = Field(
        ..., description="The status of the health check"
    )
    version: str = Field(..., description="The version of the application")
    app_name: str = Field(..., description="The name of the application")
