# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
import asyncio
from typing import Dict, Union, Mapping, Optional
from typing_extensions import Literal

import httpx

from . import resources
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._version import __version__
from ._streaming import Stream as Stream
from ._streaming import AsyncStream as AsyncStream
from ._base_client import (
    DEFAULT_LIMITS,
    DEFAULT_TIMEOUT,
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "ENVIRONMENTS",
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Moneykit",
    "AsyncMoneykit",
    "Client",
    "AsyncClient",
]

ENVIRONMENTS: Dict[str, str] = {
    "production": "https://production.moneykit.com",
    "sandbox": "https://sandbox.moneykit.com",
}


class Moneykit(SyncAPIClient):
    links: resources.Links
    auth: resources.Auth
    institutions: resources.Institutions
    link_session: resources.LinkSession
    users: resources.Users
    well_known: resources.WellKnown

    # client options
    api_key: str

    _environment: Literal["production", "sandbox"]

    def __init__(
        self,
        *,
        environment: Literal["production", "sandbox"] = "production",
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Optional[Transport] = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: Optional[ProxiesTypes] = None,
        # See httpx documentation for [limits](https://www.python-httpx.org/advanced/#pool-limit-configuration)
        connection_pool_limits: httpx.Limits | None = DEFAULT_LIMITS,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous moneykit client instance.

        This automatically infers the `api_key` argument from the `MONEYKIT_API_KEY` environment variable if it is not provided.
        """
        api_key = api_key or os.environ.get("MONEYKIT_API_KEY", None)
        if not api_key:
            raise Exception(
                "The api_key client option must be set either by passing api_key to the client or by setting the MONEYKIT_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        if base_url is None:
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            transport=transport,
            proxies=proxies,
            limits=connection_pool_limits,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.links = resources.Links(self)
        self.auth = resources.Auth(self)
        self.institutions = resources.Institutions(self)
        self.link_session = resources.LinkSession(self)
        self.users = resources.Users(self)
        self.well_known = resources.WellKnown(self)

    @property
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "sandbox"] | None = None,
        base_url: str | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        connection_pool_limits: httpx.Limits | NotGiven = NOT_GIVEN,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
    ) -> Moneykit:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.

        It should be noted that this does not share the underlying httpx client class which may lead
        to performance issues.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        # TODO: share the same httpx client between instances
        return self.__class__(
            base_url=base_url or str(self.base_url),
            environment=environment or self._environment,
            api_key=api_key or self.api_key,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            connection_pool_limits=self._limits
            if isinstance(connection_pool_limits, NotGiven)
            else connection_pool_limits,
            max_retries=self.max_retries if isinstance(max_retries, NotGiven) else max_retries,
            default_headers=headers,
            default_query=params,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def __del__(self) -> None:
        self.close()


class AsyncMoneykit(AsyncAPIClient):
    links: resources.AsyncLinks
    auth: resources.AsyncAuth
    institutions: resources.AsyncInstitutions
    link_session: resources.AsyncLinkSession
    users: resources.AsyncUsers
    well_known: resources.AsyncWellKnown

    # client options
    api_key: str

    _environment: Literal["production", "sandbox"]

    def __init__(
        self,
        *,
        environment: Literal["production", "sandbox"] = "production",
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # See httpx documentation for [custom transports](https://www.python-httpx.org/advanced/#custom-transports)
        transport: Optional[Transport] = None,
        # See httpx documentation for [proxies](https://www.python-httpx.org/advanced/#http-proxying)
        proxies: Optional[ProxiesTypes] = None,
        # See httpx documentation for [limits](https://www.python-httpx.org/advanced/#pool-limit-configuration)
        connection_pool_limits: httpx.Limits | None = DEFAULT_LIMITS,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async moneykit client instance.

        This automatically infers the `api_key` argument from the `MONEYKIT_API_KEY` environment variable if it is not provided.
        """
        api_key = api_key or os.environ.get("MONEYKIT_API_KEY", None)
        if not api_key:
            raise Exception(
                "The api_key client option must be set either by passing api_key to the client or by setting the MONEYKIT_API_KEY environment variable"
            )
        self.api_key = api_key

        self._environment = environment

        if base_url is None:
            try:
                base_url = ENVIRONMENTS[environment]
            except KeyError as exc:
                raise ValueError(f"Unknown environment: {environment}") from exc

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            transport=transport,
            proxies=proxies,
            limits=connection_pool_limits,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.links = resources.AsyncLinks(self)
        self.auth = resources.AsyncAuth(self)
        self.institutions = resources.AsyncInstitutions(self)
        self.link_session = resources.AsyncLinkSession(self)
        self.users = resources.AsyncUsers(self)
        self.well_known = resources.AsyncWellKnown(self)

    @property
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    def copy(
        self,
        *,
        api_key: str | None = None,
        environment: Literal["production", "sandbox"] | None = None,
        base_url: str | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        connection_pool_limits: httpx.Limits | NotGiven = NOT_GIVEN,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
    ) -> AsyncMoneykit:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.

        It should be noted that this does not share the underlying httpx client class which may lead
        to performance issues.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        # TODO: share the same httpx client between instances
        return self.__class__(
            base_url=base_url or str(self.base_url),
            environment=environment or self._environment,
            api_key=api_key or self.api_key,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            connection_pool_limits=self._limits
            if isinstance(connection_pool_limits, NotGiven)
            else connection_pool_limits,
            max_retries=self.max_retries if isinstance(max_retries, NotGiven) else max_retries,
            default_headers=headers,
            default_query=params,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def __del__(self) -> None:
        try:
            asyncio.get_running_loop().create_task(self.close())
        except Exception:
            pass


Client = Moneykit

AsyncClient = AsyncMoneykit
