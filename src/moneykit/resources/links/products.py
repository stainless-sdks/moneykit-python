# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types.links import product_create_params
from ..._base_client import make_request_options

__all__ = ["Products", "AsyncProducts"]


class Products(SyncAPIResource):
    def create(
        self,
        id: str,
        *,
        products: List[Literal["accounts", "account_numbers", "identity", "transactions"]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Requests an update of the provided products for the link.

        This is an
        asynchronous operation. The response will be a 202 Accepted if the request was
        successful.

        Args:
          id: The unique ID for this link.

          products: At list of at least one product to refresh.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            f"/links/{id}/products",
            body=maybe_transform({"products": products}, product_create_params.ProductCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncProducts(AsyncAPIResource):
    async def create(
        self,
        id: str,
        *,
        products: List[Literal["accounts", "account_numbers", "identity", "transactions"]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Requests an update of the provided products for the link.

        This is an
        asynchronous operation. The response will be a 202 Accepted if the request was
        successful.

        Args:
          id: The unique ID for this link.

          products: At list of at least one product to refresh.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            f"/links/{id}/products",
            body=maybe_transform({"products": products}, product_create_params.ProductCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )
