# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os

import pytest

from moneykit import Moneykit, AsyncMoneykit
from tests.utils import assert_matches_type
from moneykit.types.users import GetUserAccountsResponse

base_url = os.environ.get("API_BASE_URL", "http://127.0.0.1:4010")
api_key = os.environ.get("API_KEY", "something1234")


class TestAccounts:
    strict_client = Moneykit(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = Moneykit(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    def test_method_list(self, client: Moneykit) -> None:
        account = client.users.accounts.list(
            "string",
        )
        assert_matches_type(GetUserAccountsResponse, account, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Moneykit) -> None:
        account = client.users.accounts.list(
            "string",
            account_id=["x", "x", "x"],
            institution_id=["x", "x", "x"],
        )
        assert_matches_type(GetUserAccountsResponse, account, path=["response"])


class TestAsyncAccounts:
    strict_client = AsyncMoneykit(base_url=base_url, api_key=api_key, _strict_response_validation=True)
    loose_client = AsyncMoneykit(base_url=base_url, api_key=api_key, _strict_response_validation=False)
    parametrize = pytest.mark.parametrize("client", [strict_client, loose_client], ids=["strict", "loose"])

    @parametrize
    async def test_method_list(self, client: AsyncMoneykit) -> None:
        account = await client.users.accounts.list(
            "string",
        )
        assert_matches_type(GetUserAccountsResponse, account, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, client: AsyncMoneykit) -> None:
        account = await client.users.accounts.list(
            "string",
            account_id=["x", "x", "x"],
            institution_id=["x", "x", "x"],
        )
        assert_matches_type(GetUserAccountsResponse, account, path=["response"])
