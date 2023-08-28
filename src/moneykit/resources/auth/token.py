# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types.auth import GenerateAccessTokenResponse, token_create_params
from ..._base_client import make_request_options

__all__ = ["Token", "AsyncToken"]


class Token(SyncAPIResource):
    def create(
        self,
        *,
        client_id: Optional[str] | NotGiven = NOT_GIVEN,
        client_secret: Optional[str] | NotGiven = NOT_GIVEN,
        grant_type: Optional[str] | NotGiven = NOT_GIVEN,
        scope: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> GenerateAccessTokenResponse:
        """
        Create a new short-lived access token by validating your `client_id` and
        `client_secret`.

        The `access_token` is to be forwarded with all subsequent requests as
        `Authorization: Bearer {access_token}` HTTP header.

        When the token expires you must regenerate your `access_token`.

        The `client_id` and `client_secret` can be supplied as POST body parameters, or
        as a HTTP basic auth header.

        Args:
          client_id: Your application's MoneyKit client ID.

          client_secret: Your application's MoneyKit client secret.

          grant_type: Token grant type. Only `client_credentials` supported.

          scope: Actions to be allowed for this token, given as one or more strings separated by
              spaces. If omitted, all actions allowed for your application will be granted to
              this token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/auth/token",
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "grant_type": grant_type,
                    "scope": scope,
                },
                token_create_params.TokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateAccessTokenResponse,
        )


class AsyncToken(AsyncAPIResource):
    async def create(
        self,
        *,
        client_id: Optional[str] | NotGiven = NOT_GIVEN,
        client_secret: Optional[str] | NotGiven = NOT_GIVEN,
        grant_type: Optional[str] | NotGiven = NOT_GIVEN,
        scope: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> GenerateAccessTokenResponse:
        """
        Create a new short-lived access token by validating your `client_id` and
        `client_secret`.

        The `access_token` is to be forwarded with all subsequent requests as
        `Authorization: Bearer {access_token}` HTTP header.

        When the token expires you must regenerate your `access_token`.

        The `client_id` and `client_secret` can be supplied as POST body parameters, or
        as a HTTP basic auth header.

        Args:
          client_id: Your application's MoneyKit client ID.

          client_secret: Your application's MoneyKit client secret.

          grant_type: Token grant type. Only `client_credentials` supported.

          scope: Actions to be allowed for this token, given as one or more strings separated by
              spaces. If omitted, all actions allowed for your application will be granted to
              this token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/auth/token",
            body=maybe_transform(
                {
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "grant_type": grant_type,
                    "scope": scope,
                },
                token_create_params.TokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateAccessTokenResponse,
        )
