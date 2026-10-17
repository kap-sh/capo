# capo-transcribe: typed, async Python SDK for AWS Transcribe

`capo-transcribe` is a typed Python SDK for AWS Transcribe. It has an async client, `AsyncTranscribeClient`, for asyncio and trio, and a sync client, `TranscribeClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/transcribe/](https://capo-sdk.dev/services/transcribe/)

## Installation

```
pip install capo-transcribe
```

## Usage

```python
from capo_transcribe import AsyncTranscribeClient


async def main():
    async with AsyncTranscribeClient() as transcribe:
        # Example: call the create_call_analytics_category operation
        response = await transcribe.create_call_analytics_category()
        print(response["category_properties"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_transcribe import AsyncTranscribeClient


async def main():
    async with AsyncTranscribeClient() as transcribe:
        # Example: paginate over list_call_analytics_categories
        async for item in transcribe.iter_list_call_analytics_categories():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_transcribe import AsyncTranscribeClient
from capo_transcribe.error import BadRequestException


async def main():
    async with AsyncTranscribeClient() as transcribe:
        try:
            await transcribe.create_call_analytics_category()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_transcribe import AsyncTranscribeClient


async def main():
    async with AsyncTranscribeClient() as transcribe:
        # Default: 3 attempts for every operation
        response = await transcribe.create_call_analytics_category()

        # Override per operation
        response = await transcribe.create_call_analytics_category(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await transcribe.create_call_analytics_category(config_overrides={"retry_max_attempts": 1})
```
