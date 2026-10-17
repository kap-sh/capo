# capo-application-insights: typed, async Python SDK for AWS Application Insights

`capo-application-insights` is a typed Python SDK for AWS Application Insights. It has an async client, `AsyncApplicationInsightsClient`, for asyncio and trio, and a sync client, `ApplicationInsightsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/application-insights/](https://capo-sdk.dev/services/application-insights/)

## Installation

```
pip install capo-application-insights
```

## Usage

```python
from capo_application_insights import AsyncApplicationInsightsClient


async def main():
    async with AsyncApplicationInsightsClient() as application_insights:
        # Example: call the add_workload operation
        response = await application_insights.add_workload()
        print(response["workload_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_application_insights import AsyncApplicationInsightsClient


async def main():
    async with AsyncApplicationInsightsClient() as application_insights:
        # Example: paginate over list_applications
        async for item in application_insights.iter_list_applications():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_application_insights import AsyncApplicationInsightsClient
from capo_application_insights.error import InternalServerException


async def main():
    async with AsyncApplicationInsightsClient() as application_insights:
        try:
            await application_insights.add_workload()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_application_insights import AsyncApplicationInsightsClient


async def main():
    async with AsyncApplicationInsightsClient() as application_insights:
        # Default: 3 attempts for every operation
        response = await application_insights.add_workload()

        # Override per operation
        response = await application_insights.add_workload(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await application_insights.add_workload(config_overrides={"retry_max_attempts": 1})
```
