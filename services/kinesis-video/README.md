# capo-kinesis-video: typed, async Python SDK for AWS Kinesis Video

`capo-kinesis-video` is a typed Python SDK for AWS Kinesis Video. It has an async client, `AsyncKinesisVideoClient`, for asyncio and trio, and a sync client, `KinesisVideoClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/kinesis-video/](https://capo-sdk.dev/services/kinesis-video/)

## Installation

```
pip install capo-kinesis-video
```

## Usage

```python
from capo_kinesis_video import AsyncKinesisVideoClient


async def main():
    async with AsyncKinesisVideoClient() as kinesis_video:
        # Example: call the create_signaling_channel operation
        response = await kinesis_video.create_signaling_channel()
        print(response["channel_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_kinesis_video import AsyncKinesisVideoClient


async def main():
    async with AsyncKinesisVideoClient() as kinesis_video:
        # Example: paginate over describe_mapped_resource_configuration
        async for item in kinesis_video.iter_describe_mapped_resource_configuration():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_kinesis_video import AsyncKinesisVideoClient
from capo_kinesis_video.error import AccessDeniedException


async def main():
    async with AsyncKinesisVideoClient() as kinesis_video:
        try:
            await kinesis_video.create_signaling_channel()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_kinesis_video import AsyncKinesisVideoClient


async def main():
    async with AsyncKinesisVideoClient() as kinesis_video:
        # Default: 3 attempts for every operation
        response = await kinesis_video.create_signaling_channel()

        # Override per operation
        response = await kinesis_video.create_signaling_channel(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await kinesis_video.create_signaling_channel(config_overrides={"retry_max_attempts": 1})
```
