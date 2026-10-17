# capo-quicksight: typed, async Python SDK for AWS Quicksight

`capo-quicksight` is a typed Python SDK for AWS Quicksight. It has an async client, `AsyncQuickSightClient`, for asyncio and trio, and a sync client, `QuickSightClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/quicksight/](https://capo-sdk.dev/services/quicksight/)

## Installation

```
pip install capo-quicksight
```

## Usage

```python
from capo_quicksight import AsyncQuickSightClient


async def main():
    async with AsyncQuickSightClient() as quick_sight:
        # Example: call the batch_create_topic_reviewed_answer operation
        response = await quick_sight.batch_create_topic_reviewed_answer()
        print(response["topic_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_quicksight import AsyncQuickSightClient


async def main():
    async with AsyncQuickSightClient() as quick_sight:
        # Example: paginate over describe_folder_permissions
        async for item in quick_sight.iter_describe_folder_permissions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_quicksight import AsyncQuickSightClient
from capo_quicksight.error import AccessDeniedException


async def main():
    async with AsyncQuickSightClient() as quick_sight:
        try:
            await quick_sight.batch_create_topic_reviewed_answer()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_quicksight import AsyncQuickSightClient


async def main():
    async with AsyncQuickSightClient() as quick_sight:
        # Default: 3 attempts for every operation
        response = await quick_sight.batch_create_topic_reviewed_answer()

        # Override per operation
        response = await quick_sight.batch_create_topic_reviewed_answer(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await quick_sight.batch_create_topic_reviewed_answer(config_overrides={"retry_max_attempts": 1})
```
