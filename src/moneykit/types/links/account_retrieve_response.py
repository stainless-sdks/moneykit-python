# File generated from our OpenAPI spec by Stainless.

from .account import Account
from ..._models import BaseModel
from ..link_common import LinkCommon

__all__ = ["AccountRetrieveResponse"]


class AccountRetrieveResponse(BaseModel):
    account: Account

    link: LinkCommon
    """Link that the account is associated with."""
