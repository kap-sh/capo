# capo-account: typed, async Python SDK for AWS Account

`capo-account` is a typed Python SDK for AWS Account. It has an async client, `AsyncAccountClient`, for asyncio and trio, and a sync client, `AccountClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/account/](https://capo-sdk.dev/services/account/)

## Installation

```
pip install capo-account
```

## Usage

```python
from capo_account import AsyncAccountClient


async def main():
    async with AsyncAccountClient() as account:
        # Example: call the put_account_name operation
        response = await account.put_account_name()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_account import AsyncAccountClient


async def main():
    async with AsyncAccountClient() as account:
        # Example: paginate over list_regions
        async for item in account.iter_list_regions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_account import AsyncAccountClient
from capo_account.error import AccessDeniedException


async def main():
    async with AsyncAccountClient() as account:
        try:
            await account.put_account_name()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_account import AsyncAccountClient


async def main():
    async with AsyncAccountClient() as account:
        # Default: 3 attempts for every operation
        response = await account.put_account_name()

        # Override per operation
        response = await account.put_account_name(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await account.put_account_name(config_overrides={"retry_max_attempts": 1})
```
