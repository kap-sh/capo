# capo-codecatalyst: typed, async Python SDK for AWS Codecatalyst

`capo-codecatalyst` is a typed Python SDK for AWS Codecatalyst. It has an async client, `AsyncCodeCatalystClient`, for asyncio and trio, and a sync client, `CodeCatalystClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/codecatalyst/](https://capo-sdk.dev/services/codecatalyst/)

## Installation

```
pip install capo-codecatalyst
```

## Usage

```python
from capo_codecatalyst import AsyncCodeCatalystClient


async def main():
    async with AsyncCodeCatalystClient() as code_catalyst:
        # Example: call the get_user_details operation
        response = await code_catalyst.get_user_details()
        print(response["user_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_codecatalyst import AsyncCodeCatalystClient


async def main():
    async with AsyncCodeCatalystClient() as code_catalyst:
        # Example: paginate over list_access_tokens
        async for item in code_catalyst.iter_list_access_tokens():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_codecatalyst import AsyncCodeCatalystClient
from capo_codecatalyst.error import AccessDeniedException


async def main():
    async with AsyncCodeCatalystClient() as code_catalyst:
        try:
            await code_catalyst.get_user_details()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_codecatalyst import AsyncCodeCatalystClient


async def main():
    async with AsyncCodeCatalystClient() as code_catalyst:
        # Default: 3 attempts for every operation
        response = await code_catalyst.get_user_details()

        # Override per operation
        response = await code_catalyst.get_user_details(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await code_catalyst.get_user_details(config_overrides={"retry_max_attempts": 1})
```
