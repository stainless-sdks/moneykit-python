# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from ...types.link_session import ExchangeTokenResponse, exchange_token_create_params

__all__ = ["ExchangeToken", "AsyncExchangeToken"]


class ExchangeToken(SyncAPIResource):
    def create(
        self,
        *,
        exchangeable_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ExchangeTokenResponse:
        """
        After the end user has successfully completed the linking process, your back end
        calls this endpoint to exchange the token received by your front end for
        a`link_id` that can be used to access the link's data.

        Args:
          exchangeable_token: The token returned to your front end by MoneyLink's onSuccess callback.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/link-session/exchange-token",
            body=maybe_transform(
                {"exchangeable_token": exchangeable_token}, exchange_token_create_params.ExchangeTokenCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExchangeTokenResponse,
        )


class AsyncExchangeToken(AsyncAPIResource):
    async def create(
        self,
        *,
        exchangeable_token: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> ExchangeTokenResponse:
        """
        After the end user has successfully completed the linking process, your back end
        calls this endpoint to exchange the token received by your front end for
        a`link_id` that can be used to access the link's data.

        Args:
          exchangeable_token: The token returned to your front end by MoneyLink's onSuccess callback.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/link-session/exchange-token",
            body=maybe_transform(
                {"exchangeable_token": exchangeable_token}, exchange_token_create_params.ExchangeTokenCreateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExchangeTokenResponse,
        )
