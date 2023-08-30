# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .._models import BaseModel
from .institution import Institution

__all__ = ["GetInstitutionsResponse", "Cursors"]


class Cursors(BaseModel):
    next: Optional[str] = None
    """A cursor value pointing to the next result set."""


class GetInstitutionsResponse(BaseModel):
    cursors: Cursors
    """Pagination information."""

    institutions: List[Institution]
    """The list of institutions for this page."""
