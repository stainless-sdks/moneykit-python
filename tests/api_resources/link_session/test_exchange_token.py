# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from moneykit import Moneykit, AsyncMoneykit
from tests.utils import assert_matches_type
from moneykit.types.link_session import ExchangeTokenResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestExchangeToken:
    strict_client = Moneykit(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Moneykit(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Moneykit) -> None:
        exchange_token = client.link_session.exchange_token.create(
            exchangeable_token="c7318ff7-257c-490e-8242-03a815b223b7",
        )
        assert_matches_type(ExchangeTokenResponse, exchange_token, path=["response"])


class TestAsyncExchangeToken:
    strict_client = AsyncMoneykit(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncMoneykit(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncMoneykit) -> None:
        exchange_token = await client.link_session.exchange_token.create(
            exchangeable_token="c7318ff7-257c-490e-8242-03a815b223b7",
        )
        assert_matches_type(ExchangeTokenResponse, exchange_token, path=["response"])
