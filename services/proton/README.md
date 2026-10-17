# capo-proton: typed, async Python SDK for AWS Proton

`capo-proton` is a typed Python SDK for AWS Proton. It has an async client, `AsyncProtonClient`, for asyncio and trio, and a sync client, `ProtonClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/proton/](https://capo-sdk.dev/services/proton/)

## Installation

```
pip install capo-proton
```

## Usage

```python
from capo_proton import AsyncProtonClient


async def main():
    async with AsyncProtonClient() as proton:
        # Example: call the cancel_component_deployment operation
        response = await proton.cancel_component_deployment()
        print(response["component"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_proton import AsyncProtonClient


async def main():
    async with AsyncProtonClient() as proton:
        # Example: paginate over list_repository_sync_definitions
        async for item in proton.iter_list_repository_sync_definitions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_proton import AsyncProtonClient
from capo_proton.error import AccessDeniedException


async def main():
    async with AsyncProtonClient() as proton:
        try:
            await proton.cancel_component_deployment()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_proton import AsyncProtonClient


async def main():
    async with AsyncProtonClient() as proton:
        # Default: 3 attempts for every operation
        response = await proton.cancel_component_deployment()

        # Override per operation
        response = await proton.cancel_component_deployment(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await proton.cancel_component_deployment(config_overrides={"retry_max_attempts": 1})
```
