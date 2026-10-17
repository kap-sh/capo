# capo-mediaconvert: typed, async Python SDK for AWS Mediaconvert

`capo-mediaconvert` is a typed Python SDK for AWS Mediaconvert. It has an async client, `AsyncMediaConvertClient`, for asyncio and trio, and a sync client, `MediaConvertClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/mediaconvert/](https://capo-sdk.dev/services/mediaconvert/)

## Installation

```
pip install capo-mediaconvert
```

## Usage

```python
from capo_mediaconvert import AsyncMediaConvertClient


async def main():
    async with AsyncMediaConvertClient() as media_convert:
        # Example: call the associate_certificate operation
        response = await media_convert.associate_certificate()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_mediaconvert import AsyncMediaConvertClient


async def main():
    async with AsyncMediaConvertClient() as media_convert:
        # Example: paginate over describe_endpoints
        async for item in media_convert.iter_describe_endpoints():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_mediaconvert import AsyncMediaConvertClient
from capo_mediaconvert.error import BadRequestException


async def main():
    async with AsyncMediaConvertClient() as media_convert:
        try:
            await media_convert.associate_certificate()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_mediaconvert import AsyncMediaConvertClient


async def main():
    async with AsyncMediaConvertClient() as media_convert:
        # Default: 3 attempts for every operation
        response = await media_convert.associate_certificate()

        # Override per operation
        response = await media_convert.associate_certificate(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await media_convert.associate_certificate(config_overrides={"retry_max_attempts": 1})
```
