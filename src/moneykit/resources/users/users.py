# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .links import Links, AsyncLinks
from .accounts import Accounts, AsyncAccounts
from ..._resource import SyncAPIResource, AsyncAPIResource
from .transactions import Transactions, AsyncTransactions

if TYPE_CHECKING:
    from ..._client import Moneykit, AsyncMoneykit

__all__ = ["Users", "AsyncUsers"]


class Users(SyncAPIResource):
    transactions: Transactions
    accounts: Accounts
    links: Links

    def __init__(self, client: Moneykit) -> None:
        super().__init__(client)
        self.transactions = Transactions(client)
        self.accounts = Accounts(client)
        self.links = Links(client)


class AsyncUsers(AsyncAPIResource):
    transactions: AsyncTransactions
    accounts: AsyncAccounts
    links: AsyncLinks

    def __init__(self, client: AsyncMoneykit) -> None:
        super().__init__(client)
        self.transactions = AsyncTransactions(client)
        self.accounts = AsyncAccounts(client)
        self.links = AsyncLinks(client)
