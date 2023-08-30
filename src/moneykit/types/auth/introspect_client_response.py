# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["IntrospectClientResponse", "App"]


class App(BaseModel):
    id: str
    """Your app's ID."""

    app_name: str
    """Your app's name."""


class IntrospectClientResponse(BaseModel):
    app: App
    """Customer Application for a specific environment"""

    client_id: str
    """Your application's MoneyKit client ID."""

    client_name: str
    """Friendly API client name for identification."""

    scope: str
    """Actions allowed by the client."""

    disabled_at: Optional[datetime] = None
    """Set to timestamp if the client has been disabled."""
