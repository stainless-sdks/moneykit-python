# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .introspect import Introspect, AsyncIntrospect
from ..._resource import SyncAPIResource, AsyncAPIResource

if TYPE_CHECKING:
    from ..._client import Moneykit, AsyncMoneykit

__all__ = ["Auth", "AsyncAuth"]


class Auth(SyncAPIResource):
    introspect: Introspect

    def __init__(self, client: Moneykit) -> None:
        super().__init__(client)
        self.introspect = Introspect(client)


class AsyncAuth(AsyncAPIResource):
    introspect: AsyncIntrospect

    def __init__(self, client: AsyncMoneykit) -> None:
        super().__init__(client)
        self.introspect = AsyncIntrospect(client)
