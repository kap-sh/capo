# capo-mediapackage: typed, async Python SDK for AWS Mediapackage

`capo-mediapackage` is a typed Python SDK for AWS Mediapackage. It has an async client, `AsyncMediaPackageClient`, for asyncio and trio, and a sync client, `MediaPackageClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/mediapackage/](https://capo-sdk.dev/services/mediapackage/)

## Installation

```
pip install capo-mediapackage
```

## Usage

```python
from capo_mediapackage import AsyncMediaPackageClient


async def main():
    async with AsyncMediaPackageClient() as media_package:
        # Example: call the configure_logs operation
        response = await media_package.configure_logs()
        print(response["arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_mediapackage import AsyncMediaPackageClient


async def main():
    async with AsyncMediaPackageClient() as media_package:
        # Example: paginate over list_channels
        async for item in media_package.iter_list_channels():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_mediapackage import AsyncMediaPackageClient
from capo_mediapackage.error import ForbiddenException


async def main():
    async with AsyncMediaPackageClient() as media_package:
        try:
            await media_package.configure_logs()
        except ForbiddenException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_mediapackage import AsyncMediaPackageClient


async def main():
    async with AsyncMediaPackageClient() as media_package:
        # Default: 3 attempts for every operation
        response = await media_package.configure_logs()

        # Override per operation
        response = await media_package.configure_logs(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await media_package.configure_logs(config_overrides={"retry_max_attempts": 1})
```
