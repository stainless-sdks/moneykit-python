# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from moneykit import Moneykit, AsyncMoneykit
from tests.utils import assert_matches_type
from moneykit.types import CreateLinkSessionResponse
from moneykit._utils import parse_datetime

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestLinkSession:
    strict_client = Moneykit(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Moneykit(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_create(self, client: Moneykit) -> None:
        link_session = client.link_session.create(
            customer_user={"id": "xxxx"},
            redirect_uri="https://yourdomain.com/oauth.html",
        )
        assert_matches_type(CreateLinkSessionResponse, link_session, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    def test_method_create_with_all_params(self, client: Moneykit) -> None:
        link_session = client.link_session.create(
            customer_user={
                "id": "xxxx",
                "email": {
                    "address": "xxxx",
                    "customer_verified_at": parse_datetime("2023-02-16T00:00:00"),
                },
                "phone": {
                    "number": "+16175551212",
                    "country": "US",
                    "customer_verified_at": parse_datetime("2023-02-16T00:00:00"),
                },
            },
            redirect_uri="https://yourdomain.com/oauth.html",
            existing_link_id="mk_eqkWN34UEoa2NxyALG8pcV",
            institution_id="c7318ff7-257c-490e-8242-03a815b223b7",
            link_tags=["string", "string", "string"],
            moneylink_features={
                "bug_reporter": True,
                "enable_money_id": True,
            },
            settings={
                "providers": ["moneykit", "moneykit", "moneykit"],
                "link_permissions": {
                    "requested": [
                        {
                            "scope": "accounts",
                            "reason": "display your account balances",
                            "required": True,
                        },
                        {
                            "scope": "accounts",
                            "reason": "display your account balances",
                            "required": True,
                        },
                        {
                            "scope": "accounts",
                            "reason": "display your account balances",
                            "required": True,
                        },
                    ]
                },
                "products": {
                    "account_numbers": {
                        "required": True,
                        "prefetch": True,
                    },
                    "identity": {
                        "required": True,
                        "prefetch": True,
                    },
                    "transactions": {
                        "required": True,
                        "prefetch": True,
                        "extend_history": True,
                    },
                },
                "countries": ["US", "US", "US"],
            },
            webhook="https://yourdomain.com/moneykit_webhook",
        )
        assert_matches_type(CreateLinkSessionResponse, link_session, path=["response"])


class TestAsyncLinkSession:
    strict_client = AsyncMoneykit(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncMoneykit(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_create(self, client: AsyncMoneykit) -> None:
        link_session = await client.link_session.create(
            customer_user={"id": "xxxx"},
            redirect_uri="https://yourdomain.com/oauth.html",
        )
        assert_matches_type(CreateLinkSessionResponse, link_session, path=["response"])

    @pytest.mark.skip(
        reason="currently no good way to test endpoints defining callbacks, Prism mock server will fail trying to reach the provided callback url"
    )
    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncMoneykit) -> None:
        link_session = await client.link_session.create(
            customer_user={
                "id": "xxxx",
                "email": {
                    "address": "xxxx",
                    "customer_verified_at": parse_datetime("2023-02-16T00:00:00"),
                },
                "phone": {
                    "number": "+16175551212",
                    "country": "US",
                    "customer_verified_at": parse_datetime("2023-02-16T00:00:00"),
                },
            },
            redirect_uri="https://yourdomain.com/oauth.html",
            existing_link_id="mk_eqkWN34UEoa2NxyALG8pcV",
            institution_id="c7318ff7-257c-490e-8242-03a815b223b7",
            link_tags=["string", "string", "string"],
            moneylink_features={
                "bug_reporter": True,
                "enable_money_id": True,
            },
            settings={
                "providers": ["moneykit", "moneykit", "moneykit"],
                "link_permissions": {
                    "requested": [
                        {
                            "scope": "accounts",
                            "reason": "display your account balances",
                            "required": True,
                        },
                        {
                            "scope": "accounts",
                            "reason": "display your account balances",
                            "required": True,
                        },
                        {
                            "scope": "accounts",
                            "reason": "display your account balances",
                            "required": True,
                        },
                    ]
                },
                "products": {
                    "account_numbers": {
                        "required": True,
                        "prefetch": True,
                    },
                    "identity": {
                        "required": True,
                        "prefetch": True,
                    },
                    "transactions": {
                        "required": True,
                        "prefetch": True,
                        "extend_history": True,
                    },
                },
                "countries": ["US", "US", "US"],
            },
            webhook="https://yourdomain.com/moneykit_webhook",
        )
        assert_matches_type(CreateLinkSessionResponse, link_session, path=["response"])
