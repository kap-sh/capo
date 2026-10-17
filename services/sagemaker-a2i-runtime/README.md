# capo-sagemaker-a2i-runtime: typed, async Python SDK for AWS Sagemaker A2I Runtime

`capo-sagemaker-a2i-runtime` is a typed Python SDK for AWS Sagemaker A2I Runtime. It has an async client, `AsyncSageMakerA2IRuntimeClient`, for asyncio and trio, and a sync client, `SageMakerA2IRuntimeClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/sagemaker-a2i-runtime/](https://capo-sdk.dev/services/sagemaker-a2i-runtime/)

## Installation

```
pip install capo-sagemaker-a2i-runtime
```

## Usage

```python
from capo_sagemaker_a2i_runtime import AsyncSageMakerA2IRuntimeClient


async def main():
    async with AsyncSageMakerA2IRuntimeClient() as sage_maker_a2_i_runtime:
        # Example: call the delete_human_loop operation
        response = await sage_maker_a2_i_runtime.delete_human_loop()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_sagemaker_a2i_runtime import AsyncSageMakerA2IRuntimeClient


async def main():
    async with AsyncSageMakerA2IRuntimeClient() as sage_maker_a2_i_runtime:
        # Example: paginate over list_human_loops
        async for item in sage_maker_a2_i_runtime.iter_list_human_loops():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_sagemaker_a2i_runtime import AsyncSageMakerA2IRuntimeClient
from capo_sagemaker_a2i_runtime.error import InternalServerException


async def main():
    async with AsyncSageMakerA2IRuntimeClient() as sage_maker_a2_i_runtime:
        try:
            await sage_maker_a2_i_runtime.delete_human_loop()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_sagemaker_a2i_runtime import AsyncSageMakerA2IRuntimeClient


async def main():
    async with AsyncSageMakerA2IRuntimeClient() as sage_maker_a2_i_runtime:
        # Default: 3 attempts for every operation
        response = await sage_maker_a2_i_runtime.delete_human_loop()

        # Override per operation
        response = await sage_maker_a2_i_runtime.delete_human_loop(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await sage_maker_a2_i_runtime.delete_human_loop(config_overrides={"retry_max_attempts": 1})
```
