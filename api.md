# Shared Types

```python
from moneykit.types import SupportedVersion
```

# Links

Types:

```python
from moneykit.types import LinkCommon, LinkResponse
```

Methods:

- <code title="get /links/{id}">client.links.<a href="./src/moneykit/resources/links/links.py">retrieve</a>(id) -> <a href="./src/moneykit/types/link_response.py">LinkResponse</a></code>
- <code title="patch /links/{id}">client.links.<a href="./src/moneykit/resources/links/links.py">update</a>(id, \*\*<a href="src/moneykit/types/link_update_params.py">params</a>) -> <a href="./src/moneykit/types/link_response.py">LinkResponse</a></code>
- <code title="delete /links/{id}">client.links.<a href="./src/moneykit/resources/links/links.py">delete</a>(id) -> None</code>

## Accounts

Types:

```python
from moneykit.types.links import Account, AccountRetrieveResponse, AccountListResponse
```

Methods:

- <code title="get /links/{id}/accounts/{account_id}">client.links.accounts.<a href="./src/moneykit/resources/links/accounts/accounts.py">retrieve</a>(id, account_id) -> <a href="./src/moneykit/types/links/account_retrieve_response.py">AccountRetrieveResponse</a></code>
- <code title="get /links/{id}/accounts">client.links.accounts.<a href="./src/moneykit/resources/links/accounts/accounts.py">list</a>(id, \*\*<a href="src/moneykit/types/links/account_list_params.py">params</a>) -> <a href="./src/moneykit/types/links/account_list_response.py">AccountListResponse</a></code>

### Numbers

Types:

```python
from moneykit.types.links.accounts import NumberListResponse
```

Methods:

- <code title="get /links/{id}/accounts/numbers">client.links.accounts.numbers.<a href="./src/moneykit/resources/links/accounts/numbers.py">list</a>(id) -> <a href="./src/moneykit/types/links/accounts/number_list_response.py">NumberListResponse</a></code>

## Identity

Types:

```python
from moneykit.types.links import IdentityResponse
```

Methods:

- <code title="get /links/{id}/identity">client.links.identity.<a href="./src/moneykit/resources/links/identity.py">retrieve</a>(id, \*\*<a href="src/moneykit/types/links/identity_retrieve_params.py">params</a>) -> <a href="./src/moneykit/types/links/identity_response.py">IdentityResponse</a></code>

## Transactions

Types:

```python
from moneykit.types.links import GetTransactionsResponse, TransactionSyncResponse
```

Methods:

- <code title="get /links/{id}/transactions">client.links.transactions.<a href="./src/moneykit/resources/links/transactions.py">list</a>(id, \*\*<a href="src/moneykit/types/links/transaction_list_params.py">params</a>) -> <a href="./src/moneykit/types/links/get_transactions_response.py">GetTransactionsResponse</a></code>
- <code title="get /links/{id}/transactions/sync">client.links.transactions.<a href="./src/moneykit/resources/links/transactions.py">sync</a>(id, \*\*<a href="src/moneykit/types/links/transaction_sync_params.py">params</a>) -> <a href="./src/moneykit/types/links/transaction_sync_response.py">TransactionSyncResponse</a></code>

## Products

Methods:

- <code title="post /links/{id}/products">client.links.products.<a href="./src/moneykit/resources/links/products.py">create</a>(id, \*\*<a href="src/moneykit/types/links/product_create_params.py">params</a>) -> None</code>

# Auth

## Token

Types:

```python
from moneykit.types.auth import GenerateAccessTokenResponse
```

## Introspect

Types:

```python
from moneykit.types.auth import IntrospectClientResponse
```

Methods:

- <code title="get /auth/introspect">client.auth.introspect.<a href="./src/moneykit/resources/auth/introspect.py">retrieve</a>() -> <a href="./src/moneykit/types/auth/introspect_client_response.py">IntrospectClientResponse</a></code>

# Institutions

Types:

```python
from moneykit.types import GetInstitutionsResponse, Institution
```

Methods:

- <code title="get /institutions/{institution_id}">client.institutions.<a href="./src/moneykit/resources/institutions.py">retrieve</a>(institution_id) -> <a href="./src/moneykit/types/institution.py">Institution</a></code>
- <code title="get /institutions">client.institutions.<a href="./src/moneykit/resources/institutions.py">list</a>(\*\*<a href="src/moneykit/types/institution_list_params.py">params</a>) -> <a href="./src/moneykit/types/get_institutions_response.py">GetInstitutionsResponse</a></code>

# LinkSession

Types:

```python
from moneykit.types import CreateLinkSessionResponse
```

Methods:

- <code title="post /link-session">client.link_session.<a href="./src/moneykit/resources/link_session/link_session.py">create</a>(\*\*<a href="src/moneykit/types/link_session_create_params.py">params</a>) -> <a href="./src/moneykit/types/create_link_session_response.py">CreateLinkSessionResponse</a></code>

## ExchangeToken

Types:

```python
from moneykit.types.link_session import ExchangeTokenResponse
```

Methods:

- <code title="post /link-session/exchange-token">client.link_session.exchange_token.<a href="./src/moneykit/resources/link_session/exchange_token.py">create</a>(\*\*<a href="src/moneykit/types/link_session/exchange_token_create_params.py">params</a>) -> <a href="./src/moneykit/types/link_session/exchange_token_response.py">ExchangeTokenResponse</a></code>

# Users

## Transactions

Types:

```python
from moneykit.types.users import GetUserTransactionsResponse
```

Methods:

- <code title="get /users/{id}/transactions">client.users.transactions.<a href="./src/moneykit/resources/users/transactions.py">list</a>(id, \*\*<a href="src/moneykit/types/users/transaction_list_params.py">params</a>) -> <a href="./src/moneykit/types/users/get_user_transactions_response.py">GetUserTransactionsResponse</a></code>

## Accounts

Types:

```python
from moneykit.types.users import GetUserAccountsResponse
```

Methods:

- <code title="get /users/{id}/accounts">client.users.accounts.<a href="./src/moneykit/resources/users/accounts.py">list</a>(id, \*\*<a href="src/moneykit/types/users/account_list_params.py">params</a>) -> <a href="./src/moneykit/types/users/get_user_accounts_response.py">GetUserAccountsResponse</a></code>

# WellKnown

## Jwks

Types:

```python
from moneykit.types.well_known import JwkSet
```

Methods:

- <code title="get /.well-known/jwks.json">client.well_known.jwks.<a href="./src/moneykit/resources/well_known/jwks.py">json</a>() -> <a href="./src/moneykit/types/well_known/jwk_set.py">JwkSet</a></code>
