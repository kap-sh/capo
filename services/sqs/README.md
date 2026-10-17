# capo-sqs: typed, async Python SDK for AWS SQS

`capo-sqs` is a typed Python SDK for AWS SQS. It has an async client, `AsyncSQSClient`, for asyncio and trio, and a sync client, `SQSClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/sqs/](https://capo-sdk.dev/services/sqs/)

## Installation

```
pip install capo-sqs
```

## Usage

```python
from capo_sqs import AsyncSQSClient


async def main():
    async with AsyncSQSClient() as sqs:
        # Example: call the add_permission operation
        response = await sqs.add_permission()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_sqs import AsyncSQSClient


async def main():
    async with AsyncSQSClient() as sqs:
        # Example: paginate over list_dead_letter_source_queues
        async for item in sqs.iter_list_dead_letter_source_queues():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_sqs import AsyncSQSClient
from capo_sqs.error import InvalidAddress


async def main():
    async with AsyncSQSClient() as sqs:
        try:
            await sqs.add_permission()
        except InvalidAddress as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_sqs import AsyncSQSClient


async def main():
    async with AsyncSQSClient() as sqs:
        # Default: 3 attempts for every operation
        response = await sqs.add_permission()

        # Override per operation
        response = await sqs.add_permission(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await sqs.add_permission(config_overrides={"retry_max_attempts": 1})
```
