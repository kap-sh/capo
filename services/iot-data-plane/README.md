# capo-iot-data-plane: typed, async Python SDK for AWS IOT Data Plane

`capo-iot-data-plane` is a typed Python SDK for AWS IOT Data Plane. It has an async client, `AsyncIoTDataPlaneClient`, for asyncio and trio, and a sync client, `IoTDataPlaneClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/iot-data-plane/](https://capo-sdk.dev/services/iot-data-plane/)

## Installation

```
pip install capo-iot-data-plane
```

## Usage

```python
from capo_iot_data_plane import AsyncIoTDataPlaneClient


async def main():
    async with AsyncIoTDataPlaneClient() as io_t_data_plane:
        # Example: call the delete_connection operation
        response = await io_t_data_plane.delete_connection()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_iot_data_plane import AsyncIoTDataPlaneClient


async def main():
    async with AsyncIoTDataPlaneClient() as io_t_data_plane:
        # Example: paginate over list_retained_messages
        async for item in io_t_data_plane.iter_list_retained_messages():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_iot_data_plane import AsyncIoTDataPlaneClient
from capo_iot_data_plane.error import ForbiddenException


async def main():
    async with AsyncIoTDataPlaneClient() as io_t_data_plane:
        try:
            await io_t_data_plane.delete_connection()
        except ForbiddenException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_iot_data_plane import AsyncIoTDataPlaneClient


async def main():
    async with AsyncIoTDataPlaneClient() as io_t_data_plane:
        # Default: 3 attempts for every operation
        response = await io_t_data_plane.delete_connection()

        # Override per operation
        response = await io_t_data_plane.delete_connection(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await io_t_data_plane.delete_connection(config_overrides={"retry_max_attempts": 1})
```
