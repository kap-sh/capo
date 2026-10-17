# capo-scheduler: typed, async Python SDK for AWS Scheduler

`capo-scheduler` is a typed Python SDK for AWS Scheduler. It has an async client, `AsyncSchedulerClient`, for asyncio and trio, and a sync client, `SchedulerClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/scheduler/](https://capo-sdk.dev/services/scheduler/)

## Installation

```
pip install capo-scheduler
```

## Usage

```python
from capo_scheduler import AsyncSchedulerClient


async def main():
    async with AsyncSchedulerClient() as scheduler:
        # Example: call the list_tags_for_resource operation
        response = await scheduler.list_tags_for_resource()
        print(response["tags"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_scheduler import AsyncSchedulerClient


async def main():
    async with AsyncSchedulerClient() as scheduler:
        # Example: paginate over list_schedules
        async for item in scheduler.iter_list_schedules():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_scheduler import AsyncSchedulerClient
from capo_scheduler.error import InternalServerException


async def main():
    async with AsyncSchedulerClient() as scheduler:
        try:
            await scheduler.list_tags_for_resource()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_scheduler import AsyncSchedulerClient


async def main():
    async with AsyncSchedulerClient() as scheduler:
        # Default: 3 attempts for every operation
        response = await scheduler.list_tags_for_resource()

        # Override per operation
        response = await scheduler.list_tags_for_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await scheduler.list_tags_for_resource(config_overrides={"retry_max_attempts": 1})
```
