# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from moneykit import Moneykit, AsyncMoneykit
from tests.utils import assert_matches_type
from moneykit.types.users import GetUserTransactionsResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestTransactions:
    strict_client = Moneykit(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Moneykit(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Moneykit) -> None:
        transaction = client.users.transactions.list(
            "string",
        )
        assert_matches_type(GetUserTransactionsResponse, transaction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Moneykit) -> None:
        transaction = client.users.transactions.list(
            "string",
            account_id=["x", "x", "x"],
            category=["string", "string", "string"],
            end_date="string",
            institution_id=["x", "x", "x"],
            page=1,
            size=1,
            start_date="string",
            transaction_type=["credit", "credit", "credit"],
        )
        assert_matches_type(GetUserTransactionsResponse, transaction, path=["response"])


class TestAsyncTransactions:
    strict_client = AsyncMoneykit(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncMoneykit(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncMoneykit) -> None:
        transaction = await client.users.transactions.list(
            "string",
        )
        assert_matches_type(GetUserTransactionsResponse, transaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncMoneykit) -> None:
        transaction = await client.users.transactions.list(
            "string",
            account_id=["x", "x", "x"],
            category=["string", "string", "string"],
            end_date="string",
            institution_id=["x", "x", "x"],
            page=1,
            size=1,
            start_date="string",
            transaction_type=["credit", "credit", "credit"],
        )
        assert_matches_type(GetUserTransactionsResponse, transaction, path=["response"])
