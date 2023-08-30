# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["TransactionSyncParams"]


class TransactionSyncParams(TypedDict, total=False):
    cursor: Optional[str]
    """A cursor value representing the last update requested.

    If included, the response will only return changes after this update. If
    omitted, a complete history of updates will be returned. This value must be
    stored by the client as we do not keep track of customer cursors.
    """

    size: int
    """The number of items to return."""
