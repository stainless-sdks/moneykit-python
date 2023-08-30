# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from moneykit import Moneykit, AsyncMoneykit

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestProducts:
    strict_client = Moneykit(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Moneykit(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="prism doesn't allow an array with duplicate enums")
    @parametrize
    def test_method_create(self, client: Moneykit) -> None:
        product = client.links.products.create(
            "string",
            products=["accounts", "accounts", "accounts"],
        )
        assert product is None


class TestAsyncProducts:
    strict_client = AsyncMoneykit(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncMoneykit(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @pytest.mark.skip(reason="prism doesn't allow an array with duplicate enums")
    @parametrize
    async def test_method_create(self, client: AsyncMoneykit) -> None:
        product = await client.links.products.create(
            "string",
            products=["accounts", "accounts", "accounts"],
        )
        assert product is None
