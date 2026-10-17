# capo-s3outposts: typed, async Python SDK for AWS S3Outposts

`capo-s3outposts` is a typed Python SDK for AWS S3Outposts. It has an async client, `AsyncS3OutpostsClient`, for asyncio and trio, and a sync client, `S3OutpostsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/s3outposts/](https://capo-sdk.dev/services/s3outposts/)

## Installation

```
pip install capo-s3outposts
```

## Usage

```python
from capo_s3outposts import AsyncS3OutpostsClient


async def main():
    async with AsyncS3OutpostsClient() as s3_outposts:
        # Example: call the create_endpoint operation
        response = await s3_outposts.create_endpoint()
        print(response["endpoint_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_s3outposts import AsyncS3OutpostsClient


async def main():
    async with AsyncS3OutpostsClient() as s3_outposts:
        # Example: paginate over list_endpoints
        async for item in s3_outposts.iter_list_endpoints():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_s3outposts import AsyncS3OutpostsClient
from capo_s3outposts.error import AccessDeniedException


async def main():
    async with AsyncS3OutpostsClient() as s3_outposts:
        try:
            await s3_outposts.create_endpoint()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_s3outposts import AsyncS3OutpostsClient


async def main():
    async with AsyncS3OutpostsClient() as s3_outposts:
        # Default: 3 attempts for every operation
        response = await s3_outposts.create_endpoint()

        # Override per operation
        response = await s3_outposts.create_endpoint(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3_outposts.create_endpoint(config_overrides={"retry_max_attempts": 1})
```
