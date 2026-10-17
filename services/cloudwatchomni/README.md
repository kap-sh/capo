# capo-cloudwatchomni: typed, async Python SDK for AWS Cloudwatchomni

`capo-cloudwatchomni` is a typed Python SDK for AWS Cloudwatchomni. It has an async client, `AsyncCloudWatchOmniClient`, for asyncio and trio, and a sync client, `CloudWatchOmniClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/cloudwatchomni/](https://capo-sdk.dev/services/cloudwatchomni/)

## Installation

```
pip install capo-cloudwatchomni
```

## Usage

```python
from capo_cloudwatchomni import AsyncCloudWatchOmniClient


async def main():
    async with AsyncCloudWatchOmniClient() as cloud_watch_omni:
        # Example: call the create_access_grant operation
        response = await cloud_watch_omni.create_access_grant()
        print(response["access_grant"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_cloudwatchomni import AsyncCloudWatchOmniClient


async def main():
    async with AsyncCloudWatchOmniClient() as cloud_watch_omni:
        # Example: paginate over get_context_graph
        async for item in cloud_watch_omni.iter_get_context_graph():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cloudwatchomni import AsyncCloudWatchOmniClient
from capo_cloudwatchomni.error import AccessDeniedException


async def main():
    async with AsyncCloudWatchOmniClient() as cloud_watch_omni:
        try:
            await cloud_watch_omni.create_access_grant()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cloudwatchomni import AsyncCloudWatchOmniClient


async def main():
    async with AsyncCloudWatchOmniClient() as cloud_watch_omni:
        # Default: 3 attempts for every operation
        response = await cloud_watch_omni.create_access_grant()

        # Override per operation
        response = await cloud_watch_omni.create_access_grant(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cloud_watch_omni.create_access_grant(config_overrides={"retry_max_attempts": 1})
```
