# capo-mediaconnect: typed, async Python SDK for AWS Mediaconnect

`capo-mediaconnect` is a typed Python SDK for AWS Mediaconnect. It has an async client, `AsyncMediaConnectClient`, for asyncio and trio, and a sync client, `MediaConnectClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/mediaconnect/](https://capo-sdk.dev/services/mediaconnect/)

## Installation

```
pip install capo-mediaconnect
```

## Usage

```python
from capo_mediaconnect import AsyncMediaConnectClient


async def main():
    async with AsyncMediaConnectClient() as media_connect:
        # Example: call the list_entitlements operation
        response = await media_connect.list_entitlements()
        print(response["entitlements"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_mediaconnect import AsyncMediaConnectClient


async def main():
    async with AsyncMediaConnectClient() as media_connect:
        # Example: paginate over list_entitlements
        async for item in media_connect.iter_list_entitlements():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_mediaconnect import AsyncMediaConnectClient
from capo_mediaconnect.error import BadRequestException


async def main():
    async with AsyncMediaConnectClient() as media_connect:
        try:
            await media_connect.list_entitlements()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_mediaconnect import AsyncMediaConnectClient


async def main():
    async with AsyncMediaConnectClient() as media_connect:
        # Default: 3 attempts for every operation
        response = await media_connect.list_entitlements()

        # Override per operation
        response = await media_connect.list_entitlements(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await media_connect.list_entitlements(config_overrides={"retry_max_attempts": 1})
```
