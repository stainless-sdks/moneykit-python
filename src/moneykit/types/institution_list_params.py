# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["InstitutionListParams"]


class InstitutionListParams(TypedDict, total=False):
    cursor: Optional[str]
    """Cursor to fetch the next set of institutions.

    (You get this value from the previous call to `/institutions`.)
    """

    featured: Optional[bool]
    """If true, returns only featured institutions."""

    limit: int
    """A limit on the number of institutions to be returned."""

    name: Optional[str]
    """
    If provided, returns only institutions containing this name (wholly or as a
    prefix).
    """
