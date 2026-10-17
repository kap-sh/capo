# capo-kinesis: typed, async Python SDK for AWS Kinesis

`capo-kinesis` is a typed Python SDK for AWS Kinesis. It has an async client, `AsyncKinesisClient`, for asyncio and trio, and a sync client, `KinesisClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/kinesis/](https://capo-sdk.dev/services/kinesis/)

## Installation

```
pip install capo-kinesis
```

## Usage

```python
from capo_kinesis import AsyncKinesisClient


async def main():
    async with AsyncKinesisClient() as kinesis:
        # Example: call the add_tags_to_stream operation
        response = await kinesis.add_tags_to_stream()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_kinesis import AsyncKinesisClient


async def main():
    async with AsyncKinesisClient() as kinesis:
        # Example: paginate over list_channels
        async for item in kinesis.iter_list_channels():
            print(item)
```

## Waiters

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_until_` prefixed method.

```python
from capo_kinesis import AsyncKinesisClient


async def main():
    async with AsyncKinesisClient() as kinesis:
        # Example: wait for stream_not_exists
        await kinesis.wait_until_stream_not_exists(max_wait_time=300)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_kinesis import AsyncKinesisClient
from capo_kinesis.error import AccessDeniedException


async def main():
    async with AsyncKinesisClient() as kinesis:
        try:
            await kinesis.add_tags_to_stream()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_kinesis import AsyncKinesisClient


async def main():
    async with AsyncKinesisClient() as kinesis:
        # Default: 3 attempts for every operation
        response = await kinesis.add_tags_to_stream()

        # Override per operation
        response = await kinesis.add_tags_to_stream(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await kinesis.add_tags_to_stream(config_overrides={"retry_max_attempts": 1})
```
