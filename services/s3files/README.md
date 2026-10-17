# capo-s3files: typed, async Python SDK for AWS S3Files

`capo-s3files` is a typed Python SDK for AWS S3Files. It has an async client, `AsyncS3FilesClient`, for asyncio and trio, and a sync client, `S3FilesClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/s3files/](https://capo-sdk.dev/services/s3files/)

## Installation

```
pip install capo-s3files
```

## Usage

```python
from capo_s3files import AsyncS3FilesClient


async def main():
    async with AsyncS3FilesClient() as s3_files:
        # Example: call the create_access_point operation
        response = await s3_files.create_access_point()
        print(response["access_point_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_s3files import AsyncS3FilesClient


async def main():
    async with AsyncS3FilesClient() as s3_files:
        # Example: paginate over list_access_points
        async for item in s3_files.iter_list_access_points():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_s3files import AsyncS3FilesClient
from capo_s3files.error import ThrottlingException


async def main():
    async with AsyncS3FilesClient() as s3_files:
        try:
            await s3_files.create_access_point()
        except ThrottlingException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_s3files import AsyncS3FilesClient


async def main():
    async with AsyncS3FilesClient() as s3_files:
        # Default: 3 attempts for every operation
        response = await s3_files.create_access_point()

        # Override per operation
        response = await s3_files.create_access_point(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3_files.create_access_point(config_overrides={"retry_max_attempts": 1})
```
