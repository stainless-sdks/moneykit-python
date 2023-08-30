# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from datetime import datetime

from ..links import Account
from ..._models import BaseModel

__all__ = ["GetUserAccountsResponse", "Links"]


class Links(BaseModel):
    accounts: List[Account]

    last_synced_at: Optional[datetime] = None
    """An ISO-8601 timestamp indicating the last time that the account was updated."""


class GetUserAccountsResponse(BaseModel):
    links: Dict[str, Links]
    """
    The set of all accounts belonging to this user, as a dictionary of
    `{link_id:[accounts]}`.
    """
