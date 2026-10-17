# capo-compute-optimizer: typed, async Python SDK for AWS Compute Optimizer

`capo-compute-optimizer` is a typed Python SDK for AWS Compute Optimizer. It has an async client, `AsyncComputeOptimizerClient`, for asyncio and trio, and a sync client, `ComputeOptimizerClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/compute-optimizer/](https://capo-sdk.dev/services/compute-optimizer/)

## Installation

```
pip install capo-compute-optimizer
```

## Usage

```python
from capo_compute_optimizer import AsyncComputeOptimizerClient


async def main():
    async with AsyncComputeOptimizerClient() as compute_optimizer:
        # Example: call the delete_recommendation_preferences operation
        response = await compute_optimizer.delete_recommendation_preferences()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_compute_optimizer import AsyncComputeOptimizerClient


async def main():
    async with AsyncComputeOptimizerClient() as compute_optimizer:
        # Example: paginate over describe_recommendation_export_jobs
        async for item in compute_optimizer.iter_describe_recommendation_export_jobs():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_compute_optimizer import AsyncComputeOptimizerClient
from capo_compute_optimizer.error import AccessDeniedException


async def main():
    async with AsyncComputeOptimizerClient() as compute_optimizer:
        try:
            await compute_optimizer.delete_recommendation_preferences()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_compute_optimizer import AsyncComputeOptimizerClient


async def main():
    async with AsyncComputeOptimizerClient() as compute_optimizer:
        # Default: 3 attempts for every operation
        response = await compute_optimizer.delete_recommendation_preferences()

        # Override per operation
        response = await compute_optimizer.delete_recommendation_preferences(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await compute_optimizer.delete_recommendation_preferences(config_overrides={"retry_max_attempts": 1})
```
