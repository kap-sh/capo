# capo-ivs: typed, async Python SDK for AWS IVS

`capo-ivs` is a typed Python SDK for AWS IVS. It has an async client, `AsyncivsClient`, for asyncio and trio, and a sync client, `ivsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/ivs/](https://capo-sdk.dev/services/ivs/)

## Installation

```
pip install capo-ivs
```

## Usage

```python
from capo_ivs import AsyncivsClient


async def main():
    async with AsyncivsClient() as ivs:
        # Example: call the batch_get_channel operation
        response = await ivs.batch_get_channel()
        print(response["access_control_allow_origin"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_ivs import AsyncivsClient


async def main():
    async with AsyncivsClient() as ivs:
        # Example: paginate over list_ad_configurations
        async for item in ivs.iter_list_ad_configurations():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_ivs import AsyncivsClient
from capo_ivs.error import AccessDeniedException


async def main():
    async with AsyncivsClient() as ivs:
        try:
            await ivs.batch_get_channel()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_ivs import AsyncivsClient


async def main():
    async with AsyncivsClient() as ivs:
        # Default: 3 attempts for every operation
        response = await ivs.batch_get_channel()

        # Override per operation
        response = await ivs.batch_get_channel(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await ivs.batch_get_channel(config_overrides={"retry_max_attempts": 1})
```
