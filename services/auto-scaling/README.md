# capo-auto-scaling: typed, async Python SDK for AWS Auto Scaling

`capo-auto-scaling` is a typed Python SDK for AWS Auto Scaling. It has an async client, `AsyncAutoScalingClient`, for asyncio and trio, and a sync client, `AutoScalingClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/auto-scaling/](https://capo-sdk.dev/services/auto-scaling/)

## Installation

```
pip install capo-auto-scaling
```

## Usage

```python
from capo_auto_scaling import AsyncAutoScalingClient


async def main():
    async with AsyncAutoScalingClient() as auto_scaling:
        # Example: call the attach_instances operation
        response = await auto_scaling.attach_instances()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_auto_scaling import AsyncAutoScalingClient


async def main():
    async with AsyncAutoScalingClient() as auto_scaling:
        # Example: paginate over describe_auto_scaling_groups
        async for item in auto_scaling.iter_describe_auto_scaling_groups():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_auto_scaling import AsyncAutoScalingClient
from capo_auto_scaling.error import ResourceContentionFault


async def main():
    async with AsyncAutoScalingClient() as auto_scaling:
        try:
            await auto_scaling.attach_instances()
        except ResourceContentionFault as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_auto_scaling import AsyncAutoScalingClient


async def main():
    async with AsyncAutoScalingClient() as auto_scaling:
        # Default: 3 attempts for every operation
        response = await auto_scaling.attach_instances()

        # Override per operation
        response = await auto_scaling.attach_instances(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await auto_scaling.attach_instances(config_overrides={"retry_max_attempts": 1})
```
