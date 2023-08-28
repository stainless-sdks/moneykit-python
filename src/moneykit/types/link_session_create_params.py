# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "LinkSessionCreateParams",
    "CustomerUser",
    "CustomerUserEmail",
    "CustomerUserPhone",
    "MoneylinkFeatures",
    "Settings",
    "SettingsLinkPermissions",
    "SettingsLinkPermissionsRequested",
    "SettingsProducts",
    "SettingsProductsAccountNumbers",
    "SettingsProductsIdentity",
    "SettingsProductsTransactions",
]


class LinkSessionCreateParams(TypedDict, total=False):
    customer_user: Required[CustomerUser]
    """Details about your end user.

    These details are used to improve conversion and streamline the linking flow,
    and to support the MoneyID system, which provides enhanced debugging and
    improved privacy controls for your end user.
    """

    redirect_uri: Required[str]
    """
    For Oauth linking, a URI indicating the destination, in your application, where
    the user should be sent after authenticating with the institution. The
    `redirect_uri` should not contain any query parameters, and it must be
    pre-approved by MoneyKit during the customer setup process.
    """

    existing_link_id: Optional[str]
    """
    Supply the existing `link_id` if you are asking the user to reconnect this link.
    """

    institution_id: Optional[str]
    """The ID of the institution you want to link to.

    Providing this will skip the institution selection step. `existing_link_id` will
    take precedence over this field if both are provided.
    """

    link_tags: List[str]
    """You can supply one or more arbitrary strings as tags to describe this link."""

    moneylink_features: MoneylinkFeatures
    """Enables optional testing and UI features."""

    settings: Settings
    """
    If provided, these settings will override your default settings for this
    session.
    """

    webhook: Optional[str]
    """The destination URL to which any webhooks should be sent."""


class CustomerUserEmail(TypedDict, total=False):
    address: Required[str]
    """The user's email address."""

    customer_verified_at: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """
    Optional timestamp that marks when you last verified this email (such as when
    the user most recently clicked a verification url sent to this address). Only
    include this field if you verified the address. You may supply zeros if the time
    (but not the date) is unknown.
    """


class CustomerUserPhone(TypedDict, total=False):
    number: Required[str]
    """The user's phone number, preferably in E164 format, including the country code."""

    country: Literal["US", "GB", "CA"]
    """An enumeration."""

    customer_verified_at: Annotated[Optional[Union[str, datetime]], PropertyInfo(format="iso8601")]
    """
    Optional timestamp that marks when you last verified this number (such as when
    the user most recently returned a verification code sent via SMS to this
    number). Only include this field if you verified the number. You may supply
    zeros if the time (but not the date) is unknown.
    """


class CustomerUser(TypedDict, total=False):
    id: Required[str]
    """Your own unique ID for this user.

    Typically this will be a UUID or primary key from your application.
    """

    email: CustomerUserEmail
    """The user's email address.

    This field is optional, but either email or phone must be provided to enable
    improved link conversion via the MoneyID system.
    """

    phone: CustomerUserPhone
    """The user's mobile phone number.

    This field is optional, but either email or phone must be provided to enable
    improved link conversion via the MoneyID system.
    """


class MoneylinkFeatures(TypedDict, total=False):
    bug_reporter: bool
    """
    If enabled, the user can perform a gesture that displays a bug reporter directly
    in the SDK's UI.
    """

    enable_money_id: bool
    """If enabled, the user can register for, or login into, Money ID."""


class SettingsLinkPermissionsRequested(TypedDict, total=False):
    reason: Required[str]
    """
    A **brief** description of the reason your app wants this data. This description
    will be displayed to the user when permission is requested.
    """

    required: Required[bool]
    """
    If true, only institutions that support this data type will be available, and
    the user **must** grant this permission or the link will not be created. If
    false, then the available institutions list may include those that do not
    support this data type, and even if the user declines to grant this permission,
    the link will still be created (so long as at least one permission is granted).
    """

    scope: Required[Literal["accounts", "account_numbers", "identity", "transactions"]]
    """Permissions that a link has access to. These are accepted by a user."""


class SettingsLinkPermissions(TypedDict, total=False):
    requested: Required[List[SettingsLinkPermissionsRequested]]


class SettingsProductsAccountNumbers(TypedDict, total=False):
    prefetch: bool
    """
    If true, the data will be available as soon as possible after linking, even if
    `required` is false. If false, the data will be available after the first manual
    data refresh.
    """

    required: bool
    """If true, only institutions supporting this product will be available."""


class SettingsProductsIdentity(TypedDict, total=False):
    prefetch: bool
    """
    If true, the data will be available as soon as possible after linking, even if
    `required` is false. If false, the data will be available after the first manual
    data refresh.
    """

    required: bool
    """If true, only institutions supporting this product will be available."""


class SettingsProductsTransactions(TypedDict, total=False):
    extend_history: bool
    """If true, MoneyKit will attempt to fetch as much transaction history as possible.

    Not all institutions supply the same extent of transaction history. Generally,
    however, at least the past 30 days of transactions are available.
    """

    prefetch: bool
    """
    If true, the data will be available as soon as possible after linking, even if
    `required` is false. If false, the data will be available after the first manual
    data refresh.
    """

    required: bool
    """If true, only institutions supporting this product will be available."""


class SettingsProducts(TypedDict, total=False):
    account_numbers: SettingsProductsAccountNumbers

    identity: SettingsProductsIdentity

    transactions: SettingsProductsTransactions


class Settings(TypedDict, total=False):
    countries: Optional[List[Literal["US", "GB", "CA"]]]
    """Restricts the available institutions to those in **any** of these countries."""

    link_permissions: SettingsLinkPermissions
    """A set of permissions that the user will be prompted to grant.

    **Required** permissions will restrict the available institutions list to those
    which support that type of data. The data you will be able to fetch from the
    link is limited to the granted permissions set.
    """

    products: SettingsProducts
    """
    If provided, configures what institutions are available and how data should be
    fetched.
    """

    providers: Optional[List[Literal["moneykit", "finicity", "plaid", "yodlee", "mx", "akoya", "sophtron"]]]
    """
    If provided, restricts the available institutions to those supported by **any**
    of these providers.
    """
