# capo-cloudcontrol: typed, async Python SDK for AWS Cloudcontrol

`capo-cloudcontrol` is a typed Python SDK for AWS Cloudcontrol. It has an async client, `AsyncCloudControlClient`, for asyncio and trio, and a sync client, `CloudControlClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/cloudcontrol/](https://capo-sdk.dev/services/cloudcontrol/)

## Installation

```
pip install capo-cloudcontrol
```

## Usage

```python
from capo_cloudcontrol import AsyncCloudControlClient


async def main():
    async with AsyncCloudControlClient() as cloud_control:
        # Example: call the cancel_resource_request operation
        response = await cloud_control.cancel_resource_request()
        print(response["progress_event"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_cloudcontrol import AsyncCloudControlClient


async def main():
    async with AsyncCloudControlClient() as cloud_control:
        # Example: paginate over list_resource_requests
        async for item in cloud_control.iter_list_resource_requests():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cloudcontrol import AsyncCloudControlClient
from capo_cloudcontrol.error import ConcurrentModificationException


async def main():
    async with AsyncCloudControlClient() as cloud_control:
        try:
            await cloud_control.cancel_resource_request()
        except ConcurrentModificationException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cloudcontrol import AsyncCloudControlClient


async def main():
    async with AsyncCloudControlClient() as cloud_control:
        # Default: 3 attempts for every operation
        response = await cloud_control.cancel_resource_request()

        # Override per operation
        response = await cloud_control.cancel_resource_request(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cloud_control.cancel_resource_request(config_overrides={"retry_max_attempts": 1})
```
