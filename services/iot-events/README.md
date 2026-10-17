# capo-iot-events: typed, async Python SDK for AWS IOT Events

`capo-iot-events` is a typed Python SDK for AWS IOT Events. It has an async client, `AsyncIoTEventsClient`, for asyncio and trio, and a sync client, `IoTEventsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/iot-events/](https://capo-sdk.dev/services/iot-events/)

## Installation

```
pip install capo-iot-events
```

## Usage

```python
from capo_iot_events import AsyncIoTEventsClient


async def main():
    async with AsyncIoTEventsClient() as io_t_events:
        # Example: call the create_alarm_model operation
        response = await io_t_events.create_alarm_model()
        print(response["creation_time"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_iot_events import AsyncIoTEventsClient
from capo_iot_events.error import InternalFailureException


async def main():
    async with AsyncIoTEventsClient() as io_t_events:
        try:
            await io_t_events.create_alarm_model()
        except InternalFailureException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_iot_events import AsyncIoTEventsClient


async def main():
    async with AsyncIoTEventsClient() as io_t_events:
        # Default: 3 attempts for every operation
        response = await io_t_events.create_alarm_model()

        # Override per operation
        response = await io_t_events.create_alarm_model(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await io_t_events.create_alarm_model(config_overrides={"retry_max_attempts": 1})
```
