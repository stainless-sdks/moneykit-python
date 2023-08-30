# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["GetUserTransactionsResponse", "Accounts", "Transaction"]


class Accounts(BaseModel):
    institution_id: str

    link_id: str
    """The unique ID of the link this account belongs to."""

    name: str
    """The account name, according to the institution.

    Note that some institutions allow the end user to nickname the account; in such
    cases this field may be the name assigned by the user
    """

    last_synced_at: Optional[datetime] = None
    """An ISO-8601 timestamp indicating the last time that the account was updated."""


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


class GetUserTransactionsResponse(BaseModel):
    accounts: Dict[str, Accounts]

    page: int
    """The page number corresponding to this batch of results."""

    size: int
    """The number of results in this batch."""

    total: int
    """The total number of results for this query."""

    transactions: List[Transaction]
