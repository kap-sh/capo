# capo-ivs-realtime: typed, async Python SDK for AWS IVS Realtime

`capo-ivs-realtime` is a typed Python SDK for AWS IVS Realtime. It has an async client, `AsyncIVSRealTimeClient`, for asyncio and trio, and a sync client, `IVSRealTimeClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/ivs-realtime/](https://capo-sdk.dev/services/ivs-realtime/)

## Installation

```
pip install capo-ivs-realtime
```

## Usage

```python
from capo_ivs_realtime import AsyncIVSRealTimeClient


async def main():
    async with AsyncIVSRealTimeClient() as ivs_real_time:
        # Example: call the create_encoder_configuration operation
        response = await ivs_real_time.create_encoder_configuration()
        print(response["encoder_configuration"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_ivs_realtime import AsyncIVSRealTimeClient


async def main():
    async with AsyncIVSRealTimeClient() as ivs_real_time:
        # Example: paginate over list_compositions
        async for item in ivs_real_time.iter_list_compositions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_ivs_realtime import AsyncIVSRealTimeClient
from capo_ivs_realtime.error import AccessDeniedException


async def main():
    async with AsyncIVSRealTimeClient() as ivs_real_time:
        try:
            await ivs_real_time.create_encoder_configuration()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_ivs_realtime import AsyncIVSRealTimeClient


async def main():
    async with AsyncIVSRealTimeClient() as ivs_real_time:
        # Default: 3 attempts for every operation
        response = await ivs_real_time.create_encoder_configuration()

        # Override per operation
        response = await ivs_real_time.create_encoder_configuration(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await ivs_real_time.create_encoder_configuration(config_overrides={"retry_max_attempts": 1})
```
