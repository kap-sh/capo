# capo-cloudwatch-events: typed, async Python SDK for AWS Cloudwatch Events

`capo-cloudwatch-events` is a typed Python SDK for AWS Cloudwatch Events. It has an async client, `AsyncCloudWatchEventsClient`, for asyncio and trio, and a sync client, `CloudWatchEventsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/cloudwatch-events/](https://capo-sdk.dev/services/cloudwatch-events/)

## Installation

```
pip install capo-cloudwatch-events
```

## Usage

```python
from capo_cloudwatch_events import AsyncCloudWatchEventsClient


async def main():
    async with AsyncCloudWatchEventsClient() as cloud_watch_events:
        # Example: call the activate_event_source operation
        response = await cloud_watch_events.activate_event_source()
        print(response)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cloudwatch_events import AsyncCloudWatchEventsClient
from capo_cloudwatch_events.error import ConcurrentModificationException


async def main():
    async with AsyncCloudWatchEventsClient() as cloud_watch_events:
        try:
            await cloud_watch_events.activate_event_source()
        except ConcurrentModificationException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cloudwatch_events import AsyncCloudWatchEventsClient


async def main():
    async with AsyncCloudWatchEventsClient() as cloud_watch_events:
        # Default: 3 attempts for every operation
        response = await cloud_watch_events.activate_event_source()

        # Override per operation
        response = await cloud_watch_events.activate_event_source(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cloud_watch_events.activate_event_source(config_overrides={"retry_max_attempts": 1})
```
