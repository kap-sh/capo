# capo-clouddirectory: typed, async Python SDK for AWS Clouddirectory

`capo-clouddirectory` is a typed Python SDK for AWS Clouddirectory. It has an async client, `AsyncCloudDirectoryClient`, for asyncio and trio, and a sync client, `CloudDirectoryClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/clouddirectory/](https://capo-sdk.dev/services/clouddirectory/)

## Installation

```
pip install capo-clouddirectory
```

## Usage

```python
from capo_clouddirectory import AsyncCloudDirectoryClient


async def main():
    async with AsyncCloudDirectoryClient() as cloud_directory:
        # Example: call the add_facet_to_object operation
        response = await cloud_directory.add_facet_to_object()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_clouddirectory import AsyncCloudDirectoryClient


async def main():
    async with AsyncCloudDirectoryClient() as cloud_directory:
        # Example: paginate over list_applied_schema_arns
        async for item in cloud_directory.iter_list_applied_schema_arns():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_clouddirectory import AsyncCloudDirectoryClient
from capo_clouddirectory.error import AccessDeniedException


async def main():
    async with AsyncCloudDirectoryClient() as cloud_directory:
        try:
            await cloud_directory.add_facet_to_object()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_clouddirectory import AsyncCloudDirectoryClient


async def main():
    async with AsyncCloudDirectoryClient() as cloud_directory:
        # Default: 3 attempts for every operation
        response = await cloud_directory.add_facet_to_object()

        # Override per operation
        response = await cloud_directory.add_facet_to_object(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cloud_directory.add_facet_to_object(config_overrides={"retry_max_attempts": 1})
```
