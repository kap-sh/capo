# capo-kinesis-analytics: typed, async Python SDK for AWS Kinesis Analytics

`capo-kinesis-analytics` is a typed Python SDK for AWS Kinesis Analytics. It has an async client, `AsyncKinesisAnalyticsClient`, for asyncio and trio, and a sync client, `KinesisAnalyticsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/kinesis-analytics/](https://capo-sdk.dev/services/kinesis-analytics/)

## Installation

```
pip install capo-kinesis-analytics
```

## Usage

```python
from capo_kinesis_analytics import AsyncKinesisAnalyticsClient


async def main():
    async with AsyncKinesisAnalyticsClient() as kinesis_analytics:
        # Example: call the add_application_cloud_watch_logging_option operation
        response = await kinesis_analytics.add_application_cloud_watch_logging_option()
        print(response)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_kinesis_analytics import AsyncKinesisAnalyticsClient
from capo_kinesis_analytics.error import ConcurrentModificationException


async def main():
    async with AsyncKinesisAnalyticsClient() as kinesis_analytics:
        try:
            await kinesis_analytics.add_application_cloud_watch_logging_option()
        except ConcurrentModificationException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_kinesis_analytics import AsyncKinesisAnalyticsClient


async def main():
    async with AsyncKinesisAnalyticsClient() as kinesis_analytics:
        # Default: 3 attempts for every operation
        response = await kinesis_analytics.add_application_cloud_watch_logging_option()

        # Override per operation
        response = await kinesis_analytics.add_application_cloud_watch_logging_option(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await kinesis_analytics.add_application_cloud_watch_logging_option(config_overrides={"retry_max_attempts": 1})
```
