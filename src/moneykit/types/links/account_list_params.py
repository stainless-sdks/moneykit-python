# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["AccountListParams"]


class AccountListParams(TypedDict, total=False):
    account_ids: Optional[List[str]]
    """An optional list of account IDs to filter the results."""
