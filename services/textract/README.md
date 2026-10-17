# capo-textract: typed, async Python SDK for AWS Textract

`capo-textract` is a typed Python SDK for AWS Textract. It has an async client, `AsyncTextractClient`, for asyncio and trio, and a sync client, `TextractClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/textract/](https://capo-sdk.dev/services/textract/)

## Installation

```
pip install capo-textract
```

## Usage

```python
from capo_textract import AsyncTextractClient


async def main():
    async with AsyncTextractClient() as textract:
        # Example: call the analyze_document operation
        response = await textract.analyze_document()
        print(response["document_metadata"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_textract import AsyncTextractClient


async def main():
    async with AsyncTextractClient() as textract:
        # Example: paginate over list_adapters
        async for item in textract.iter_list_adapters():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_textract import AsyncTextractClient
from capo_textract.error import AccessDeniedException


async def main():
    async with AsyncTextractClient() as textract:
        try:
            await textract.analyze_document()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_textract import AsyncTextractClient


async def main():
    async with AsyncTextractClient() as textract:
        # Default: 3 attempts for every operation
        response = await textract.analyze_document()

        # Override per operation
        response = await textract.analyze_document(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await textract.analyze_document(config_overrides={"retry_max_attempts": 1})
```
