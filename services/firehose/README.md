# capo-firehose: typed, async Python SDK for AWS Firehose

`capo-firehose` is a typed Python SDK for AWS Firehose. It has an async client, `AsyncFirehoseClient`, for asyncio and trio, and a sync client, `FirehoseClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/firehose/](https://capo-sdk.dev/services/firehose/)

## Installation

```
pip install capo-firehose
```

## Usage

```python
from capo_firehose import AsyncFirehoseClient


async def main():
    async with AsyncFirehoseClient() as firehose:
        # Example: call the create_delivery_stream operation
        response = await firehose.create_delivery_stream()
        print(response["delivery_stream_arn"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_firehose import AsyncFirehoseClient
from capo_firehose.error import InvalidArgumentException


async def main():
    async with AsyncFirehoseClient() as firehose:
        try:
            await firehose.create_delivery_stream()
        except InvalidArgumentException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_firehose import AsyncFirehoseClient


async def main():
    async with AsyncFirehoseClient() as firehose:
        # Default: 3 attempts for every operation
        response = await firehose.create_delivery_stream()

        # Override per operation
        response = await firehose.create_delivery_stream(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await firehose.create_delivery_stream(config_overrides={"retry_max_attempts": 1})
```
