# capo-kinesis-video-signaling: typed, async Python SDK for AWS Kinesis Video Signaling

`capo-kinesis-video-signaling` is a typed Python SDK for AWS Kinesis Video Signaling. It has an async client, `AsyncKinesisVideoSignalingClient`, for asyncio and trio, and a sync client, `KinesisVideoSignalingClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/kinesis-video-signaling/](https://capo-sdk.dev/services/kinesis-video-signaling/)

## Installation

```
pip install capo-kinesis-video-signaling
```

## Usage

```python
from capo_kinesis_video_signaling import AsyncKinesisVideoSignalingClient


async def main():
    async with AsyncKinesisVideoSignalingClient() as kinesis_video_signaling:
        # Example: call the get_ice_server_config operation
        response = await kinesis_video_signaling.get_ice_server_config()
        print(response["ice_server_list"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_kinesis_video_signaling import AsyncKinesisVideoSignalingClient
from capo_kinesis_video_signaling.error import ClientLimitExceededException


async def main():
    async with AsyncKinesisVideoSignalingClient() as kinesis_video_signaling:
        try:
            await kinesis_video_signaling.get_ice_server_config()
        except ClientLimitExceededException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_kinesis_video_signaling import AsyncKinesisVideoSignalingClient


async def main():
    async with AsyncKinesisVideoSignalingClient() as kinesis_video_signaling:
        # Default: 3 attempts for every operation
        response = await kinesis_video_signaling.get_ice_server_config()

        # Override per operation
        response = await kinesis_video_signaling.get_ice_server_config(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await kinesis_video_signaling.get_ice_server_config(config_overrides={"retry_max_attempts": 1})
```
