# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.well_known import JwkSet

__all__ = ["Jwks", "AsyncJwks"]


class Jwks(SyncAPIResource):
    def json(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> JwkSet:
        """
        The JSON Web Key Set (JWKS) is a set of keys containing the public keys used to
        verify webhook JSON Web Tokens (JWT) issued by MoneyKit webhooks.
        """
        return self._get(
            "/.well-known/jwks.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JwkSet,
        )


class AsyncJwks(AsyncAPIResource):
    async def json(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> JwkSet:
        """
        The JSON Web Key Set (JWKS) is a set of keys containing the public keys used to
        verify webhook JSON Web Tokens (JWT) issued by MoneyKit webhooks.
        """
        return await self._get(
            "/.well-known/jwks.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JwkSet,
        )
