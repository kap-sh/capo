# capo-auto-scaling-plans: typed, async Python SDK for AWS Auto Scaling Plans

`capo-auto-scaling-plans` is a typed Python SDK for AWS Auto Scaling Plans. It has an async client, `AsyncAutoScalingPlansClient`, for asyncio and trio, and a sync client, `AutoScalingPlansClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/auto-scaling-plans/](https://capo-sdk.dev/services/auto-scaling-plans/)

## Installation

```
pip install capo-auto-scaling-plans
```

## Usage

```python
from capo_auto_scaling_plans import AsyncAutoScalingPlansClient


async def main():
    async with AsyncAutoScalingPlansClient() as auto_scaling_plans:
        # Example: call the create_scaling_plan operation
        response = await auto_scaling_plans.create_scaling_plan()
        print(response["scaling_plan_version"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_auto_scaling_plans import AsyncAutoScalingPlansClient
from capo_auto_scaling_plans.error import ConcurrentUpdateException


async def main():
    async with AsyncAutoScalingPlansClient() as auto_scaling_plans:
        try:
            await auto_scaling_plans.create_scaling_plan()
        except ConcurrentUpdateException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_auto_scaling_plans import AsyncAutoScalingPlansClient


async def main():
    async with AsyncAutoScalingPlansClient() as auto_scaling_plans:
        # Default: 3 attempts for every operation
        response = await auto_scaling_plans.create_scaling_plan()

        # Override per operation
        response = await auto_scaling_plans.create_scaling_plan(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await auto_scaling_plans.create_scaling_plan(config_overrides={"retry_max_attempts": 1})
```
