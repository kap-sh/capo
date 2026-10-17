# capo-timestream-write: typed, async Python SDK for AWS Timestream Write

`capo-timestream-write` is a typed Python SDK for AWS Timestream Write. It has an async client, `AsyncTimestreamWriteClient`, for asyncio and trio, and a sync client, `TimestreamWriteClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/timestream-write/](https://capo-sdk.dev/services/timestream-write/)

## Installation

```
pip install capo-timestream-write
```

## Usage

```python
from capo_timestream_write import AsyncTimestreamWriteClient


async def main():
    async with AsyncTimestreamWriteClient() as timestream_write:
        # Example: call the create_batch_load_task operation
        response = await timestream_write.create_batch_load_task()
        print(response["task_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_timestream_write import AsyncTimestreamWriteClient


async def main():
    async with AsyncTimestreamWriteClient() as timestream_write:
        # Example: paginate over list_batch_load_tasks
        async for item in timestream_write.iter_list_batch_load_tasks():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_timestream_write import AsyncTimestreamWriteClient
from capo_timestream_write.error import AccessDeniedException


async def main():
    async with AsyncTimestreamWriteClient() as timestream_write:
        try:
            await timestream_write.create_batch_load_task()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_timestream_write import AsyncTimestreamWriteClient


async def main():
    async with AsyncTimestreamWriteClient() as timestream_write:
        # Default: 3 attempts for every operation
        response = await timestream_write.create_batch_load_task()

        # Override per operation
        response = await timestream_write.create_batch_load_task(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await timestream_write.create_batch_load_task(config_overrides={"retry_max_attempts": 1})
```
