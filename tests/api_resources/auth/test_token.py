# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from moneykit import Moneykit, AsyncMoneykit
from tests.utils import assert_matches_type
from moneykit.types.auth import GenerateAccessTokenResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestToken:
    strict_client = Moneykit(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Moneykit(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_create(self, client: Moneykit) -> None:
        token = client.auth.token.create()
        assert_matches_type(GenerateAccessTokenResponse, token, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Moneykit) -> None:
        token = client.auth.token.create(
            client_id="string",
            client_secret="string",
            grant_type="string",
            scope="string",
        )
        assert_matches_type(GenerateAccessTokenResponse, token, path=["response"])


class TestAsyncToken:
    strict_client = AsyncMoneykit(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncMoneykit(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_create(self, client: AsyncMoneykit) -> None:
        token = await client.auth.token.create()
        assert_matches_type(GenerateAccessTokenResponse, token, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, client: AsyncMoneykit) -> None:
        token = await client.auth.token.create(
            client_id="string",
            client_secret="string",
            grant_type="string",
            scope="string",
        )
        assert_matches_type(GenerateAccessTokenResponse, token, path=["response"])
