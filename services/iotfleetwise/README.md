# capo-iotfleetwise: typed, async Python SDK for AWS Iotfleetwise

`capo-iotfleetwise` is a typed Python SDK for AWS Iotfleetwise. It has an async client, `AsyncIoTFleetWiseClient`, for asyncio and trio, and a sync client, `IoTFleetWiseClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/iotfleetwise/](https://capo-sdk.dev/services/iotfleetwise/)

## Installation

```
pip install capo-iotfleetwise
```

## Usage

```python
from capo_iotfleetwise import AsyncIoTFleetWiseClient


async def main():
    async with AsyncIoTFleetWiseClient() as io_t_fleet_wise:
        # Example: call the batch_create_vehicle operation
        response = await io_t_fleet_wise.batch_create_vehicle()
        print(response["vehicles"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_iotfleetwise import AsyncIoTFleetWiseClient


async def main():
    async with AsyncIoTFleetWiseClient() as io_t_fleet_wise:
        # Example: paginate over get_vehicle_status
        async for item in io_t_fleet_wise.iter_get_vehicle_status():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_iotfleetwise import AsyncIoTFleetWiseClient
from capo_iotfleetwise.error import InternalServerException


async def main():
    async with AsyncIoTFleetWiseClient() as io_t_fleet_wise:
        try:
            await io_t_fleet_wise.batch_create_vehicle()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_iotfleetwise import AsyncIoTFleetWiseClient


async def main():
    async with AsyncIoTFleetWiseClient() as io_t_fleet_wise:
        # Default: 3 attempts for every operation
        response = await io_t_fleet_wise.batch_create_vehicle()

        # Override per operation
        response = await io_t_fleet_wise.batch_create_vehicle(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await io_t_fleet_wise.batch_create_vehicle(config_overrides={"retry_max_attempts": 1})
```
