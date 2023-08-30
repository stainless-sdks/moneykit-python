# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import TypedDict

__all__ = ["LinkUpdateParams"]


class LinkUpdateParams(TypedDict, total=False):
    tags: Optional[List[str]]
    """Arbitrary strings used to describe this link."""

    webhook: Optional[str]
    """
    Sets the webhook URL for this link. To remove a webhook for this link, set to
    `null`.
    """
