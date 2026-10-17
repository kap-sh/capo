# capo-memorydb: typed, async Python SDK for AWS Memorydb

`capo-memorydb` is a typed Python SDK for AWS Memorydb. It has an async client, `AsyncMemoryDBClient`, for asyncio and trio, and a sync client, `MemoryDBClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/memorydb/](https://capo-sdk.dev/services/memorydb/)

## Installation

```
pip install capo-memorydb
```

## Usage

```python
from capo_memorydb import AsyncMemoryDBClient


async def main():
    async with AsyncMemoryDBClient() as memory_db:
        # Example: call the batch_update_cluster operation
        response = await memory_db.batch_update_cluster()
        print(response["processed_clusters"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_memorydb import AsyncMemoryDBClient


async def main():
    async with AsyncMemoryDBClient() as memory_db:
        # Example: paginate over describe_ac_ls
        async for item in memory_db.iter_describe_ac_ls():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_memorydb import AsyncMemoryDBClient
from capo_memorydb.error import InvalidParameterValueException


async def main():
    async with AsyncMemoryDBClient() as memory_db:
        try:
            await memory_db.batch_update_cluster()
        except InvalidParameterValueException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_memorydb import AsyncMemoryDBClient


async def main():
    async with AsyncMemoryDBClient() as memory_db:
        # Default: 3 attempts for every operation
        response = await memory_db.batch_update_cluster()

        # Override per operation
        response = await memory_db.batch_update_cluster(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await memory_db.batch_update_cluster(config_overrides={"retry_max_attempts": 1})
```
