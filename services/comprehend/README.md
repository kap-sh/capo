# capo-comprehend: typed, async Python SDK for AWS Comprehend

`capo-comprehend` is a typed Python SDK for AWS Comprehend. It has an async client, `AsyncComprehendClient`, for asyncio and trio, and a sync client, `ComprehendClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/comprehend/](https://capo-sdk.dev/services/comprehend/)

## Installation

```
pip install capo-comprehend
```

## Usage

```python
from capo_comprehend import AsyncComprehendClient


async def main():
    async with AsyncComprehendClient() as comprehend:
        # Example: call the batch_detect_dominant_language operation
        response = await comprehend.batch_detect_dominant_language()
        print(response["result_list"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_comprehend import AsyncComprehendClient


async def main():
    async with AsyncComprehendClient() as comprehend:
        # Example: paginate over list_datasets
        async for item in comprehend.iter_list_datasets():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_comprehend import AsyncComprehendClient
from capo_comprehend.error import BatchSizeLimitExceededException


async def main():
    async with AsyncComprehendClient() as comprehend:
        try:
            await comprehend.batch_detect_dominant_language()
        except BatchSizeLimitExceededException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_comprehend import AsyncComprehendClient


async def main():
    async with AsyncComprehendClient() as comprehend:
        # Default: 3 attempts for every operation
        response = await comprehend.batch_detect_dominant_language()

        # Override per operation
        response = await comprehend.batch_detect_dominant_language(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await comprehend.batch_detect_dominant_language(config_overrides={"retry_max_attempts": 1})
```
