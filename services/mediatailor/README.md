# capo-mediatailor: typed, async Python SDK for AWS Mediatailor

`capo-mediatailor` is a typed Python SDK for AWS Mediatailor. It has an async client, `AsyncMediaTailorClient`, for asyncio and trio, and a sync client, `MediaTailorClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/mediatailor/](https://capo-sdk.dev/services/mediatailor/)

## Installation

```
pip install capo-mediatailor
```

## Usage

```python
from capo_mediatailor import AsyncMediaTailorClient


async def main():
    async with AsyncMediaTailorClient() as media_tailor:
        # Example: call the configure_logs_for_playback_configuration operation
        response = await media_tailor.configure_logs_for_playback_configuration()
        print(response["percent_enabled"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_mediatailor import AsyncMediaTailorClient


async def main():
    async with AsyncMediaTailorClient() as media_tailor:
        # Example: paginate over list_alerts
        async for item in media_tailor.iter_list_alerts():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_mediatailor import AsyncMediaTailorClient
from capo_mediatailor.error import BadRequestException


async def main():
    async with AsyncMediaTailorClient() as media_tailor:
        try:
            await media_tailor.list_tags_for_resource()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_mediatailor import AsyncMediaTailorClient


async def main():
    async with AsyncMediaTailorClient() as media_tailor:
        # Default: 3 attempts for every operation
        response = await media_tailor.configure_logs_for_playback_configuration()

        # Override per operation
        response = await media_tailor.configure_logs_for_playback_configuration(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await media_tailor.configure_logs_for_playback_configuration(config_overrides={"retry_max_attempts": 1})
```
