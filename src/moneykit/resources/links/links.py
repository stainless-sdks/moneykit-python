# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...types import LinkResponse, link_update_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from .accounts import Accounts, AsyncAccounts
from .identity import Identity, AsyncIdentity
from .products import Products, AsyncProducts
from ..._resource import SyncAPIResource, AsyncAPIResource
from .transactions import Transactions, AsyncTransactions
from ..._base_client import make_request_options

if TYPE_CHECKING:
    from ..._client import Moneykit, AsyncMoneykit

__all__ = ["Links", "AsyncLinks"]


class Links(SyncAPIResource):
    accounts: Accounts
    identity: Identity
    transactions: Transactions
    products: Products

    def __init__(self, client: Moneykit) -> None:
        super().__init__(client)
        self.accounts = Accounts(client)
        self.identity = Identity(client)
        self.transactions = Transactions(client)
        self.products = Products(client)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> LinkResponse:
        """
        Fetches details about a link.

        Args:
          id: The unique ID for this link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/links/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkResponse,
        )

    def update(
        self,
        id: str,
        *,
        tags: List[str] | NotGiven = NOT_GIVEN,
        webhook: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> LinkResponse:
        """
        Updates the link configuration.

        Args:
          id: The unique ID for this link.

          tags: Arbitrary strings used to describe this link.

          webhook: Sets the webhook URL for this link. To remove a webhook for this link, set to
              `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            f"/links/{id}",
            body=maybe_transform(
                {
                    "tags": tags,
                    "webhook": webhook,
                },
                link_update_params.LinkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes this link and disables its access token.

        <p>After deletion, the link id
        and access token are no longer valid and cannot be used to access any data that
        was associated with it.

        Args:
          id: The unique ID for this link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/links/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncLinks(AsyncAPIResource):
    accounts: AsyncAccounts
    identity: AsyncIdentity
    transactions: AsyncTransactions
    products: AsyncProducts

    def __init__(self, client: AsyncMoneykit) -> None:
        super().__init__(client)
        self.accounts = AsyncAccounts(client)
        self.identity = AsyncIdentity(client)
        self.transactions = AsyncTransactions(client)
        self.products = AsyncProducts(client)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> LinkResponse:
        """
        Fetches details about a link.

        Args:
          id: The unique ID for this link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/links/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkResponse,
        )

    async def update(
        self,
        id: str,
        *,
        tags: List[str] | NotGiven = NOT_GIVEN,
        webhook: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> LinkResponse:
        """
        Updates the link configuration.

        Args:
          id: The unique ID for this link.

          tags: Arbitrary strings used to describe this link.

          webhook: Sets the webhook URL for this link. To remove a webhook for this link, set to
              `null`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            f"/links/{id}",
            body=maybe_transform(
                {
                    "tags": tags,
                    "webhook": webhook,
                },
                link_update_params.LinkUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LinkResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Deletes this link and disables its access token.

        <p>After deletion, the link id
        and access token are no longer valid and cannot be used to access any data that
        was associated with it.

        Args:
          id: The unique ID for this link.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/links/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )
