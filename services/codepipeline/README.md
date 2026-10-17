# capo-codepipeline: typed, async Python SDK for AWS Codepipeline

`capo-codepipeline` is a typed Python SDK for AWS Codepipeline. It has an async client, `AsyncCodePipelineClient`, for asyncio and trio, and a sync client, `CodePipelineClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/codepipeline/](https://capo-sdk.dev/services/codepipeline/)

## Installation

```
pip install capo-codepipeline
```

## Usage

```python
from capo_codepipeline import AsyncCodePipelineClient


async def main():
    async with AsyncCodePipelineClient() as code_pipeline:
        # Example: call the acknowledge_job operation
        response = await code_pipeline.acknowledge_job()
        print(response["status"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_codepipeline import AsyncCodePipelineClient


async def main():
    async with AsyncCodePipelineClient() as code_pipeline:
        # Example: paginate over list_action_executions
        async for item in code_pipeline.iter_list_action_executions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_codepipeline import AsyncCodePipelineClient
from capo_codepipeline.error import InvalidNonceException


async def main():
    async with AsyncCodePipelineClient() as code_pipeline:
        try:
            await code_pipeline.acknowledge_job()
        except InvalidNonceException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_codepipeline import AsyncCodePipelineClient


async def main():
    async with AsyncCodePipelineClient() as code_pipeline:
        # Default: 3 attempts for every operation
        response = await code_pipeline.acknowledge_job()

        # Override per operation
        response = await code_pipeline.acknowledge_job(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await code_pipeline.acknowledge_job(config_overrides={"retry_max_attempts": 1})
```
