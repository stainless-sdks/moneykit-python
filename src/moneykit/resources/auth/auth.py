# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .token import Token, AsyncToken
from .introspect import Introspect, AsyncIntrospect
from ..._resource import SyncAPIResource, AsyncAPIResource

if TYPE_CHECKING:
    from ..._client import Moneykit, AsyncMoneykit

__all__ = ["Auth", "AsyncAuth"]


class Auth(SyncAPIResource):
    token: Token
    introspect: Introspect

    def __init__(self, client: Moneykit) -> None:
        super().__init__(client)
        self.token = Token(client)
        self.introspect = Introspect(client)


class AsyncAuth(AsyncAPIResource):
    token: AsyncToken
    introspect: AsyncIntrospect

    def __init__(self, client: AsyncMoneykit) -> None:
        super().__init__(client)
        self.token = AsyncToken(client)
        self.introspect = AsyncIntrospect(client)
