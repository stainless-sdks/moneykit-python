# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types.links import (
    GetTransactionsResponse,
    TransactionSyncResponse,
    transaction_list_params,
    transaction_sync_params,
)
from ..._base_client import make_request_options

__all__ = ["Transactions", "AsyncTransactions"]


class Transactions(SyncAPIResource):
    def list(
        self,
        id: str,
        *,
        account_ids: List[str] | NotGiven = NOT_GIVEN,
        end_date: Optional[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        start_date: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> GetTransactionsResponse:
        """
        Fetches transactions for the accounts associated with a
        <a href=#tag/Links>link</a>. Results are paginated, and returned in reverse
        chronological order. <p>MoneyKit checks for updated account data, including
        transactions, periodically throughout the day, but the update frequency can
        vary, depending on the downstream data provider and the institution. To force a
        check for updated transactions, you can use the
        <a href=#operation/refresh_products>/products</a> endpoint.

        Args:
          id: The unique ID for this link.

          account_ids: An optional list of account IDs to filter the results.

          end_date: The latest date for which data should be returned, formatted as YYYY-MM-DD.
              Defaults to today.

          page: The page number to return.

          size: The number of items to return per page.

          start_date: The earliest date for which data should be returned, formatted as YYYY-MM-DD.
              Defaults to 90 days before the `end_date`. <p>If you want to retrieve **all**
              transactions, use `1900-01-01`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/links/{id}/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_ids": account_ids,
                        "end_date": end_date,
                        "page": page,
                        "size": size,
                        "start_date": start_date,
                    },
                    transaction_list_params.TransactionListParams,
                ),
            ),
            cast_to=GetTransactionsResponse,
        )

    def sync(
        self,
        id: str,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> TransactionSyncResponse:
        """
        Provides a paginated feed of transactions, grouped into `created`, `updated`,
        and `removed` lists. <p>Each call will also return a `next_cursor` value. In
        subsequent calls, include that value to receive only changes that have occurred
        since the previous call. <p>Large numbers of transactions will be paginated, and
        the `has_more` field will be true. You should continue calling this endpoint
        with each new `next_cursor` value until `has_more` is false. <p>Note also that
        the `transactions.updates_available` webhook will alert you when new data is
        available.

        Args:
          id: The unique ID for this link.

          cursor: A cursor value representing the last update requested. If included, the response
              will only return changes after this update. If omitted, a complete history of
              updates will be returned. This value must be stored by the client as we do not
              keep track of customer cursors.

          size: The number of items to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/links/{id}/transactions/sync",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "size": size,
                    },
                    transaction_sync_params.TransactionSyncParams,
                ),
            ),
            cast_to=TransactionSyncResponse,
        )


class AsyncTransactions(AsyncAPIResource):
    async def list(
        self,
        id: str,
        *,
        account_ids: List[str] | NotGiven = NOT_GIVEN,
        end_date: Optional[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        start_date: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> GetTransactionsResponse:
        """
        Fetches transactions for the accounts associated with a
        <a href=#tag/Links>link</a>. Results are paginated, and returned in reverse
        chronological order. <p>MoneyKit checks for updated account data, including
        transactions, periodically throughout the day, but the update frequency can
        vary, depending on the downstream data provider and the institution. To force a
        check for updated transactions, you can use the
        <a href=#operation/refresh_products>/products</a> endpoint.

        Args:
          id: The unique ID for this link.

          account_ids: An optional list of account IDs to filter the results.

          end_date: The latest date for which data should be returned, formatted as YYYY-MM-DD.
              Defaults to today.

          page: The page number to return.

          size: The number of items to return per page.

          start_date: The earliest date for which data should be returned, formatted as YYYY-MM-DD.
              Defaults to 90 days before the `end_date`. <p>If you want to retrieve **all**
              transactions, use `1900-01-01`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/links/{id}/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_ids": account_ids,
                        "end_date": end_date,
                        "page": page,
                        "size": size,
                        "start_date": start_date,
                    },
                    transaction_list_params.TransactionListParams,
                ),
            ),
            cast_to=GetTransactionsResponse,
        )

    async def sync(
        self,
        id: str,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> TransactionSyncResponse:
        """
        Provides a paginated feed of transactions, grouped into `created`, `updated`,
        and `removed` lists. <p>Each call will also return a `next_cursor` value. In
        subsequent calls, include that value to receive only changes that have occurred
        since the previous call. <p>Large numbers of transactions will be paginated, and
        the `has_more` field will be true. You should continue calling this endpoint
        with each new `next_cursor` value until `has_more` is false. <p>Note also that
        the `transactions.updates_available` webhook will alert you when new data is
        available.

        Args:
          id: The unique ID for this link.

          cursor: A cursor value representing the last update requested. If included, the response
              will only return changes after this update. If omitted, a complete history of
              updates will be returned. This value must be stored by the client as we do not
              keep track of customer cursors.

          size: The number of items to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/links/{id}/transactions/sync",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "size": size,
                    },
                    transaction_sync_params.TransactionSyncParams,
                ),
            ),
            cast_to=TransactionSyncResponse,
        )
