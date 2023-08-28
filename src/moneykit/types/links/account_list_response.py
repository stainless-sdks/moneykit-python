# File generated from our OpenAPI spec by Stainless.

from typing import List

from .account import Account
from ..._models import BaseModel
from ..link_common import LinkCommon

__all__ = ["AccountListResponse"]


class AccountListResponse(BaseModel):
    accounts: List[Account]
    """List of accounts."""

    link: LinkCommon
    """Link that the accounts are associated with."""
