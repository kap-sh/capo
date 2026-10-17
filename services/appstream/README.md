# capo-appstream: typed, async Python SDK for AWS Appstream

`capo-appstream` is a typed Python SDK for AWS Appstream. It has an async client, `AsyncAppStreamClient`, for asyncio and trio, and a sync client, `AppStreamClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/appstream/](https://capo-sdk.dev/services/appstream/)

## Installation

```
pip install capo-appstream
```

## Usage

```python
from capo_appstream import AsyncAppStreamClient


async def main():
    async with AsyncAppStreamClient() as app_stream:
        # Example: call the associate_app_block_builder_app_block operation
        response = await app_stream.associate_app_block_builder_app_block()
        print(response["app_block_builder_app_block_association"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_appstream import AsyncAppStreamClient


async def main():
    async with AsyncAppStreamClient() as app_stream:
        # Example: paginate over describe_app_block_builder_app_block_associations
        async for item in app_stream.iter_describe_app_block_builder_app_block_associations():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_appstream import AsyncAppStreamClient
from capo_appstream.error import ConcurrentModificationException


async def main():
    async with AsyncAppStreamClient() as app_stream:
        try:
            await app_stream.associate_app_block_builder_app_block()
        except ConcurrentModificationException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_appstream import AsyncAppStreamClient


async def main():
    async with AsyncAppStreamClient() as app_stream:
        # Default: 3 attempts for every operation
        response = await app_stream.associate_app_block_builder_app_block()

        # Override per operation
        response = await app_stream.associate_app_block_builder_app_block(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await app_stream.associate_app_block_builder_app_block(config_overrides={"retry_max_attempts": 1})
```
