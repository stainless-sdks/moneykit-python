# File generated from our OpenAPI spec by Stainless.

from typing import List

from ..._models import BaseModel

__all__ = ["JwkSet"]


class JwkSet(BaseModel):
    keys: List[object]
    """JWKs used for validating MoneyKit-issued tokens."""
