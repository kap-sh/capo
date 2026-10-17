# capo-fms: typed, async Python SDK for AWS FMS

`capo-fms` is a typed Python SDK for AWS FMS. It has an async client, `AsyncFMSClient`, for asyncio and trio, and a sync client, `FMSClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/fms/](https://capo-sdk.dev/services/fms/)

## Installation

```
pip install capo-fms
```

## Usage

```python
from capo_fms import AsyncFMSClient


async def main():
    async with AsyncFMSClient() as fms:
        # Example: call the associate_admin_account operation
        response = await fms.associate_admin_account()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_fms import AsyncFMSClient


async def main():
    async with AsyncFMSClient() as fms:
        # Example: paginate over list_admin_accounts_for_organization
        async for item in fms.iter_list_admin_accounts_for_organization():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_fms import AsyncFMSClient
from capo_fms.error import InternalErrorException


async def main():
    async with AsyncFMSClient() as fms:
        try:
            await fms.associate_admin_account()
        except InternalErrorException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_fms import AsyncFMSClient


async def main():
    async with AsyncFMSClient() as fms:
        # Default: 3 attempts for every operation
        response = await fms.associate_admin_account()

        # Override per operation
        response = await fms.associate_admin_account(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await fms.associate_admin_account(config_overrides={"retry_max_attempts": 1})
```
