# capo-wickr: typed, async Python SDK for AWS Wickr

`capo-wickr` is a typed Python SDK for AWS Wickr. It has an async client, `AsyncWickrClient`, for asyncio and trio, and a sync client, `WickrClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/wickr/](https://capo-sdk.dev/services/wickr/)

## Installation

```
pip install capo-wickr
```

## Usage

```python
from capo_wickr import AsyncWickrClient


async def main():
    async with AsyncWickrClient() as wickr:
        # Example: call the batch_create_user operation
        response = await wickr.batch_create_user()
        print(response["message"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_wickr import AsyncWickrClient


async def main():
    async with AsyncWickrClient() as wickr:
        # Example: paginate over list_blocked_guest_users
        async for item in wickr.iter_list_blocked_guest_users():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_wickr import AsyncWickrClient
from capo_wickr.error import BadRequestError


async def main():
    async with AsyncWickrClient() as wickr:
        try:
            await wickr.batch_create_user()
        except BadRequestError as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_wickr import AsyncWickrClient


async def main():
    async with AsyncWickrClient() as wickr:
        # Default: 3 attempts for every operation
        response = await wickr.batch_create_user()

        # Override per operation
        response = await wickr.batch_create_user(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await wickr.batch_create_user(config_overrides={"retry_max_attempts": 1})
```
