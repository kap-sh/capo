# capo-cloudfront: typed, async Python SDK for AWS Cloudfront

`capo-cloudfront` is a typed Python SDK for AWS Cloudfront. It has an async client, `AsyncCloudFrontClient`, for asyncio and trio, and a sync client, `CloudFrontClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/cloudfront/](https://capo-sdk.dev/services/cloudfront/)

## Installation

```
pip install capo-cloudfront
```

## Usage

```python
from capo_cloudfront import AsyncCloudFrontClient


async def main():
    async with AsyncCloudFrontClient() as cloud_front:
        # Example: call the associate_alias operation
        response = await cloud_front.associate_alias()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_cloudfront import AsyncCloudFrontClient


async def main():
    async with AsyncCloudFrontClient() as cloud_front:
        # Example: paginate over list_cloud_front_origin_access_identities
        async for item in cloud_front.iter_list_cloud_front_origin_access_identities():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cloudfront import AsyncCloudFrontClient
from capo_cloudfront.error import AccessDenied


async def main():
    async with AsyncCloudFrontClient() as cloud_front:
        try:
            await cloud_front.associate_alias()
        except AccessDenied as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cloudfront import AsyncCloudFrontClient


async def main():
    async with AsyncCloudFrontClient() as cloud_front:
        # Default: 3 attempts for every operation
        response = await cloud_front.associate_alias()

        # Override per operation
        response = await cloud_front.associate_alias(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cloud_front.associate_alias(config_overrides={"retry_max_attempts": 1})
```
