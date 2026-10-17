# capo-healthlake: typed, async Python SDK for AWS Healthlake

`capo-healthlake` is a typed Python SDK for AWS Healthlake. It has an async client, `AsyncHealthLakeClient`, for asyncio and trio, and a sync client, `HealthLakeClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/healthlake/](https://capo-sdk.dev/services/healthlake/)

## Installation

```
pip install capo-healthlake
```

## Usage

```python
from capo_healthlake import AsyncHealthLakeClient


async def main():
    async with AsyncHealthLakeClient() as health_lake:
        # Example: call the create_data_transformation_profile operation
        response = await health_lake.create_data_transformation_profile()
        print(response["profile_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_healthlake import AsyncHealthLakeClient


async def main():
    async with AsyncHealthLakeClient() as health_lake:
        # Example: paginate over list_data_transformation_jobs
        async for item in health_lake.iter_list_data_transformation_jobs():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_healthlake import AsyncHealthLakeClient
from capo_healthlake.error import AccessDeniedException


async def main():
    async with AsyncHealthLakeClient() as health_lake:
        try:
            await health_lake.create_data_transformation_profile()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_healthlake import AsyncHealthLakeClient


async def main():
    async with AsyncHealthLakeClient() as health_lake:
        # Default: 3 attempts for every operation
        response = await health_lake.create_data_transformation_profile()

        # Override per operation
        response = await health_lake.create_data_transformation_profile(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await health_lake.create_data_transformation_profile(config_overrides={"retry_max_attempts": 1})
```
