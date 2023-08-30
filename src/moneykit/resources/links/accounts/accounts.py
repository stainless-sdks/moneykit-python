# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List

from .numbers import Numbers, AsyncNumbers
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types.links import (
    AccountListResponse,
    AccountRetrieveResponse,
    account_list_params,
)
from ...._base_client import make_request_options

if TYPE_CHECKING:
    from ...._client import Moneykit, AsyncMoneykit

__all__ = ["Accounts", "AsyncAccounts"]


class Accounts(SyncAPIResource):
    numbers: Numbers

    def __init__(self, client: Moneykit) -> None:
        super().__init__(client)
        self.numbers = Numbers(client)

    def retrieve(
        self,
        account_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AccountRetrieveResponse:
        """
        Fetches a single account associated with a <a href=#tag/Links>link</a>.

        Args:
          id: The unique ID for this link.

          account_id: The account ID to fetch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/links/{id}/accounts/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountRetrieveResponse,
        )

    def list(
        self,
        id: str,
        *,
        account_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AccountListResponse:
        """
        Returns a list of open, permissioned accounts associated with a
        <a href=#tag/Links>link</a>.

        Args:
          id: The unique ID for this link.

          account_ids: An optional list of account IDs to filter the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/links/{id}/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_ids": account_ids}, account_list_params.AccountListParams),
            ),
            cast_to=AccountListResponse,
        )


class AsyncAccounts(AsyncAPIResource):
    numbers: AsyncNumbers

    def __init__(self, client: AsyncMoneykit) -> None:
        super().__init__(client)
        self.numbers = AsyncNumbers(client)

    async def retrieve(
        self,
        account_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AccountRetrieveResponse:
        """
        Fetches a single account associated with a <a href=#tag/Links>link</a>.

        Args:
          id: The unique ID for this link.

          account_id: The account ID to fetch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/links/{id}/accounts/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountRetrieveResponse,
        )

    async def list(
        self,
        id: str,
        *,
        account_ids: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> AccountListResponse:
        """
        Returns a list of open, permissioned accounts associated with a
        <a href=#tag/Links>link</a>.

        Args:
          id: The unique ID for this link.

          account_ids: An optional list of account IDs to filter the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/links/{id}/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_ids": account_ids}, account_list_params.AccountListParams),
            ),
            cast_to=AccountListResponse,
        )
