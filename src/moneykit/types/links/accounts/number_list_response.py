# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel
from ...link_common import LinkCommon

__all__ = [
    "NumberListResponse",
    "Account",
    "AccountBalances",
    "AccountNumbers",
    "AccountNumbersACH",
    "AccountNumbersBac",
    "AccountNumbersEft",
    "AccountNumbersInternational",
]


class AccountBalances(BaseModel):
    currency: Literal[
        "AFN",
        "EUR",
        "ALL",
        "DZD",
        "USD",
        "AOA",
        "XCD",
        "ARS",
        "AMD",
        "AWG",
        "AUD",
        "AZN",
        "BSD",
        "BHD",
        "BDT",
        "BBD",
        "BYN",
        "BZD",
        "XOF",
        "BMD",
        "INR",
        "BTN",
        "BOB",
        "BOV",
        "BAM",
        "BWP",
        "NOK",
        "BRL",
        "BND",
        "BGN",
        "BIF",
        "CVE",
        "KHR",
        "XAF",
        "CAD",
        "KYD",
        "CLP",
        "CLF",
        "CNY",
        "COP",
        "COU",
        "KMF",
        "CDF",
        "NZD",
        "CRC",
        "HRK",
        "CUP",
        "CUC",
        "ANG",
        "CZK",
        "DKK",
        "DJF",
        "DOP",
        "EGP",
        "SVC",
        "ERN",
        "SZL",
        "ETB",
        "FKP",
        "FJD",
        "XPF",
        "GMD",
        "GEL",
        "GHS",
        "GIP",
        "GTQ",
        "GBP",
        "GNF",
        "GYD",
        "HTG",
        "HNL",
        "HKD",
        "HUF",
        "ISK",
        "IDR",
        "XDR",
        "IRR",
        "IQD",
        "ILS",
        "JMD",
        "JPY",
        "JOD",
        "KZT",
        "KES",
        "KPW",
        "KRW",
        "KWD",
        "KGS",
        "LAK",
        "LBP",
        "LSL",
        "ZAR",
        "LRD",
        "LYD",
        "CHF",
        "MOP",
        "MKD",
        "MGA",
        "MWK",
        "MYR",
        "MVR",
        "MRU",
        "MUR",
        "XUA",
        "MXN",
        "MXV",
        "MDL",
        "MNT",
        "MAD",
        "MZN",
        "MMK",
        "NAD",
        "NPR",
        "NIO",
        "NGN",
        "OMR",
        "PKR",
        "PAB",
        "PGK",
        "PYG",
        "PEN",
        "PHP",
        "PLN",
        "QAR",
        "RON",
        "RUB",
        "RWF",
        "SHP",
        "WST",
        "STN",
        "SAR",
        "RSD",
        "SCR",
        "SLL",
        "SLE",
        "SGD",
        "XSU",
        "SBD",
        "SOS",
        "SSP",
        "LKR",
        "SDG",
        "SRD",
        "SEK",
        "CHE",
        "CHW",
        "SYP",
        "TWD",
        "TJS",
        "TZS",
        "THB",
        "TOP",
        "TTD",
        "TND",
        "TRY",
        "TMT",
        "UGX",
        "UAH",
        "AED",
        "USN",
        "UYU",
        "UYI",
        "UYW",
        "UZS",
        "VUV",
        "VES",
        "VED",
        "VND",
        "YER",
        "ZMW",
        "ZWL",
        "XBA",
        "XBB",
        "XBC",
        "XBD",
        "XTS",
        "XXX",
        "XAU",
        "XPD",
        "XPT",
        "XAG",
    ]
    """ISO 4217 currency.

    Its enumerants are ISO 4217 currencies except for some special currencies like
    ``XXX`. Enumerants names are lowercase cureency code e.g. :attr:`Currency.eur`,
    :attr:`Currency.usd`.
    """

    available: Optional[float] = None
    """The amount of funds available for use.

    Not all institutions report the available balance. <p>Note that the available
    balance typically does not include overdraft limits.
    """

    current: Optional[float] = None
    """
    The total amount of funds in the account. <p>For credit or loan accounts, a
    positive number indicates the amount owed by the account holder. If the balance
    is negative (this is rare), this indicates an amount owed **to** the account
    holder. <p>For depository or investment accounts, a positive number is the asset
    value of the account. If the balance is negative (this is rare), this indicates
    an overdraft or margin condition.
    """

    limit: Optional[float] = None
    """The credit limit on the account.

    Typically this exists only for credit-type accounts. <p>In some cases, this may
    represent the overdraft limit for depository accounts.
    """


class AccountNumbersACH(BaseModel):
    account_number: str
    """The account number."""

    routing_number: str
    """The routing number."""

    wire_routing_number: Optional[str] = None
    """The wire routing number."""


class AccountNumbersBac(BaseModel):
    account_number: str
    """The account number."""

    sort_code: str
    """The sort code."""


class AccountNumbersEft(BaseModel):
    account_number: str
    """The account number."""

    branch_number: str
    """The branch number."""

    institution_number: str
    """The institution number."""


class AccountNumbersInternational(BaseModel):
    bic: str
    """The BIC."""

    iban: str
    """The IBAN."""


class AccountNumbers(BaseModel):
    ach: List[AccountNumbersACH]
    """List of ACH account numbers."""

    bacs: List[AccountNumbersBac]
    """List of BACS account numbers."""

    eft: List[AccountNumbersEft]
    """List of EFT account numbers."""

    international: List[AccountNumbersInternational]
    """List of international account numbers."""


class Account(BaseModel):
    account_id: str
    """
    MoneyKit's unique ID for the account. <p>The `account_id` is distinct from the
    institution's account number. For accounts that may change account numbers from
    time to time, such as credit cards, MoneyKit attempts to keep the `account_id`
    constant. However, if MoneyKit can't reconcile the new account data with the old
    data, the `account_id` may change.
    """

    account_type: Literal[
        "depository.cash",
        "depository.checking",
        "depository.savings",
        "depository.prepaid",
        "depository.other",
        "credit_card",
        "loan.general",
        "loan.mortgage",
        "loan.other",
        "investment",
        "other",
    ]
    """An enumeration."""

    balances: AccountBalances
    """The balance of funds for this account.

    Note that balances are typically cached and may lag behind actual values at the
    institution. To update balances, please use the
    <a href=#operation/refresh_products>/products</a> endpoint.
    """

    name: str
    """The account name, according to the institution.

    Note that some institutions allow the end user to nickname the account; in such
    cases this field may be the name assigned by the user.
    """

    numbers: AccountNumbers
    """The various types of account numbers."""

    account_mask: Optional[str] = None
    """
    The last four characters (usually digits) of the account number. Note that this
    mask may be non-unique between accounts.
    """


class NumberListResponse(BaseModel):
    accounts: List[Account]

    link: LinkCommon
