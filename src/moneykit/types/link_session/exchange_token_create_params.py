# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ExchangeTokenCreateParams"]


class ExchangeTokenCreateParams(TypedDict, total=False):
    exchangeable_token: Required[str]
    """The token returned to your front end by MoneyLink's onSuccess callback."""
