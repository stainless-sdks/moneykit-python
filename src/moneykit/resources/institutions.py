# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional

from ..types import Institution, GetInstitutionsResponse, institution_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import make_request_options

__all__ = ["Institutions", "AsyncInstitutions"]


class Institutions(SyncAPIResource):
    def retrieve(
        self,
        institution_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Institution:
        """
        Fetches details about a single institution.

        Args:
          institution_id: The institution ID to fetch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/institutions/{institution_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Institution,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        featured: Optional[bool] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> GetInstitutionsResponse:
        """Fetches a list of institutions, optionally filtered by name.

        Results are
        paginated.

        Args:
          cursor: Cursor to fetch the next set of institutions. (You get this value from the
              previous call to `/institutions`.)

          featured: If true, returns only featured institutions.

          limit: A limit on the number of institutions to be returned.

          name: If provided, returns only institutions containing this name (wholly or as a
              prefix).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/institutions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "featured": featured,
                        "limit": limit,
                        "name": name,
                    },
                    institution_list_params.InstitutionListParams,
                ),
            ),
            cast_to=GetInstitutionsResponse,
        )


class AsyncInstitutions(AsyncAPIResource):
    async def retrieve(
        self,
        institution_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> Institution:
        """
        Fetches details about a single institution.

        Args:
          institution_id: The institution ID to fetch.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/institutions/{institution_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Institution,
        )

    async def list(
        self,
        *,
        cursor: Optional[str] | NotGiven = NOT_GIVEN,
        featured: Optional[bool] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        name: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> GetInstitutionsResponse:
        """Fetches a list of institutions, optionally filtered by name.

        Results are
        paginated.

        Args:
          cursor: Cursor to fetch the next set of institutions. (You get this value from the
              previous call to `/institutions`.)

          featured: If true, returns only featured institutions.

          limit: A limit on the number of institutions to be returned.

          name: If provided, returns only institutions containing this name (wholly or as a
              prefix).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/institutions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "featured": featured,
                        "limit": limit,
                        "name": name,
                    },
                    institution_list_params.InstitutionListParams,
                ),
            ),
            cast_to=GetInstitutionsResponse,
        )
