# capo-iot-wireless: typed, async Python SDK for AWS IOT Wireless

`capo-iot-wireless` is a typed Python SDK for AWS IOT Wireless. It has an async client, `AsyncIoTWirelessClient`, for asyncio and trio, and a sync client, `IoTWirelessClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/iot-wireless/](https://capo-sdk.dev/services/iot-wireless/)

## Installation

```
pip install capo-iot-wireless
```

## Usage

```python
from capo_iot_wireless import AsyncIoTWirelessClient


async def main():
    async with AsyncIoTWirelessClient() as io_t_wireless:
        # Example: call the associate_aws_account_with_partner_account operation
        response = await io_t_wireless.associate_aws_account_with_partner_account()
        print(response["sidewalk"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_iot_wireless import AsyncIoTWirelessClient


async def main():
    async with AsyncIoTWirelessClient() as io_t_wireless:
        # Example: paginate over list_destinations
        async for item in io_t_wireless.iter_list_destinations():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_iot_wireless import AsyncIoTWirelessClient
from capo_iot_wireless.error import AccessDeniedException


async def main():
    async with AsyncIoTWirelessClient() as io_t_wireless:
        try:
            await io_t_wireless.associate_aws_account_with_partner_account()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_iot_wireless import AsyncIoTWirelessClient


async def main():
    async with AsyncIoTWirelessClient() as io_t_wireless:
        # Default: 3 attempts for every operation
        response = await io_t_wireless.associate_aws_account_with_partner_account()

        # Override per operation
        response = await io_t_wireless.associate_aws_account_with_partner_account(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await io_t_wireless.associate_aws_account_with_partner_account(config_overrides={"retry_max_attempts": 1})
```
