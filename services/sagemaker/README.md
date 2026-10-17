# capo-sagemaker: typed, async Python SDK for AWS Sagemaker

`capo-sagemaker` is a typed Python SDK for AWS Sagemaker. It has an async client, `AsyncSageMakerClient`, for asyncio and trio, and a sync client, `SageMakerClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/sagemaker/](https://capo-sdk.dev/services/sagemaker/)

## Installation

```
pip install capo-sagemaker
```

## Usage

```python
from capo_sagemaker import AsyncSageMakerClient


async def main():
    async with AsyncSageMakerClient() as sage_maker:
        # Example: call the add_association operation
        response = await sage_maker.add_association()
        print(response["source_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_sagemaker import AsyncSageMakerClient


async def main():
    async with AsyncSageMakerClient() as sage_maker:
        # Example: paginate over create_hub_content_presigned_urls
        async for item in sage_maker.iter_create_hub_content_presigned_urls():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_sagemaker import AsyncSageMakerClient
from capo_sagemaker.error import ResourceLimitExceeded


async def main():
    async with AsyncSageMakerClient() as sage_maker:
        try:
            await sage_maker.add_association()
        except ResourceLimitExceeded as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_sagemaker import AsyncSageMakerClient


async def main():
    async with AsyncSageMakerClient() as sage_maker:
        # Default: 3 attempts for every operation
        response = await sage_maker.add_association()

        # Override per operation
        response = await sage_maker.add_association(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await sage_maker.add_association(config_overrides={"retry_max_attempts": 1})
```
