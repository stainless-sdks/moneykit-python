# File generated from our OpenAPI spec by Stainless.

from .._models import BaseModel

__all__ = ["CreateLinkSessionResponse"]


class CreateLinkSessionResponse(BaseModel):
    link_session_token: str
    """A unique token identifying this link session."""
