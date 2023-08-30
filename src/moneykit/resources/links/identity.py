# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types.links import IdentityResponse, identity_retrieve_params
from ..._base_client import make_request_options

__all__ = ["Identity", "AsyncIdentity"]


class Identity(SyncAPIResource):
    def retrieve(
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
    ) -> IdentityResponse:
        """
        Returns account owner information from the institution, including names, emails,
        phone numbers, and addresses, for all permissioned accounts associated with a
        <a href=#tag/Links>link</a>. <p>Some fields may be empty, if not provided by the
        institution.

        Args:
          id: The unique ID for this link.

          account_ids: An optional list of account IDs to filter the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/links/{id}/identity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_ids": account_ids}, identity_retrieve_params.IdentityRetrieveParams),
            ),
            cast_to=IdentityResponse,
        )


class AsyncIdentity(AsyncAPIResource):
    async def retrieve(
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
    ) -> IdentityResponse:
        """
        Returns account owner information from the institution, including names, emails,
        phone numbers, and addresses, for all permissioned accounts associated with a
        <a href=#tag/Links>link</a>. <p>Some fields may be empty, if not provided by the
        institution.

        Args:
          id: The unique ID for this link.

          account_ids: An optional list of account IDs to filter the results.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/links/{id}/identity",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"account_ids": account_ids}, identity_retrieve_params.IdentityRetrieveParams),
            ),
            cast_to=IdentityResponse,
        )
