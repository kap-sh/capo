# capo-appflow: typed, async Python SDK for AWS Appflow

`capo-appflow` is a typed Python SDK for AWS Appflow. It has an async client, `AsyncAppflowClient`, for asyncio and trio, and a sync client, `AppflowClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/appflow/](https://capo-sdk.dev/services/appflow/)

## Installation

```
pip install capo-appflow
```

## Usage

```python
from capo_appflow import AsyncAppflowClient


async def main():
    async with AsyncAppflowClient() as appflow:
        # Example: call the cancel_flow_executions operation
        response = await appflow.cancel_flow_executions()
        print(response["invalid_executions"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_appflow import AsyncAppflowClient


async def main():
    async with AsyncAppflowClient() as appflow:
        # Example: paginate over describe_connector_profiles
        async for item in appflow.iter_describe_connector_profiles():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_appflow import AsyncAppflowClient
from capo_appflow.error import AccessDeniedException


async def main():
    async with AsyncAppflowClient() as appflow:
        try:
            await appflow.cancel_flow_executions()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_appflow import AsyncAppflowClient


async def main():
    async with AsyncAppflowClient() as appflow:
        # Default: 3 attempts for every operation
        response = await appflow.cancel_flow_executions()

        # Override per operation
        response = await appflow.cancel_flow_executions(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await appflow.cancel_flow_executions(config_overrides={"retry_max_attempts": 1})
```
