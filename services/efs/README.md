# capo-efs: typed, async Python SDK for AWS EFS

`capo-efs` is a typed Python SDK for AWS EFS. It has an async client, `AsyncEFSClient`, for asyncio and trio, and a sync client, `EFSClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/efs/](https://capo-sdk.dev/services/efs/)

## Installation

```
pip install capo-efs
```

## Usage

```python
from capo_efs import AsyncEFSClient


async def main():
    async with AsyncEFSClient() as efs:
        # Example: call the create_access_point operation
        response = await efs.create_access_point()
        print(response["client_token"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_efs import AsyncEFSClient


async def main():
    async with AsyncEFSClient() as efs:
        # Example: paginate over describe_access_points
        async for item in efs.iter_describe_access_points():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_efs import AsyncEFSClient
from capo_efs.error import AccessPointAlreadyExists


async def main():
    async with AsyncEFSClient() as efs:
        try:
            await efs.create_access_point()
        except AccessPointAlreadyExists as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_efs import AsyncEFSClient


async def main():
    async with AsyncEFSClient() as efs:
        # Default: 3 attempts for every operation
        response = await efs.create_access_point()

        # Override per operation
        response = await efs.create_access_point(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await efs.create_access_point(config_overrides={"retry_max_attempts": 1})
```
