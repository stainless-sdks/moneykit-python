# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .account import Account
from ..._models import BaseModel
from ..link_common import LinkCommon

__all__ = ["GetTransactionsResponse", "Transaction"]


class Transaction(BaseModel):
    account_id: str
    """The ID of the account in which this transaction occurred."""

    amount: str
    """The amount of this transaction, denominated in account currency.

    This amount is always non-negative. The `type` field indicates whether it is
    entering or leaving the account.
    """

    currency: str
    """The ISO-4217 currency code of the transaction."""

    pending: bool
    """
    If true, this transaction is pending or unsettled and has not yet affected the
    account. Commonly these are credit card transactions, particularly approvals
    (holds) such as for hotel or restaurant reservations placed in advance where the
    final amount is still to be determined.
    """

    transaction_id: str
    """The unique ID for this transaction."""

    type: Literal["credit", "debit"]
    """An enumeration."""

    category: Optional[str] = None
    """
    The category for this transaction, given as a dotted string indicating a
    hierarchical categorization. See <a href=/pages/categories>Transaction
    Categories</a> for the list of possible transaction types.
    """

    description: Optional[str] = None
    """
    A normalized, cleaned transaction description suitable for presentation to the
    end user. Commonly this will be the merchant or counterparty name.
    """

    raw_description: Optional[str] = None
    """
    The raw transaction description as provided by the institution, where available.
    """


class GetTransactionsResponse(BaseModel):
    accounts: List[Account]
    """A list of accounts for which transactions are being returned."""

    link: LinkCommon
    """The link that these accounts belong to."""

    page: int
    """The page number corresponding to this batch of results."""

    size: int
    """The number of results in this batch."""

    total: int
    """The total number of results for this query."""

    transactions: List[Transaction]
    """A list of transactions."""
