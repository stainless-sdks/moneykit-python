# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Institution"]


class Institution(BaseModel):
    color: str
    """The primary color of this institution, represented as hexcode."""

    country: Literal["US", "GB", "CA"]
    """An enumeration."""

    institution_id: str
    """MoneyKit's unique ID for this institution."""

    institution_id_aliases: List[str]
    """
    Alternative institution IDs that point to this institution that can be used for
    lookup.
    """

    is_featured: bool
    """True for institutions that should be visually promoted to the end-user."""

    name: str
    """The name of the institution."""

    color_dark: Optional[str] = None
    """The dark-mode primary color of this institution, represented as hexcode."""

    domain: Optional[str] = None
    """The domain of the institution's customer-facing website."""
