# capo-eventbridgev2: typed, async Python SDK for AWS Eventbridgev2

`capo-eventbridgev2` is a typed Python SDK for AWS Eventbridgev2. It has an async client, `AsyncEventBridgeV2Client`, for asyncio and trio, and a sync client, `EventBridgeV2Client`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/eventbridgev2/](https://capo-sdk.dev/services/eventbridgev2/)

## Installation

```
pip install capo-eventbridgev2
```

## Usage

```python
from capo_eventbridgev2 import AsyncEventBridgeV2Client


async def main():
    async with AsyncEventBridgeV2Client() as event_bridge_v2:
        # Example: call the create_event_bus operation
        response = await event_bridge_v2.create_event_bus()
        print(response["event_bus_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_eventbridgev2 import AsyncEventBridgeV2Client


async def main():
    async with AsyncEventBridgeV2Client() as event_bridge_v2:
        # Example: paginate over list_event_buses
        async for item in event_bridge_v2.iter_list_event_buses():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_eventbridgev2 import AsyncEventBridgeV2Client
from capo_eventbridgev2.error import AccessDeniedException


async def main():
    async with AsyncEventBridgeV2Client() as event_bridge_v2:
        try:
            await event_bridge_v2.create_event_bus()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_eventbridgev2 import AsyncEventBridgeV2Client


async def main():
    async with AsyncEventBridgeV2Client() as event_bridge_v2:
        # Default: 3 attempts for every operation
        response = await event_bridge_v2.create_event_bus()

        # Override per operation
        response = await event_bridge_v2.create_event_bus(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await event_bridge_v2.create_event_bus(config_overrides={"retry_max_attempts": 1})
```
