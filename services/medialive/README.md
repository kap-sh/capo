# capo-medialive: typed, async Python SDK for AWS Medialive

`capo-medialive` is a typed Python SDK for AWS Medialive. It has an async client, `AsyncMediaLiveClient`, for asyncio and trio, and a sync client, `MediaLiveClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/medialive/](https://capo-sdk.dev/services/medialive/)

## Installation

```
pip install capo-medialive
```

## Usage

```python
from capo_medialive import AsyncMediaLiveClient


async def main():
    async with AsyncMediaLiveClient() as media_live:
        # Example: call the accept_input_device_transfer operation
        response = await media_live.accept_input_device_transfer()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_medialive import AsyncMediaLiveClient


async def main():
    async with AsyncMediaLiveClient() as media_live:
        # Example: paginate over describe_schedule
        async for item in media_live.iter_describe_schedule():
            print(item)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from capo_medialive import AsyncMediaLiveClient


async def main():
    async with AsyncMediaLiveClient() as media_live:
        # Example: call describe_input_device_thumbnail and read the streaming response
        async with media_live.describe_input_device_thumbnail() as response:
            async for chunk in response["body"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_medialive import AsyncMediaLiveClient
from capo_medialive.error import BadGatewayException


async def main():
    async with AsyncMediaLiveClient() as media_live:
        try:
            await media_live.accept_input_device_transfer()
        except BadGatewayException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_medialive import AsyncMediaLiveClient


async def main():
    async with AsyncMediaLiveClient() as media_live:
        # Default: 3 attempts for every operation
        response = await media_live.accept_input_device_transfer()

        # Override per operation
        response = await media_live.accept_input_device_transfer(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await media_live.accept_input_device_transfer(config_overrides={"retry_max_attempts": 1})
```
