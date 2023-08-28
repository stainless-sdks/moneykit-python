# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types.users import GetUserTransactionsResponse, transaction_list_params
from ..._base_client import make_request_options

__all__ = ["Transactions", "AsyncTransactions"]


class Transactions(SyncAPIResource):
    def list(
        self,
        id: str,
        *,
        account_id: List[str] | NotGiven = NOT_GIVEN,
        category: List[str] | NotGiven = NOT_GIVEN,
        end_date: Optional[str] | NotGiven = NOT_GIVEN,
        institution_id: List[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        start_date: Optional[str] | NotGiven = NOT_GIVEN,
        transaction_type: List[Literal["credit", "debit"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> GetUserTransactionsResponse:
        """
        Fetches transactions for a <a href=#operation/get_user_accounts>user</a>.
        <p>This endpoint fetches all transactions for a user across all of their links.
        You can use it to retrieve transactions from any or all accounts at once,
        regardless of which institution they belong to.

        Args:
          id: The unique ID for this user. This is the same ID provided in the call to
              <a href=#operation/create_link_session>/link-session</a> to create any link for
              this user.

          account_id: If present, filters results to transactions in accounts matching the given IDs.

          end_date: The latest date for which data should be returned, formatted as YYYY-MM-DD.
              Defaults to today.

          institution_id: If present, filters results to transactions at institutions matching the given
              IDs.

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
            f"/users/{id}/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "category": category,
                        "end_date": end_date,
                        "institution_id": institution_id,
                        "page": page,
                        "size": size,
                        "start_date": start_date,
                        "transaction_type": transaction_type,
                    },
                    transaction_list_params.TransactionListParams,
                ),
            ),
            cast_to=GetUserTransactionsResponse,
        )


class AsyncTransactions(AsyncAPIResource):
    async def list(
        self,
        id: str,
        *,
        account_id: List[str] | NotGiven = NOT_GIVEN,
        category: List[str] | NotGiven = NOT_GIVEN,
        end_date: Optional[str] | NotGiven = NOT_GIVEN,
        institution_id: List[str] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        size: int | NotGiven = NOT_GIVEN,
        start_date: Optional[str] | NotGiven = NOT_GIVEN,
        transaction_type: List[Literal["credit", "debit"]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> GetUserTransactionsResponse:
        """
        Fetches transactions for a <a href=#operation/get_user_accounts>user</a>.
        <p>This endpoint fetches all transactions for a user across all of their links.
        You can use it to retrieve transactions from any or all accounts at once,
        regardless of which institution they belong to.

        Args:
          id: The unique ID for this user. This is the same ID provided in the call to
              <a href=#operation/create_link_session>/link-session</a> to create any link for
              this user.

          account_id: If present, filters results to transactions in accounts matching the given IDs.

          end_date: The latest date for which data should be returned, formatted as YYYY-MM-DD.
              Defaults to today.

          institution_id: If present, filters results to transactions at institutions matching the given
              IDs.

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
            f"/users/{id}/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "category": category,
                        "end_date": end_date,
                        "institution_id": institution_id,
                        "page": page,
                        "size": size,
                        "start_date": start_date,
                        "transaction_type": transaction_type,
                    },
                    transaction_list_params.TransactionListParams,
                ),
            ),
            cast_to=GetUserTransactionsResponse,
        )
