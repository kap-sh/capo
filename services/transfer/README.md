# capo-transfer: typed, async Python SDK for AWS Transfer

`capo-transfer` is a typed Python SDK for AWS Transfer. It has an async client, `AsyncTransferClient`, for asyncio and trio, and a sync client, `TransferClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/transfer/](https://capo-sdk.dev/services/transfer/)

## Installation

```
pip install capo-transfer
```

## Usage

```python
from capo_transfer import AsyncTransferClient


async def main():
    async with AsyncTransferClient() as transfer:
        # Example: call the create_access operation
        response = await transfer.create_access()
        print(response["server_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_transfer import AsyncTransferClient


async def main():
    async with AsyncTransferClient() as transfer:
        # Example: paginate over list_accesses
        async for item in transfer.iter_list_accesses():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_transfer import AsyncTransferClient
from capo_transfer.error import InternalServiceError


async def main():
    async with AsyncTransferClient() as transfer:
        try:
            await transfer.create_access()
        except InternalServiceError as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_transfer import AsyncTransferClient


async def main():
    async with AsyncTransferClient() as transfer:
        # Default: 3 attempts for every operation
        response = await transfer.create_access()

        # Override per operation
        response = await transfer.create_access(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await transfer.create_access(config_overrides={"retry_max_attempts": 1})
```
