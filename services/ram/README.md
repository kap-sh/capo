# capo-ram: typed, async Python SDK for AWS RAM

`capo-ram` is a typed Python SDK for AWS RAM. It has an async client, `AsyncRAMClient`, for asyncio and trio, and a sync client, `RAMClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/ram/](https://capo-sdk.dev/services/ram/)

## Installation

```
pip install capo-ram
```

## Usage

```python
from capo_ram import AsyncRAMClient


async def main():
    async with AsyncRAMClient() as ram:
        # Example: call the accept_resource_share_invitation operation
        response = await ram.accept_resource_share_invitation()
        print(response["resource_share_invitation"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_ram import AsyncRAMClient


async def main():
    async with AsyncRAMClient() as ram:
        # Example: paginate over get_resource_policies
        async for item in ram.iter_get_resource_policies():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_ram import AsyncRAMClient
from capo_ram.error import IdempotentParameterMismatchException


async def main():
    async with AsyncRAMClient() as ram:
        try:
            await ram.accept_resource_share_invitation()
        except IdempotentParameterMismatchException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_ram import AsyncRAMClient


async def main():
    async with AsyncRAMClient() as ram:
        # Default: 3 attempts for every operation
        response = await ram.accept_resource_share_invitation()

        # Override per operation
        response = await ram.accept_resource_share_invitation(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await ram.accept_resource_share_invitation(config_overrides={"retry_max_attempts": 1})
```
