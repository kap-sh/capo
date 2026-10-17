# capo-s3tables: typed, async Python SDK for AWS S3Tables

`capo-s3tables` is a typed Python SDK for AWS S3Tables. It has an async client, `AsyncS3TablesClient`, for asyncio and trio, and a sync client, `S3TablesClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/s3tables/](https://capo-sdk.dev/services/s3tables/)

## Installation

```
pip install capo-s3tables
```

## Usage

```python
from capo_s3tables import AsyncS3TablesClient


async def main():
    async with AsyncS3TablesClient() as s3_tables:
        # Example: call the list_tags_for_resource operation
        response = await s3_tables.list_tags_for_resource()
        print(response["tags"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_s3tables import AsyncS3TablesClient


async def main():
    async with AsyncS3TablesClient() as s3_tables:
        # Example: paginate over list_namespaces
        async for item in s3_tables.iter_list_namespaces():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_s3tables import AsyncS3TablesClient
from capo_s3tables.error import BadRequestException


async def main():
    async with AsyncS3TablesClient() as s3_tables:
        try:
            await s3_tables.list_tags_for_resource()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_s3tables import AsyncS3TablesClient


async def main():
    async with AsyncS3TablesClient() as s3_tables:
        # Default: 3 attempts for every operation
        response = await s3_tables.list_tags_for_resource()

        # Override per operation
        response = await s3_tables.list_tags_for_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await s3_tables.list_tags_for_resource(config_overrides={"retry_max_attempts": 1})
```
