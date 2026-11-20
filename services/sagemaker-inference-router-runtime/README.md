# capo-sagemaker-inference-router-runtime: typed, async Python SDK for AWS Sagemaker Inference Router Runtime

`capo-sagemaker-inference-router-runtime` is a typed Python SDK for AWS Sagemaker Inference Router Runtime. It has an async client, `AsyncSageMakerInferenceRouterRuntimeClient`, for asyncio and trio, and a sync client, `SageMakerInferenceRouterRuntimeClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/sagemaker-inference-router-runtime/](https://capo-sdk.dev/services/sagemaker-inference-router-runtime/)

## Installation

```
pip install capo-sagemaker-inference-router-runtime
```

## Usage

```python
from capo_sagemaker_inference_router_runtime import AsyncSageMakerInferenceRouterRuntimeClient


async def main():
    async with AsyncSageMakerInferenceRouterRuntimeClient() as sage_maker_inference_router_runtime:
        # Example: call the invoke_inference_router operation
        response = await sage_maker_inference_router_runtime.invoke_inference_router()
        print(response["body"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_sagemaker_inference_router_runtime import AsyncSageMakerInferenceRouterRuntimeClient
from capo_sagemaker_inference_router_runtime.error import AccessDeniedException


async def main():
    async with AsyncSageMakerInferenceRouterRuntimeClient() as sage_maker_inference_router_runtime:
        try:
            await sage_maker_inference_router_runtime.invoke_inference_router()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

`retry_mode="adaptive"` (or `AWS_RETRY_MODE=adaptive`, or `retry_mode = adaptive` in the AWS profile) also slows the whole client down once the service starts throttling it, then speeds back up as requests succeed. The default is `standard`.

```python
from capo_sagemaker_inference_router_runtime import AsyncSageMakerInferenceRouterRuntimeClient


async def main():
    async with AsyncSageMakerInferenceRouterRuntimeClient() as sage_maker_inference_router_runtime:
        # Default: 3 attempts for every operation
        response = await sage_maker_inference_router_runtime.invoke_inference_router()

        # Override per operation
        response = await sage_maker_inference_router_runtime.invoke_inference_router(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await sage_maker_inference_router_runtime.invoke_inference_router(config_overrides={"retry_max_attempts": 1})
```
