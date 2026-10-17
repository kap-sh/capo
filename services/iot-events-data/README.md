# capo-iot-events-data: typed, async Python SDK for AWS IOT Events Data

`capo-iot-events-data` is a typed Python SDK for AWS IOT Events Data. It has an async client, `AsyncIoTEventsDataClient`, for asyncio and trio, and a sync client, `IoTEventsDataClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/iot-events-data/](https://capo-sdk.dev/services/iot-events-data/)

## Installation

```
pip install capo-iot-events-data
```

## Usage

```python
from capo_iot_events_data import AsyncIoTEventsDataClient


async def main():
    async with AsyncIoTEventsDataClient() as io_t_events_data:
        # Example: call the batch_acknowledge_alarm operation
        response = await io_t_events_data.batch_acknowledge_alarm()
        print(response["error_entries"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_iot_events_data import AsyncIoTEventsDataClient
from capo_iot_events_data.error import InternalFailureException


async def main():
    async with AsyncIoTEventsDataClient() as io_t_events_data:
        try:
            await io_t_events_data.batch_acknowledge_alarm()
        except InternalFailureException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_iot_events_data import AsyncIoTEventsDataClient


async def main():
    async with AsyncIoTEventsDataClient() as io_t_events_data:
        # Default: 3 attempts for every operation
        response = await io_t_events_data.batch_acknowledge_alarm()

        # Override per operation
        response = await io_t_events_data.batch_acknowledge_alarm(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await io_t_events_data.batch_acknowledge_alarm(config_overrides={"retry_max_attempts": 1})
```
