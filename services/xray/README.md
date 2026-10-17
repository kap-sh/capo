# capo-xray: typed, async Python SDK for AWS Xray

`capo-xray` is a typed Python SDK for AWS Xray. It has an async client, `AsyncXRayClient`, for asyncio and trio, and a sync client, `XRayClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/xray/](https://capo-sdk.dev/services/xray/)

## Installation

```
pip install capo-xray
```

## Usage

```python
from capo_xray import AsyncXRayClient


async def main():
    async with AsyncXRayClient() as x_ray:
        # Example: call the batch_get_traces operation
        response = await x_ray.batch_get_traces()
        print(response["traces"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_xray import AsyncXRayClient


async def main():
    async with AsyncXRayClient() as x_ray:
        # Example: paginate over batch_get_traces
        async for item in x_ray.iter_batch_get_traces():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_xray import AsyncXRayClient
from capo_xray.error import InvalidRequestException


async def main():
    async with AsyncXRayClient() as x_ray:
        try:
            await x_ray.batch_get_traces()
        except InvalidRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_xray import AsyncXRayClient


async def main():
    async with AsyncXRayClient() as x_ray:
        # Default: 3 attempts for every operation
        response = await x_ray.batch_get_traces()

        # Override per operation
        response = await x_ray.batch_get_traces(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await x_ray.batch_get_traces(config_overrides={"retry_max_attempts": 1})
```
