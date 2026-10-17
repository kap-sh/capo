# capo-arc-region-switch: typed, async Python SDK for AWS Arc Region Switch

`capo-arc-region-switch` is a typed Python SDK for AWS Arc Region Switch. It has an async client, `AsyncARCRegionswitchClient`, for asyncio and trio, and a sync client, `ARCRegionswitchClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/arc-region-switch/](https://capo-sdk.dev/services/arc-region-switch/)

## Installation

```
pip install capo-arc-region-switch
```

## Usage

```python
from capo_arc_region_switch import AsyncARCRegionswitchClient


async def main():
    async with AsyncARCRegionswitchClient() as arc_regionswitch:
        # Example: call the approve_plan_execution_step operation
        response = await arc_regionswitch.approve_plan_execution_step()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_arc_region_switch import AsyncARCRegionswitchClient


async def main():
    async with AsyncARCRegionswitchClient() as arc_regionswitch:
        # Example: paginate over get_plan_evaluation_status
        async for item in arc_regionswitch.iter_get_plan_evaluation_status():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_arc_region_switch import AsyncARCRegionswitchClient
from capo_arc_region_switch.error import AccessDeniedException


async def main():
    async with AsyncARCRegionswitchClient() as arc_regionswitch:
        try:
            await arc_regionswitch.approve_plan_execution_step()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_arc_region_switch import AsyncARCRegionswitchClient


async def main():
    async with AsyncARCRegionswitchClient() as arc_regionswitch:
        # Default: 3 attempts for every operation
        response = await arc_regionswitch.approve_plan_execution_step()

        # Override per operation
        response = await arc_regionswitch.approve_plan_execution_step(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await arc_regionswitch.approve_plan_execution_step(config_overrides={"retry_max_attempts": 1})
```
