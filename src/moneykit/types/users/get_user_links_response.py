# File generated from our OpenAPI spec by Stainless.

from typing import Dict

from ..._models import BaseModel

__all__ = ["GetUserLinksResponse"]


class GetUserLinksResponse(BaseModel):
    links: Dict[str, Links]
    """The set of links belonging to this user, as a dictionary of `{link_id:link}`."""
