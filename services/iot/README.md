# capo-iot: typed, async Python SDK for AWS IOT

`capo-iot` is a typed Python SDK for AWS IOT. It has an async client, `AsyncIoTClient`, for asyncio and trio, and a sync client, `IoTClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/iot/](https://capo-sdk.dev/services/iot/)

## Installation

```
pip install capo-iot
```

## Usage

```python
from capo_iot import AsyncIoTClient


async def main():
    async with AsyncIoTClient() as io_t:
        # Example: call the accept_certificate_transfer operation
        response = await io_t.accept_certificate_transfer()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_iot import AsyncIoTClient


async def main():
    async with AsyncIoTClient() as io_t:
        # Example: paginate over get_behavior_model_training_summaries
        async for item in io_t.iter_get_behavior_model_training_summaries():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_iot import AsyncIoTClient
from capo_iot.error import InternalFailureException


async def main():
    async with AsyncIoTClient() as io_t:
        try:
            await io_t.accept_certificate_transfer()
        except InternalFailureException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_iot import AsyncIoTClient


async def main():
    async with AsyncIoTClient() as io_t:
        # Default: 3 attempts for every operation
        response = await io_t.accept_certificate_transfer()

        # Override per operation
        response = await io_t.accept_certificate_transfer(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await io_t.accept_certificate_transfer(config_overrides={"retry_max_attempts": 1})
```
