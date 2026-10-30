# capo-sagemakertrainingsessionruntime: typed, async Python SDK for AWS Sagemakertrainingsessionruntime

`capo-sagemakertrainingsessionruntime` is a typed Python SDK for AWS Sagemakertrainingsessionruntime. It has an async client, `AsyncSageMakerTrainingSessionRuntimeClient`, for asyncio and trio, and a sync client, `SageMakerTrainingSessionRuntimeClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/sagemakertrainingsessionruntime/](https://capo-sdk.dev/services/sagemakertrainingsessionruntime/)

## Installation

```
pip install capo-sagemakertrainingsessionruntime
```

## Usage

```python
from capo_sagemakertrainingsessionruntime import AsyncSageMakerTrainingSessionRuntimeClient


async def main():
    async with AsyncSageMakerTrainingSessionRuntimeClient() as sage_maker_training_session_runtime:
        # Example: call the execute_sampling_operation operation
        response = await sage_maker_training_session_runtime.execute_sampling_operation()
        print(response["operation_id"])
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from capo_sagemakertrainingsessionruntime import AsyncSageMakerTrainingSessionRuntimeClient


async def main():
    async with AsyncSageMakerTrainingSessionRuntimeClient() as sage_maker_training_session_runtime:
        # Example: call sample_training_session_with_response_stream and read the streaming response
        async with sage_maker_training_session_runtime.sample_training_session_with_response_stream() as response:
            async for chunk in response["body"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_sagemakertrainingsessionruntime import AsyncSageMakerTrainingSessionRuntimeClient
from capo_sagemakertrainingsessionruntime.error import ConflictException


async def main():
    async with AsyncSageMakerTrainingSessionRuntimeClient() as sage_maker_training_session_runtime:
        try:
            await sage_maker_training_session_runtime.execute_sampling_operation()
        except ConflictException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_sagemakertrainingsessionruntime import AsyncSageMakerTrainingSessionRuntimeClient


async def main():
    async with AsyncSageMakerTrainingSessionRuntimeClient() as sage_maker_training_session_runtime:
        # Default: 3 attempts for every operation
        response = await sage_maker_training_session_runtime.execute_sampling_operation()

        # Override per operation
        response = await sage_maker_training_session_runtime.execute_sampling_operation(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await sage_maker_training_session_runtime.execute_sampling_operation(config_overrides={"retry_max_attempts": 1})
```
