# capo-kinesis-video-webrtc-storage: typed, async Python SDK for AWS Kinesis Video Webrtc Storage

`capo-kinesis-video-webrtc-storage` is a typed Python SDK for AWS Kinesis Video Webrtc Storage. It has an async client, `AsyncKinesisVideoWebRTCStorageClient`, for asyncio and trio, and a sync client, `KinesisVideoWebRTCStorageClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/kinesis-video-webrtc-storage/](https://capo-sdk.dev/services/kinesis-video-webrtc-storage/)

## Installation

```
pip install capo-kinesis-video-webrtc-storage
```

## Usage

```python
from capo_kinesis_video_webrtc_storage import AsyncKinesisVideoWebRTCStorageClient


async def main():
    async with AsyncKinesisVideoWebRTCStorageClient() as kinesis_video_web_rtc_storage:
        # Example: call the join_storage_session operation
        response = await kinesis_video_web_rtc_storage.join_storage_session()
        print(response)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_kinesis_video_webrtc_storage import AsyncKinesisVideoWebRTCStorageClient
from capo_kinesis_video_webrtc_storage.error import AccessDeniedException


async def main():
    async with AsyncKinesisVideoWebRTCStorageClient() as kinesis_video_web_rtc_storage:
        try:
            await kinesis_video_web_rtc_storage.join_storage_session()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_kinesis_video_webrtc_storage import AsyncKinesisVideoWebRTCStorageClient


async def main():
    async with AsyncKinesisVideoWebRTCStorageClient() as kinesis_video_web_rtc_storage:
        # Default: 3 attempts for every operation
        response = await kinesis_video_web_rtc_storage.join_storage_session()

        # Override per operation
        response = await kinesis_video_web_rtc_storage.join_storage_session(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await kinesis_video_web_rtc_storage.join_storage_session(config_overrides={"retry_max_attempts": 1})
```
