# capo-data-pipeline: typed, async Python SDK for AWS Data Pipeline

`capo-data-pipeline` is a typed Python SDK for AWS Data Pipeline. It has an async client, `AsyncDataPipelineClient`, for asyncio and trio, and a sync client, `DataPipelineClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/data-pipeline/](https://capo-sdk.dev/services/data-pipeline/)

## Installation

```
pip install capo-data-pipeline
```

## Usage

```python
from capo_data_pipeline import AsyncDataPipelineClient


async def main():
    async with AsyncDataPipelineClient() as data_pipeline:
        # Example: call the activate_pipeline operation
        response = await data_pipeline.activate_pipeline()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_data_pipeline import AsyncDataPipelineClient


async def main():
    async with AsyncDataPipelineClient() as data_pipeline:
        # Example: paginate over describe_objects
        async for item in data_pipeline.iter_describe_objects():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_data_pipeline import AsyncDataPipelineClient
from capo_data_pipeline.error import InternalServiceError


async def main():
    async with AsyncDataPipelineClient() as data_pipeline:
        try:
            await data_pipeline.activate_pipeline()
        except InternalServiceError as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_data_pipeline import AsyncDataPipelineClient


async def main():
    async with AsyncDataPipelineClient() as data_pipeline:
        # Default: 3 attempts for every operation
        response = await data_pipeline.activate_pipeline()

        # Override per operation
        response = await data_pipeline.activate_pipeline(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await data_pipeline.activate_pipeline(config_overrides={"retry_max_attempts": 1})
```
