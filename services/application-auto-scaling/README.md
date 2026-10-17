# capo-application-auto-scaling: typed, async Python SDK for AWS Application Auto Scaling

`capo-application-auto-scaling` is a typed Python SDK for AWS Application Auto Scaling. It has an async client, `AsyncApplicationAutoScalingClient`, for asyncio and trio, and a sync client, `ApplicationAutoScalingClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/application-auto-scaling/](https://capo-sdk.dev/services/application-auto-scaling/)

## Installation

```
pip install capo-application-auto-scaling
```

## Usage

```python
from capo_application_auto_scaling import AsyncApplicationAutoScalingClient


async def main():
    async with AsyncApplicationAutoScalingClient() as application_auto_scaling:
        # Example: call the delete_scaling_policy operation
        response = await application_auto_scaling.delete_scaling_policy()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_application_auto_scaling import AsyncApplicationAutoScalingClient


async def main():
    async with AsyncApplicationAutoScalingClient() as application_auto_scaling:
        # Example: paginate over describe_scalable_targets
        async for item in application_auto_scaling.iter_describe_scalable_targets():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_application_auto_scaling import AsyncApplicationAutoScalingClient
from capo_application_auto_scaling.error import ConcurrentUpdateException


async def main():
    async with AsyncApplicationAutoScalingClient() as application_auto_scaling:
        try:
            await application_auto_scaling.delete_scaling_policy()
        except ConcurrentUpdateException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_application_auto_scaling import AsyncApplicationAutoScalingClient


async def main():
    async with AsyncApplicationAutoScalingClient() as application_auto_scaling:
        # Default: 3 attempts for every operation
        response = await application_auto_scaling.delete_scaling_policy()

        # Override per operation
        response = await application_auto_scaling.delete_scaling_policy(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await application_auto_scaling.delete_scaling_policy(config_overrides={"retry_max_attempts": 1})
```
