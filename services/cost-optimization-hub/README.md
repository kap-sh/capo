# capo-cost-optimization-hub: typed, async Python SDK for AWS Cost Optimization Hub

`capo-cost-optimization-hub` is a typed Python SDK for AWS Cost Optimization Hub. It has an async client, `AsyncCostOptimizationHubClient`, for asyncio and trio, and a sync client, `CostOptimizationHubClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/cost-optimization-hub/](https://capo-sdk.dev/services/cost-optimization-hub/)

## Installation

```
pip install capo-cost-optimization-hub
```

## Usage

```python
from capo_cost_optimization_hub import AsyncCostOptimizationHubClient


async def main():
    async with AsyncCostOptimizationHubClient() as cost_optimization_hub:
        # Example: call the get_preferences operation
        response = await cost_optimization_hub.get_preferences()
        print(response["savings_estimation_mode"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_cost_optimization_hub import AsyncCostOptimizationHubClient


async def main():
    async with AsyncCostOptimizationHubClient() as cost_optimization_hub:
        # Example: paginate over list_efficiency_metrics
        async for item in cost_optimization_hub.iter_list_efficiency_metrics():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cost_optimization_hub import AsyncCostOptimizationHubClient
from capo_cost_optimization_hub.error import AccessDeniedException


async def main():
    async with AsyncCostOptimizationHubClient() as cost_optimization_hub:
        try:
            await cost_optimization_hub.get_preferences()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cost_optimization_hub import AsyncCostOptimizationHubClient


async def main():
    async with AsyncCostOptimizationHubClient() as cost_optimization_hub:
        # Default: 3 attempts for every operation
        response = await cost_optimization_hub.get_preferences()

        # Override per operation
        response = await cost_optimization_hub.get_preferences(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cost_optimization_hub.get_preferences(config_overrides={"retry_max_attempts": 1})
```
