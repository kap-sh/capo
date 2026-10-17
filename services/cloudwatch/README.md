# capo-cloudwatch: typed, async Python SDK for AWS Cloudwatch

`capo-cloudwatch` is a typed Python SDK for AWS Cloudwatch. It has an async client, `AsyncCloudWatchClient`, for asyncio and trio, and a sync client, `CloudWatchClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/cloudwatch/](https://capo-sdk.dev/services/cloudwatch/)

## Installation

```
pip install capo-cloudwatch
```

## Usage

```python
from capo_cloudwatch import AsyncCloudWatchClient


async def main():
    async with AsyncCloudWatchClient() as cloud_watch:
        # Example: call the associate_dataset_kms_key operation
        response = await cloud_watch.associate_dataset_kms_key()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_cloudwatch import AsyncCloudWatchClient


async def main():
    async with AsyncCloudWatchClient() as cloud_watch:
        # Example: paginate over describe_alarm_history
        async for item in cloud_watch.iter_describe_alarm_history():
            print(item)
```

## Waiters

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_until_` prefixed method.

```python
from capo_cloudwatch import AsyncCloudWatchClient


async def main():
    async with AsyncCloudWatchClient() as cloud_watch:
        # Example: wait for alarm_mute_rule_exists
        await cloud_watch.wait_until_alarm_mute_rule_exists(max_wait_time=300)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cloudwatch import AsyncCloudWatchClient
from capo_cloudwatch.error import ConflictException


async def main():
    async with AsyncCloudWatchClient() as cloud_watch:
        try:
            await cloud_watch.associate_dataset_kms_key()
        except ConflictException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cloudwatch import AsyncCloudWatchClient


async def main():
    async with AsyncCloudWatchClient() as cloud_watch:
        # Default: 3 attempts for every operation
        response = await cloud_watch.associate_dataset_kms_key()

        # Override per operation
        response = await cloud_watch.associate_dataset_kms_key(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cloud_watch.associate_dataset_kms_key(config_overrides={"retry_max_attempts": 1})
```
