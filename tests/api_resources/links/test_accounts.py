# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from moneykit import Moneykit, AsyncMoneykit
from tests.utils import assert_matches_type
from moneykit.types.links import AccountListResponse, AccountRetrieveResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAccounts:
    strict_client = Moneykit(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Moneykit(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_retrieve(self, client: Moneykit) -> None:
        account = client.links.accounts.retrieve(
            "string",
            id="mk_eqkWN34UEoa2NxyALG8pcV",
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    def test_method_list(self, client: Moneykit) -> None:
        account = client.links.accounts.list(
            "string",
        )
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Moneykit) -> None:
        account = client.links.accounts.list(
            "string",
            account_ids=["string", "string", "string"],
        )
        assert_matches_type(AccountListResponse, account, path=["response"])


class TestAsyncAccounts:
    strict_client = AsyncMoneykit(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncMoneykit(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_retrieve(self, client: AsyncMoneykit) -> None:
        account = await client.links.accounts.retrieve(
            "string",
            id="mk_eqkWN34UEoa2NxyALG8pcV",
        )
        assert_matches_type(AccountRetrieveResponse, account, path=["response"])

    @parametrize
    async def test_method_list(self, client: AsyncMoneykit) -> None:
        account = await client.links.accounts.list(
            "string",
        )
        assert_matches_type(AccountListResponse, account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncMoneykit) -> None:
        account = await client.links.accounts.list(
            "string",
            account_ids=["string", "string", "string"],
        )
        assert_matches_type(AccountListResponse, account, path=["response"])
