# capo-cloudwatch-logs: typed, async Python SDK for AWS Cloudwatch Logs

`capo-cloudwatch-logs` is a typed Python SDK for AWS Cloudwatch Logs. It has an async client, `AsyncCloudWatchLogsClient`, for asyncio and trio, and a sync client, `CloudWatchLogsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/cloudwatch-logs/](https://capo-sdk.dev/services/cloudwatch-logs/)

## Installation

```
pip install capo-cloudwatch-logs
```

## Usage

```python
from capo_cloudwatch_logs import AsyncCloudWatchLogsClient


async def main():
    async with AsyncCloudWatchLogsClient() as cloud_watch_logs:
        # Example: call the associate_kms_key operation
        response = await cloud_watch_logs.associate_kms_key()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_cloudwatch_logs import AsyncCloudWatchLogsClient


async def main():
    async with AsyncCloudWatchLogsClient() as cloud_watch_logs:
        # Example: paginate over describe_configuration_templates
        async for item in cloud_watch_logs.iter_describe_configuration_templates():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cloudwatch_logs import AsyncCloudWatchLogsClient
from capo_cloudwatch_logs.error import InvalidParameterException


async def main():
    async with AsyncCloudWatchLogsClient() as cloud_watch_logs:
        try:
            await cloud_watch_logs.associate_kms_key()
        except InvalidParameterException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cloudwatch_logs import AsyncCloudWatchLogsClient


async def main():
    async with AsyncCloudWatchLogsClient() as cloud_watch_logs:
        # Default: 3 attempts for every operation
        response = await cloud_watch_logs.associate_kms_key()

        # Override per operation
        response = await cloud_watch_logs.associate_kms_key(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cloud_watch_logs.associate_kms_key(config_overrides={"retry_max_attempts": 1})
```
