# capo-kms: typed, async Python SDK for AWS Key Management Service

`capo-kms` is a typed Python SDK for AWS Key Management Service. It has an async client, `AsyncKMSClient`, for asyncio and trio, and a sync client, `KMSClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/kms/](https://capo-sdk.dev/services/kms/)

## Installation

```
pip install capo-kms
```

## Usage

```python
from capo_kms import AsyncKMSClient


async def main():
    async with AsyncKMSClient() as kms:
        # Example: call the cancel_key_deletion operation
        response = await kms.cancel_key_deletion()
        print(response["key_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_kms import AsyncKMSClient


async def main():
    async with AsyncKMSClient() as kms:
        # Example: paginate over describe_custom_key_stores
        async for item in kms.iter_describe_custom_key_stores():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_kms import AsyncKMSClient
from capo_kms.error import DependencyTimeoutException


async def main():
    async with AsyncKMSClient() as kms:
        try:
            await kms.cancel_key_deletion()
        except DependencyTimeoutException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_kms import AsyncKMSClient


async def main():
    async with AsyncKMSClient() as kms:
        # Default: 3 attempts for every operation
        response = await kms.cancel_key_deletion()

        # Override per operation
        response = await kms.cancel_key_deletion(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await kms.cancel_key_deletion(config_overrides={"retry_max_attempts": 1})
```
