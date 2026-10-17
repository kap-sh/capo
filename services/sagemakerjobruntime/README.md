# capo-sagemakerjobruntime: typed, async Python SDK for AWS Sagemakerjobruntime

`capo-sagemakerjobruntime` is a typed Python SDK for AWS Sagemakerjobruntime. It has an async client, `AsyncSagemakerJobRuntimeClient`, for asyncio and trio, and a sync client, `SagemakerJobRuntimeClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/sagemakerjobruntime/](https://capo-sdk.dev/services/sagemakerjobruntime/)

## Installation

```
pip install capo-sagemakerjobruntime
```

## Usage

```python
from capo_sagemakerjobruntime import AsyncSagemakerJobRuntimeClient


async def main():
    async with AsyncSagemakerJobRuntimeClient() as sagemaker_job_runtime:
        # Example: call the complete_rollout operation
        response = await sagemaker_job_runtime.complete_rollout()
        print(response)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from capo_sagemakerjobruntime import AsyncSagemakerJobRuntimeClient


async def main():
    async with AsyncSagemakerJobRuntimeClient() as sagemaker_job_runtime:
        # Example: call sample_with_response_stream and read the streaming response
        async with sagemaker_job_runtime.sample_with_response_stream() as response:
            async for chunk in response["body"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_sagemakerjobruntime import AsyncSagemakerJobRuntimeClient
from capo_sagemakerjobruntime.error import AccessDeniedException


async def main():
    async with AsyncSagemakerJobRuntimeClient() as sagemaker_job_runtime:
        try:
            await sagemaker_job_runtime.complete_rollout()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_sagemakerjobruntime import AsyncSagemakerJobRuntimeClient


async def main():
    async with AsyncSagemakerJobRuntimeClient() as sagemaker_job_runtime:
        # Default: 3 attempts for every operation
        response = await sagemaker_job_runtime.complete_rollout()

        # Override per operation
        response = await sagemaker_job_runtime.complete_rollout(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await sagemaker_job_runtime.complete_rollout(config_overrides={"retry_max_attempts": 1})
```
