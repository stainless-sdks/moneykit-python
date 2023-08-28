# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ProductCreateParams"]


class ProductCreateParams(TypedDict, total=False):
    products: Required[List[Literal["accounts", "account_numbers", "identity", "transactions"]]]
    """At list of at least one product to refresh."""
