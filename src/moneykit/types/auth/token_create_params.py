# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["TokenCreateParams"]


class TokenCreateParams(TypedDict, total=False):
    client_id: Optional[str]
    """Your application's MoneyKit client ID."""

    client_secret: Optional[str]
    """Your application's MoneyKit client secret."""

    grant_type: Optional[str]
    """Token grant type. Only `client_credentials` supported."""

    scope: str
    """
    Actions to be allowed for this token, given as one or more strings separated by
    spaces. If omitted, all actions allowed for your application will be granted to
    this token.
    """
