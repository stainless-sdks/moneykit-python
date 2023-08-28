# File generated from our OpenAPI spec by Stainless.

from ..._models import BaseModel
from ..link_common import LinkCommon

__all__ = ["ExchangeTokenResponse"]


class ExchangeTokenResponse(BaseModel):
    link: LinkCommon
    """Details of the new link."""

    link_id: str
    """The unique ID associated with this link."""
