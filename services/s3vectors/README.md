# capo-s3vectors: typed, async Python SDK for AWS S3Vectors

`capo-s3vectors` is a typed Python SDK for AWS S3Vectors. It has an async client, `AsyncS3VectorsClient`, for asyncio and trio, and a sync client, `S3VectorsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/s3vectors/](https://capo-sdk.dev/services/s3vectors/)

## Installation

```
pip install capo-s3vectors
```

## Usage

```python
from capo_s3vectors import AsyncS3VectorsClient


async def main():
    async with AsyncS3VectorsClient() as s3_vectors:
        # Example: call the list_tags_for_resource operation
        response = await s3_vectors.list_tags_for_resource()
        print(response["tags"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_s3vectors import AsyncS3VectorsClient


async def main():
    async with AsyncS3VectorsClient() as s3_vectors:
        # Example: paginate over list_vector_buckets
        async for item in s3_vectors.iter_list_vector_buckets():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_s3vectors import AsyncS3VectorsClient
from capo_s3vectors.error import AccessDeniedException


async def main():
    async with AsyncS3VectorsClient() as s3_vectors:
        try:
            await s3_vectors.list_tags_for_resource()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_s3vectors import AsyncS3VectorsClient


async def main():
    async with AsyncS3VectorsClient() as s3_vectors:
        # Default: 3 attempts for every operation
        response = await s3_vectors.list_tags_for_resource()

        # Override per operation
        response = await s3_vectors.list_tags_for_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3_vectors.list_tags_for_resource(config_overrides={"retry_max_attempts": 1})
```
