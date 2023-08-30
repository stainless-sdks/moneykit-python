# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types.users import GetUserAccountsResponse, account_list_params
from ..._base_client import make_request_options

__all__ = ["Accounts", "AsyncAccounts"]


class Accounts(SyncAPIResource):
    def list(
        self,
        id: str,
        *,
        account_id: List[str] | NotGiven = NOT_GIVEN,
        institution_id: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> GetUserAccountsResponse:
        """
        Fetches all accounts belonging to a
        <a href=#operation/get_user_accounts>user</a>.

        Args:
          id: The unique ID for this user. This is the same ID provided in the call to
              <a href=#operation/create_link_session>/link-session</a> to create any link for
              this user.

          account_id: If present, filters results to accounts matching the given IDs.

          institution_id: If present, filters results to accounts at institutions matching the given IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/users/{id}/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "institution_id": institution_id,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            cast_to=GetUserAccountsResponse,
        )


class AsyncAccounts(AsyncAPIResource):
    async def list(
        self,
        id: str,
        *,
        account_id: List[str] | NotGiven = NOT_GIVEN,
        institution_id: List[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> GetUserAccountsResponse:
        """
        Fetches all accounts belonging to a
        <a href=#operation/get_user_accounts>user</a>.

        Args:
          id: The unique ID for this user. This is the same ID provided in the call to
              <a href=#operation/create_link_session>/link-session</a> to create any link for
              this user.

          account_id: If present, filters results to accounts matching the given IDs.

          institution_id: If present, filters results to accounts at institutions matching the given IDs.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/users/{id}/accounts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account_id": account_id,
                        "institution_id": institution_id,
                    },
                    account_list_params.AccountListParams,
                ),
            ),
            cast_to=GetUserAccountsResponse,
        )
