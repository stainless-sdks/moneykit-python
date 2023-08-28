# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from ...types import CreateLinkSessionResponse, link_session_create_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import make_request_options
from .exchange_token import ExchangeToken, AsyncExchangeToken

if TYPE_CHECKING:
    from ..._client import Moneykit, AsyncMoneykit

__all__ = ["LinkSession", "AsyncLinkSession"]


class LinkSession(SyncAPIResource):
    exchange_token: ExchangeToken

    def __init__(self, client: Moneykit) -> None:
        super().__init__(client)
        self.exchange_token = ExchangeToken(client)

    def create(
        self,
        *,
        customer_user: link_session_create_params.CustomerUser,
        redirect_uri: str,
        existing_link_id: Optional[str] | NotGiven = NOT_GIVEN,
        institution_id: Optional[str] | NotGiven = NOT_GIVEN,
        link_tags: List[str] | NotGiven = NOT_GIVEN,
        moneylink_features: link_session_create_params.MoneylinkFeatures | NotGiven = NOT_GIVEN,
        settings: link_session_create_params.Settings | NotGiven = NOT_GIVEN,
        webhook: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CreateLinkSessionResponse:
        """
        This endpoint is to be called by your back end, to establish a new link session
        for creating a link to your end user's institution.

        Args:
          customer_user: Details about your end user. These details are used to improve conversion and
              streamline the linking flow, and to support the MoneyID system, which provides
              enhanced debugging and improved privacy controls for your end user.

          redirect_uri: For Oauth linking, a URI indicating the destination, in your application, where
              the user should be sent after authenticating with the institution. The
              `redirect_uri` should not contain any query parameters, and it must be
              pre-approved by MoneyKit during the customer setup process.

          existing_link_id: Supply the existing `link_id` if you are asking the user to reconnect this link.

          institution_id: The ID of the institution you want to link to. Providing this will skip the
              institution selection step. `existing_link_id` will take precedence over this
              field if both are provided.

          link_tags: You can supply one or more arbitrary strings as tags to describe this link.

          moneylink_features: Enables optional testing and UI features.

          settings: If provided, these settings will override your default settings for this
              session.

          webhook: The destination URL to which any webhooks should be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/link-session",
            body=maybe_transform(
                {
                    "customer_user": customer_user,
                    "redirect_uri": redirect_uri,
                    "existing_link_id": existing_link_id,
                    "institution_id": institution_id,
                    "link_tags": link_tags,
                    "moneylink_features": moneylink_features,
                    "settings": settings,
                    "webhook": webhook,
                },
                link_session_create_params.LinkSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateLinkSessionResponse,
        )


class AsyncLinkSession(AsyncAPIResource):
    exchange_token: AsyncExchangeToken

    def __init__(self, client: AsyncMoneykit) -> None:
        super().__init__(client)
        self.exchange_token = AsyncExchangeToken(client)

    async def create(
        self,
        *,
        customer_user: link_session_create_params.CustomerUser,
        redirect_uri: str,
        existing_link_id: Optional[str] | NotGiven = NOT_GIVEN,
        institution_id: Optional[str] | NotGiven = NOT_GIVEN,
        link_tags: List[str] | NotGiven = NOT_GIVEN,
        moneylink_features: link_session_create_params.MoneylinkFeatures | NotGiven = NOT_GIVEN,
        settings: link_session_create_params.Settings | NotGiven = NOT_GIVEN,
        webhook: Optional[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | None | NotGiven = NOT_GIVEN,
    ) -> CreateLinkSessionResponse:
        """
        This endpoint is to be called by your back end, to establish a new link session
        for creating a link to your end user's institution.

        Args:
          customer_user: Details about your end user. These details are used to improve conversion and
              streamline the linking flow, and to support the MoneyID system, which provides
              enhanced debugging and improved privacy controls for your end user.

          redirect_uri: For Oauth linking, a URI indicating the destination, in your application, where
              the user should be sent after authenticating with the institution. The
              `redirect_uri` should not contain any query parameters, and it must be
              pre-approved by MoneyKit during the customer setup process.

          existing_link_id: Supply the existing `link_id` if you are asking the user to reconnect this link.

          institution_id: The ID of the institution you want to link to. Providing this will skip the
              institution selection step. `existing_link_id` will take precedence over this
              field if both are provided.

          link_tags: You can supply one or more arbitrary strings as tags to describe this link.

          moneylink_features: Enables optional testing and UI features.

          settings: If provided, these settings will override your default settings for this
              session.

          webhook: The destination URL to which any webhooks should be sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/link-session",
            body=maybe_transform(
                {
                    "customer_user": customer_user,
                    "redirect_uri": redirect_uri,
                    "existing_link_id": existing_link_id,
                    "institution_id": institution_id,
                    "link_tags": link_tags,
                    "moneylink_features": moneylink_features,
                    "settings": settings,
                    "webhook": webhook,
                },
                link_session_create_params.LinkSessionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreateLinkSessionResponse,
        )
