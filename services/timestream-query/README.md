# capo-timestream-query: typed, async Python SDK for AWS Timestream Query

`capo-timestream-query` is a typed Python SDK for AWS Timestream Query. It has an async client, `AsyncTimestreamQueryClient`, for asyncio and trio, and a sync client, `TimestreamQueryClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/timestream-query/](https://capo-sdk.dev/services/timestream-query/)

## Installation

```
pip install capo-timestream-query
```

## Usage

```python
from capo_timestream_query import AsyncTimestreamQueryClient


async def main():
    async with AsyncTimestreamQueryClient() as timestream_query:
        # Example: call the cancel_query operation
        response = await timestream_query.cancel_query()
        print(response["cancellation_message"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_timestream_query import AsyncTimestreamQueryClient


async def main():
    async with AsyncTimestreamQueryClient() as timestream_query:
        # Example: paginate over list_scheduled_queries
        async for item in timestream_query.iter_list_scheduled_queries():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_timestream_query import AsyncTimestreamQueryClient
from capo_timestream_query.error import AccessDeniedException


async def main():
    async with AsyncTimestreamQueryClient() as timestream_query:
        try:
            await timestream_query.cancel_query()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_timestream_query import AsyncTimestreamQueryClient


async def main():
    async with AsyncTimestreamQueryClient() as timestream_query:
        # Default: 3 attempts for every operation
        response = await timestream_query.cancel_query()

        # Override per operation
        response = await timestream_query.cancel_query(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await timestream_query.cancel_query(config_overrides={"retry_max_attempts": 1})
```
