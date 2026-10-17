# capo-sso: typed, async Python SDK for AWS SSO

`capo-sso` is a typed Python SDK for AWS SSO. It has an async client, `AsyncSSOClient`, for asyncio and trio, and a sync client, `SSOClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/sso/](https://capo-sdk.dev/services/sso/)

## Installation

```
pip install capo-sso
```

## Usage

```python
from capo_sso import AsyncSSOClient


async def main():
    async with AsyncSSOClient() as sso:
        # Example: call the get_role_credentials operation
        response = await sso.get_role_credentials()
        print(response["role_credentials"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_sso import AsyncSSOClient


async def main():
    async with AsyncSSOClient() as sso:
        # Example: paginate over list_account_roles
        async for item in sso.iter_list_account_roles():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_sso import AsyncSSOClient
from capo_sso.error import InvalidRequestException


async def main():
    async with AsyncSSOClient() as sso:
        try:
            await sso.get_role_credentials()
        except InvalidRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_sso import AsyncSSOClient


async def main():
    async with AsyncSSOClient() as sso:
        # Default: 3 attempts for every operation
        response = await sso.get_role_credentials()

        # Override per operation
        response = await sso.get_role_credentials(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await sso.get_role_credentials(config_overrides={"retry_max_attempts": 1})
```
