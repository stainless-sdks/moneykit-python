# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "LinkResponse",
    "Products",
    "ProductsAccountNumbers",
    "ProductsAccountNumbersSettings",
    "ProductsAccounts",
    "ProductsIdentity",
    "ProductsIdentitySettings",
    "ProductsTransactions",
    "ProductsTransactionsSettings",
]


class ProductsAccountNumbersSettings(BaseModel):
    prefetch: Optional[bool] = None
    """
    If true, the data will be available as soon as possible after linking, even if
    `required` is false. If false, the data will be available after the first manual
    data refresh.
    """

    required: Optional[bool] = None
    """If true, only institutions supporting this product will be available."""


class ProductsAccountNumbers(BaseModel):
    settings: ProductsAccountNumbersSettings

    last_attempted_at: Optional[datetime] = None
    """An ISO-8601 timestamp indicating the last time that the product was attempted."""

    refreshed_at: Optional[datetime] = None
    """An ISO-8601 timestamp indicating the last time that the product was updated."""


class ProductsAccounts(BaseModel):
    last_attempted_at: Optional[datetime] = None
    """An ISO-8601 timestamp indicating the last time that the product was attempted."""

    refreshed_at: Optional[datetime] = None
    """An ISO-8601 timestamp indicating the last time that the product was updated."""


class ProductsIdentitySettings(BaseModel):
    prefetch: Optional[bool] = None
    """
    If true, the data will be available as soon as possible after linking, even if
    `required` is false. If false, the data will be available after the first manual
    data refresh.
    """

    required: Optional[bool] = None
    """If true, only institutions supporting this product will be available."""


class ProductsIdentity(BaseModel):
    settings: ProductsIdentitySettings

    last_attempted_at: Optional[datetime] = None
    """An ISO-8601 timestamp indicating the last time that the product was attempted."""

    refreshed_at: Optional[datetime] = None
    """An ISO-8601 timestamp indicating the last time that the product was updated."""


class ProductsTransactionsSettings(BaseModel):
    extend_history: Optional[bool] = None
    """If true, MoneyKit will attempt to fetch as much transaction history as possible.

    Not all institutions supply the same extent of transaction history. Generally,
    however, at least the past 30 days of transactions are available.
    """

    prefetch: Optional[bool] = None
    """
    If true, the data will be available as soon as possible after linking, even if
    `required` is false. If false, the data will be available after the first manual
    data refresh.
    """

    required: Optional[bool] = None
    """If true, only institutions supporting this product will be available."""


class ProductsTransactions(BaseModel):
    settings: ProductsTransactionsSettings

    last_attempted_at: Optional[datetime] = None
    """An ISO-8601 timestamp indicating the last time that the product was attempted."""

    refreshed_at: Optional[datetime] = None
    """An ISO-8601 timestamp indicating the last time that the product was updated."""


class Products(BaseModel):
    account_numbers: Optional[ProductsAccountNumbers] = None

    accounts: Optional[ProductsAccounts] = None

    identity: Optional[ProductsIdentity] = None

    transactions: Optional[ProductsTransactions] = None


class LinkResponse(BaseModel):
    institution_id: str
    """The unique ID for the institution this link is connected to."""

    institution_name: str
    """The institution name this link is connected to."""

    link_id: str
    """The unique ID for this link."""

    products: Products
    """The granted products available for this link."""

    provider: Literal["moneykit", "finicity", "plaid", "yodlee", "mx", "akoya", "sophtron"]
    """An enumeration."""

    state: Literal["connecting", "awaiting_token_exchange", "connected", "deleted", "error"]
    """An enumeration."""

    error_code: Optional[object] = None
    """An enumeration."""

    last_synced_at: Optional[datetime] = None
    """An ISO-8601 timestamp indicating the last time that the account was updated."""

    tags: Optional[List[str]] = None
    """Arbitrary strings used to describe this link."""

    webhook: Optional[str] = None
    """The webhook url assigned to this link."""
