# capo-applicationcostprofiler: typed, async Python SDK for AWS Applicationcostprofiler

`capo-applicationcostprofiler` is a typed Python SDK for AWS Applicationcostprofiler. It has an async client, `AsyncApplicationCostProfilerClient`, for asyncio and trio, and a sync client, `ApplicationCostProfilerClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/applicationcostprofiler/](https://capo-sdk.dev/services/applicationcostprofiler/)

## Installation

```
pip install capo-applicationcostprofiler
```

## Usage

```python
from capo_applicationcostprofiler import AsyncApplicationCostProfilerClient


async def main():
    async with AsyncApplicationCostProfilerClient() as application_cost_profiler:
        # Example: call the delete_report_definition operation
        response = await application_cost_profiler.delete_report_definition()
        print(response["report_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_applicationcostprofiler import AsyncApplicationCostProfilerClient


async def main():
    async with AsyncApplicationCostProfilerClient() as application_cost_profiler:
        # Example: paginate over list_report_definitions
        async for item in application_cost_profiler.iter_list_report_definitions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_applicationcostprofiler import AsyncApplicationCostProfilerClient
from capo_applicationcostprofiler.error import AccessDeniedException


async def main():
    async with AsyncApplicationCostProfilerClient() as application_cost_profiler:
        try:
            await application_cost_profiler.delete_report_definition()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_applicationcostprofiler import AsyncApplicationCostProfilerClient


async def main():
    async with AsyncApplicationCostProfilerClient() as application_cost_profiler:
        # Default: 3 attempts for every operation
        response = await application_cost_profiler.delete_report_definition()

        # Override per operation
        response = await application_cost_profiler.delete_report_definition(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await application_cost_profiler.delete_report_definition(config_overrides={"retry_max_attempts": 1})
```
