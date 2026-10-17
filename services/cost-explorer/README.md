# capo-cost-explorer: typed, async Python SDK for AWS Cost Explorer

`capo-cost-explorer` is a typed Python SDK for AWS Cost Explorer. It has an async client, `AsyncCostExplorerClient`, for asyncio and trio, and a sync client, `CostExplorerClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/cost-explorer/](https://capo-sdk.dev/services/cost-explorer/)

## Installation

```
pip install capo-cost-explorer
```

## Usage

```python
from capo_cost_explorer import AsyncCostExplorerClient


async def main():
    async with AsyncCostExplorerClient() as cost_explorer:
        # Example: call the create_anomaly_monitor operation
        response = await cost_explorer.create_anomaly_monitor()
        print(response["monitor_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_cost_explorer import AsyncCostExplorerClient


async def main():
    async with AsyncCostExplorerClient() as cost_explorer:
        # Example: paginate over get_anomalies
        async for item in cost_explorer.iter_get_anomalies():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cost_explorer import AsyncCostExplorerClient
from capo_cost_explorer.error import LimitExceededException


async def main():
    async with AsyncCostExplorerClient() as cost_explorer:
        try:
            await cost_explorer.create_anomaly_monitor()
        except LimitExceededException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cost_explorer import AsyncCostExplorerClient


async def main():
    async with AsyncCostExplorerClient() as cost_explorer:
        # Default: 3 attempts for every operation
        response = await cost_explorer.create_anomaly_monitor()

        # Override per operation
        response = await cost_explorer.create_anomaly_monitor(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cost_explorer.create_anomaly_monitor(config_overrides={"retry_max_attempts": 1})
```
