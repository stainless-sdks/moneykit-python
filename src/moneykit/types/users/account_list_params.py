# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["AccountListParams"]


class AccountListParams(TypedDict, total=False):
    account_id: Optional[List[str]]
    """If present, filters results to accounts matching the given IDs."""

    institution_id: Optional[List[str]]
    """If present, filters results to accounts at institutions matching the given IDs."""
