# capo-sagemaker-runtime: typed, async Python SDK for AWS Sagemaker Runtime

`capo-sagemaker-runtime` is a typed Python SDK for AWS Sagemaker Runtime. It has an async client, `AsyncSageMakerRuntimeClient`, for asyncio and trio, and a sync client, `SageMakerRuntimeClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/sagemaker-runtime/](https://capo-sdk.dev/services/sagemaker-runtime/)

## Installation

```
pip install capo-sagemaker-runtime
```

## Usage

```python
from capo_sagemaker_runtime import AsyncSageMakerRuntimeClient


async def main():
    async with AsyncSageMakerRuntimeClient() as sage_maker_runtime:
        # Example: call the invoke_endpoint operation
        response = await sage_maker_runtime.invoke_endpoint()
        print(response["body"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_sagemaker_runtime import AsyncSageMakerRuntimeClient
from capo_sagemaker_runtime.error import InternalDependencyException


async def main():
    async with AsyncSageMakerRuntimeClient() as sage_maker_runtime:
        try:
            await sage_maker_runtime.invoke_endpoint()
        except InternalDependencyException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_sagemaker_runtime import AsyncSageMakerRuntimeClient


async def main():
    async with AsyncSageMakerRuntimeClient() as sage_maker_runtime:
        # Default: 3 attempts for every operation
        response = await sage_maker_runtime.invoke_endpoint()

        # Override per operation
        response = await sage_maker_runtime.invoke_endpoint(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await sage_maker_runtime.invoke_endpoint(config_overrides={"retry_max_attempts": 1})
```
