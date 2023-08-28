# File generated from our OpenAPI spec by Stainless.

import datetime
from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .link_common import LinkCommon

__all__ = ["TransactionSyncResponse", "Cursor", "Transactions", "TransactionsCreated", "TransactionsUpdated"]


class Cursor(BaseModel):
    next: Optional[str] = None
    """A cursor value pointing to the next result set."""


class TransactionsCreated(BaseModel):
    account_id: str
    """The ID of the account in which this transaction occurred."""

    amount: str
    """The amount of this transaction, denominated in account currency.

    This amount is always non-negative. The `type` field indicates whether it is
    entering or leaving the account.
    """

    currency: str
    """The ISO-4217 currency code of the transaction."""

    date: datetime.date
    """The effective (posted) date of the transaction, in ISO-8601 format.

    For pending transactions, this date is when the transaction was initiated.
    """

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

    datetime: Optional[_datetime.datetime] = None
    """
    If the institution has provided the actual time of the transaction, this field
    contains the full date and time of the transaction, in ISO-8601 format. If the
    time is not available, this field will be null. <p>Note that the time is
    generally reported in the timezone of the institution or the account holder.
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


class TransactionsUpdated(BaseModel):
    account_id: str
    """The ID of the account in which this transaction occurred."""

    amount: str
    """The amount of this transaction, denominated in account currency.

    This amount is always non-negative. The `type` field indicates whether it is
    entering or leaving the account.
    """

    currency: str
    """The ISO-4217 currency code of the transaction."""

    date: datetime.date
    """The effective (posted) date of the transaction, in ISO-8601 format.

    For pending transactions, this date is when the transaction was initiated.
    """

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

    datetime: Optional[_datetime.datetime] = None
    """
    If the institution has provided the actual time of the transaction, this field
    contains the full date and time of the transaction, in ISO-8601 format. If the
    time is not available, this field will be null. <p>Note that the time is
    generally reported in the timezone of the institution or the account holder.
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


class Transactions(BaseModel):
    created: List[TransactionsCreated]
    """
    A list of transactions that have been added to the link ordered by ascending
    datetime.
    """

    removed: List[str]
    """
    A list of transaction ids that have been removed from the link ordered by
    ascending datetime.
    """

    updated: List[TransactionsUpdated]
    """
    A list of transactions that have been updated on the link ordered by ascending
    datetime.
    """


class TransactionSyncResponse(BaseModel):
    cursor: Cursor
    """Pagination information"""

    has_more: bool
    """
    This condition indicates the presence of transaction updates exceeding the
    requested count. If true, additional updates can be retrieved by making an
    additional request with cursor set to next_cursor.
    """

    link: LinkCommon
    """The link that these transactions belong to."""

    transactions: Transactions
    """list of created, updated and removed transactions."""
