# capo-snow-device-management: typed, async Python SDK for AWS Snow Device Management

`capo-snow-device-management` is a typed Python SDK for AWS Snow Device Management. It has an async client, `AsyncSnowDeviceManagementClient`, for asyncio and trio, and a sync client, `SnowDeviceManagementClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/snow-device-management/](https://capo-sdk.dev/services/snow-device-management/)

## Installation

```
pip install capo-snow-device-management
```

## Usage

```python
from capo_snow_device_management import AsyncSnowDeviceManagementClient


async def main():
    async with AsyncSnowDeviceManagementClient() as snow_device_management:
        # Example: call the list_tags_for_resource operation
        response = await snow_device_management.list_tags_for_resource()
        print(response["tags"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_snow_device_management import AsyncSnowDeviceManagementClient


async def main():
    async with AsyncSnowDeviceManagementClient() as snow_device_management:
        # Example: paginate over list_devices
        async for item in snow_device_management.iter_list_devices():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_snow_device_management import AsyncSnowDeviceManagementClient
from capo_snow_device_management.error import InternalServerException


async def main():
    async with AsyncSnowDeviceManagementClient() as snow_device_management:
        try:
            await snow_device_management.list_tags_for_resource()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_snow_device_management import AsyncSnowDeviceManagementClient


async def main():
    async with AsyncSnowDeviceManagementClient() as snow_device_management:
        # Default: 3 attempts for every operation
        response = await snow_device_management.list_tags_for_resource()

        # Override per operation
        response = await snow_device_management.list_tags_for_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await snow_device_management.list_tags_for_resource(config_overrides={"retry_max_attempts": 1})
```
