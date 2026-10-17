# capo-mq: typed, async Python SDK for AWS MQ

`capo-mq` is a typed Python SDK for AWS MQ. It has an async client, `AsyncmqClient`, for asyncio and trio, and a sync client, `mqClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/mq/](https://capo-sdk.dev/services/mq/)

## Installation

```
pip install capo-mq
```

## Usage

```python
from capo_mq import AsyncmqClient


async def main():
    async with AsyncmqClient() as mq:
        # Example: call the create_broker operation
        response = await mq.create_broker()
        print(response["broker_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_mq import AsyncmqClient


async def main():
    async with AsyncmqClient() as mq:
        # Example: paginate over describe_shared_resources
        async for item in mq.iter_describe_shared_resources():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_mq import AsyncmqClient
from capo_mq.error import BadRequestException


async def main():
    async with AsyncmqClient() as mq:
        try:
            await mq.create_broker()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_mq import AsyncmqClient


async def main():
    async with AsyncmqClient() as mq:
        # Default: 3 attempts for every operation
        response = await mq.create_broker()

        # Override per operation
        response = await mq.create_broker(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await mq.create_broker(config_overrides={"retry_max_attempts": 1})
```
