# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from moneykit import Moneykit, AsyncMoneykit
from tests.utils import assert_matches_type
from moneykit.types.links import GetTransactionsResponse, TransactionSyncResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestTransactions:
    strict_client = Moneykit(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Moneykit(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Moneykit) -> None:
        transaction = client.links.transactions.list(
            "string",
        )
        assert_matches_type(GetTransactionsResponse, transaction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Moneykit) -> None:
        transaction = client.links.transactions.list(
            "string",
            account_ids=["string", "string", "string"],
            end_date="string",
            page=1,
            size=1,
            start_date="string",
        )
        assert_matches_type(GetTransactionsResponse, transaction, path=["response"])

    @parametrize
    def test_method_sync(self, client: Moneykit) -> None:
        transaction = client.links.transactions.sync(
            "string",
        )
        assert_matches_type(TransactionSyncResponse, transaction, path=["response"])

    @parametrize
    def test_method_sync_with_all_params(self, client: Moneykit) -> None:
        transaction = client.links.transactions.sync(
            "string",
            cursor="string",
            size=1,
        )
        assert_matches_type(TransactionSyncResponse, transaction, path=["response"])


class TestAsyncTransactions:
    strict_client = AsyncMoneykit(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncMoneykit(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncMoneykit) -> None:
        transaction = await client.links.transactions.list(
            "string",
        )
        assert_matches_type(GetTransactionsResponse, transaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncMoneykit) -> None:
        transaction = await client.links.transactions.list(
            "string",
            account_ids=["string", "string", "string"],
            end_date="string",
            page=1,
            size=1,
            start_date="string",
        )
        assert_matches_type(GetTransactionsResponse, transaction, path=["response"])

    @parametrize
    async def test_method_sync(self, client: AsyncMoneykit) -> None:
        transaction = await client.links.transactions.sync(
            "string",
        )
        assert_matches_type(TransactionSyncResponse, transaction, path=["response"])

    @parametrize
    async def test_method_sync_with_all_params(self, client: AsyncMoneykit) -> None:
        transaction = await client.links.transactions.sync(
            "string",
            cursor="string",
            size=1,
        )
        assert_matches_type(TransactionSyncResponse, transaction, path=["response"])
