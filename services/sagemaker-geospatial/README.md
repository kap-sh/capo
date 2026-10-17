# capo-sagemaker-geospatial: typed, async Python SDK for AWS Sagemaker Geospatial

`capo-sagemaker-geospatial` is a typed Python SDK for AWS Sagemaker Geospatial. It has an async client, `AsyncSageMakerGeospatialClient`, for asyncio and trio, and a sync client, `SageMakerGeospatialClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/sagemaker-geospatial/](https://capo-sdk.dev/services/sagemaker-geospatial/)

## Installation

```
pip install capo-sagemaker-geospatial
```

## Usage

```python
from capo_sagemaker_geospatial import AsyncSageMakerGeospatialClient


async def main():
    async with AsyncSageMakerGeospatialClient() as sage_maker_geospatial:
        # Example: call the list_tags_for_resource operation
        response = await sage_maker_geospatial.list_tags_for_resource()
        print(response["tags"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_sagemaker_geospatial import AsyncSageMakerGeospatialClient


async def main():
    async with AsyncSageMakerGeospatialClient() as sage_maker_geospatial:
        # Example: paginate over list_earth_observation_jobs
        async for item in sage_maker_geospatial.iter_list_earth_observation_jobs():
            print(item)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from capo_sagemaker_geospatial import AsyncSageMakerGeospatialClient


async def main():
    async with AsyncSageMakerGeospatialClient() as sage_maker_geospatial:
        # Example: call get_tile and read the streaming response
        async with sage_maker_geospatial.get_tile() as response:
            async for chunk in response["binary_file"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_sagemaker_geospatial import AsyncSageMakerGeospatialClient
from capo_sagemaker_geospatial.error import AccessDeniedException


async def main():
    async with AsyncSageMakerGeospatialClient() as sage_maker_geospatial:
        try:
            await sage_maker_geospatial.list_tags_for_resource()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_sagemaker_geospatial import AsyncSageMakerGeospatialClient


async def main():
    async with AsyncSageMakerGeospatialClient() as sage_maker_geospatial:
        # Default: 3 attempts for every operation
        response = await sage_maker_geospatial.list_tags_for_resource()

        # Override per operation
        response = await sage_maker_geospatial.list_tags_for_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await sage_maker_geospatial.list_tags_for_resource(config_overrides={"retry_max_attempts": 1})
```
