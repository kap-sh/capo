# capo-mediapackagev2: typed, async Python SDK for AWS Mediapackagev2

`capo-mediapackagev2` is a typed Python SDK for AWS Mediapackagev2. It has an async client, `AsyncMediaPackageV2Client`, for asyncio and trio, and a sync client, `MediaPackageV2Client`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/mediapackagev2/](https://capo-sdk.dev/services/mediapackagev2/)

## Installation

```
pip install capo-mediapackagev2
```

## Usage

```python
from capo_mediapackagev2 import AsyncMediaPackageV2Client


async def main():
    async with AsyncMediaPackageV2Client() as media_package_v2:
        # Example: call the list_tags_for_resource operation
        response = await media_package_v2.list_tags_for_resource()
        print(response["tags"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_mediapackagev2 import AsyncMediaPackageV2Client


async def main():
    async with AsyncMediaPackageV2Client() as media_package_v2:
        # Example: paginate over list_channel_groups
        async for item in media_package_v2.iter_list_channel_groups():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_mediapackagev2 import AsyncMediaPackageV2Client
from capo_mediapackagev2.error import ValidationException


async def main():
    async with AsyncMediaPackageV2Client() as media_package_v2:
        try:
            await media_package_v2.list_tags_for_resource()
        except ValidationException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_mediapackagev2 import AsyncMediaPackageV2Client


async def main():
    async with AsyncMediaPackageV2Client() as media_package_v2:
        # Default: 3 attempts for every operation
        response = await media_package_v2.list_tags_for_resource()

        # Override per operation
        response = await media_package_v2.list_tags_for_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await media_package_v2.list_tags_for_resource(config_overrides={"retry_max_attempts": 1})
```
