# capo-datasync: typed, async Python SDK for AWS Datasync

`capo-datasync` is a typed Python SDK for AWS Datasync. It has an async client, `AsyncDataSyncClient`, for asyncio and trio, and a sync client, `DataSyncClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/datasync/](https://capo-sdk.dev/services/datasync/)

## Installation

```
pip install capo-datasync
```

## Usage

```python
from capo_datasync import AsyncDataSyncClient


async def main():
    async with AsyncDataSyncClient() as data_sync:
        # Example: call the cancel_task_execution operation
        response = await data_sync.cancel_task_execution()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_datasync import AsyncDataSyncClient


async def main():
    async with AsyncDataSyncClient() as data_sync:
        # Example: paginate over list_agents
        async for item in data_sync.iter_list_agents():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_datasync import AsyncDataSyncClient
from capo_datasync.error import InternalException


async def main():
    async with AsyncDataSyncClient() as data_sync:
        try:
            await data_sync.cancel_task_execution()
        except InternalException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_datasync import AsyncDataSyncClient


async def main():
    async with AsyncDataSyncClient() as data_sync:
        # Default: 3 attempts for every operation
        response = await data_sync.cancel_task_execution()

        # Override per operation
        response = await data_sync.cancel_task_execution(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await data_sync.cancel_task_execution(config_overrides={"retry_max_attempts": 1})
```
