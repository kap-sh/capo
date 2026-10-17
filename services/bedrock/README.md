# capo-bedrock: typed, async Python SDK for AWS Bedrock

`capo-bedrock` is a typed Python SDK for AWS Bedrock. It has an async client, `AsyncBedrockClient`, for asyncio and trio, and a sync client, `BedrockClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/bedrock/](https://capo-sdk.dev/services/bedrock/)

## Installation

```
pip install capo-bedrock
```

## Usage

```python
from capo_bedrock import AsyncBedrockClient


async def main():
    async with AsyncBedrockClient() as bedrock:
        # Example: call the batch_delete_advanced_prompt_optimization_job operation
        response = await bedrock.batch_delete_advanced_prompt_optimization_job()
        print(response["errors"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_bedrock import AsyncBedrockClient


async def main():
    async with AsyncBedrockClient() as bedrock:
        # Example: paginate over list_advanced_prompt_optimization_jobs
        async for item in bedrock.iter_list_advanced_prompt_optimization_jobs():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_bedrock import AsyncBedrockClient
from capo_bedrock.error import AccessDeniedException


async def main():
    async with AsyncBedrockClient() as bedrock:
        try:
            await bedrock.batch_delete_advanced_prompt_optimization_job()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_bedrock import AsyncBedrockClient


async def main():
    async with AsyncBedrockClient() as bedrock:
        # Default: 3 attempts for every operation
        response = await bedrock.batch_delete_advanced_prompt_optimization_job()

        # Override per operation
        response = await bedrock.batch_delete_advanced_prompt_optimization_job(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await bedrock.batch_delete_advanced_prompt_optimization_job(config_overrides={"retry_max_attempts": 1})
```
