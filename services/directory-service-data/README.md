# capo-directory-service-data: typed, async Python SDK for AWS Directory Service Data

`capo-directory-service-data` is a typed Python SDK for AWS Directory Service Data. It has an async client, `AsyncDirectoryServiceDataClient`, for asyncio and trio, and a sync client, `DirectoryServiceDataClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/directory-service-data/](https://capo-sdk.dev/services/directory-service-data/)

## Installation

```
pip install capo-directory-service-data
```

## Usage

```python
from capo_directory_service_data import AsyncDirectoryServiceDataClient


async def main():
    async with AsyncDirectoryServiceDataClient() as directory_service_data:
        # Example: call the add_group_member operation
        response = await directory_service_data.add_group_member()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_directory_service_data import AsyncDirectoryServiceDataClient


async def main():
    async with AsyncDirectoryServiceDataClient() as directory_service_data:
        # Example: paginate over list_group_members
        async for item in directory_service_data.iter_list_group_members():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_directory_service_data import AsyncDirectoryServiceDataClient
from capo_directory_service_data.error import AccessDeniedException


async def main():
    async with AsyncDirectoryServiceDataClient() as directory_service_data:
        try:
            await directory_service_data.add_group_member()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_directory_service_data import AsyncDirectoryServiceDataClient


async def main():
    async with AsyncDirectoryServiceDataClient() as directory_service_data:
        # Default: 3 attempts for every operation
        response = await directory_service_data.add_group_member()

        # Override per operation
        response = await directory_service_data.add_group_member(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await directory_service_data.add_group_member(config_overrides={"retry_max_attempts": 1})
```
