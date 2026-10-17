# capo-batch: typed, async Python SDK for AWS Batch

`capo-batch` is a typed Python SDK for AWS Batch. It has an async client, `AsyncBatchClient`, for asyncio and trio, and a sync client, `BatchClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/batch/](https://capo-sdk.dev/services/batch/)

## Installation

```
pip install capo-batch
```

## Usage

```python
from capo_batch import AsyncBatchClient


async def main():
    async with AsyncBatchClient() as batch:
        # Example: call the cancel_job operation
        response = await batch.cancel_job()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_batch import AsyncBatchClient


async def main():
    async with AsyncBatchClient() as batch:
        # Example: paginate over describe_compute_environments
        async for item in batch.iter_describe_compute_environments():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_batch import AsyncBatchClient
from capo_batch.error import ClientException


async def main():
    async with AsyncBatchClient() as batch:
        try:
            await batch.cancel_job()
        except ClientException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_batch import AsyncBatchClient


async def main():
    async with AsyncBatchClient() as batch:
        # Default: 3 attempts for every operation
        response = await batch.cancel_job()

        # Override per operation
        response = await batch.cancel_job(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await batch.cancel_job(config_overrides={"retry_max_attempts": 1})
```
