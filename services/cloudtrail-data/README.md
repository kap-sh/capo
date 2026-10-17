# capo-cloudtrail-data: typed, async Python SDK for AWS Cloudtrail Data

`capo-cloudtrail-data` is a typed Python SDK for AWS Cloudtrail Data. It has an async client, `AsyncCloudTrailDataClient`, for asyncio and trio, and a sync client, `CloudTrailDataClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/cloudtrail-data/](https://capo-sdk.dev/services/cloudtrail-data/)

## Installation

```
pip install capo-cloudtrail-data
```

## Usage

```python
from capo_cloudtrail_data import AsyncCloudTrailDataClient


async def main():
    async with AsyncCloudTrailDataClient() as cloud_trail_data:
        # Example: call the put_audit_events operation
        response = await cloud_trail_data.put_audit_events()
        print(response["successful"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cloudtrail_data import AsyncCloudTrailDataClient
from capo_cloudtrail_data.error import ChannelInsufficientPermission


async def main():
    async with AsyncCloudTrailDataClient() as cloud_trail_data:
        try:
            await cloud_trail_data.put_audit_events()
        except ChannelInsufficientPermission as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cloudtrail_data import AsyncCloudTrailDataClient


async def main():
    async with AsyncCloudTrailDataClient() as cloud_trail_data:
        # Default: 3 attempts for every operation
        response = await cloud_trail_data.put_audit_events()

        # Override per operation
        response = await cloud_trail_data.put_audit_events(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cloud_trail_data.put_audit_events(config_overrides={"retry_max_attempts": 1})
```
