# File generated from our OpenAPI spec by Stainless.

from ..._models import BaseModel

__all__ = ["GenerateAccessTokenResponse"]


class GenerateAccessTokenResponse(BaseModel):
    access_token: str
    """Short-lived access token."""

    expires_in: int
    """How long until `access_token` expires in seconds."""

    token_type: str
    """Always "bearer"."""
