# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING

from .jwks import Jwks, AsyncJwks
from ..._resource import SyncAPIResource, AsyncAPIResource

if TYPE_CHECKING:
    from ..._client import Moneykit, AsyncMoneykit

__all__ = ["WellKnown", "AsyncWellKnown"]


class WellKnown(SyncAPIResource):
    jwks: Jwks

    def __init__(self, client: Moneykit) -> None:
        super().__init__(client)
        self.jwks = Jwks(client)


class AsyncWellKnown(AsyncAPIResource):
    jwks: AsyncJwks

    def __init__(self, client: AsyncMoneykit) -> None:
        super().__init__(client)
        self.jwks = AsyncJwks(client)
