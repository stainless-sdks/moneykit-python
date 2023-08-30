# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["TransactionListParams"]


class TransactionListParams(TypedDict, total=False):
    account_ids: Optional[List[str]]
    """An optional list of account IDs to filter the results."""

    end_date: Optional[str]
    """
    The latest date for which data should be returned, formatted as YYYY-MM-DD.
    Defaults to today.
    """

    page: int
    """The page number to return."""

    size: int
    """The number of items to return per page."""

    start_date: Optional[str]
    """
    The earliest date for which data should be returned, formatted as YYYY-MM-DD.
    Defaults to 90 days before the `end_date`. <p>If you want to retrieve **all**
    transactions, use `1900-01-01`.
    """
