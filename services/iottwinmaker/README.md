# capo-iottwinmaker: typed, async Python SDK for AWS Iottwinmaker

`capo-iottwinmaker` is a typed Python SDK for AWS Iottwinmaker. It has an async client, `AsyncIoTTwinMakerClient`, for asyncio and trio, and a sync client, `IoTTwinMakerClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/iottwinmaker/](https://capo-sdk.dev/services/iottwinmaker/)

## Installation

```
pip install capo-iottwinmaker
```

## Usage

```python
from capo_iottwinmaker import AsyncIoTTwinMakerClient


async def main():
    async with AsyncIoTTwinMakerClient() as io_t_twin_maker:
        # Example: call the batch_put_property_values operation
        response = await io_t_twin_maker.batch_put_property_values()
        print(response["error_entries"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_iottwinmaker import AsyncIoTTwinMakerClient


async def main():
    async with AsyncIoTTwinMakerClient() as io_t_twin_maker:
        # Example: paginate over execute_query
        async for item in io_t_twin_maker.iter_execute_query():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_iottwinmaker import AsyncIoTTwinMakerClient
from capo_iottwinmaker.error import InternalServerException


async def main():
    async with AsyncIoTTwinMakerClient() as io_t_twin_maker:
        try:
            await io_t_twin_maker.batch_put_property_values()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_iottwinmaker import AsyncIoTTwinMakerClient


async def main():
    async with AsyncIoTTwinMakerClient() as io_t_twin_maker:
        # Default: 3 attempts for every operation
        response = await io_t_twin_maker.batch_put_property_values()

        # Override per operation
        response = await io_t_twin_maker.batch_put_property_values(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await io_t_twin_maker.batch_put_property_values(config_overrides={"retry_max_attempts": 1})
```
