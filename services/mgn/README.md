# capo-mgn: typed, async Python SDK for AWS Mgn

`capo-mgn` is a typed Python SDK for AWS Mgn. It has an async client, `AsyncmgnClient`, for asyncio and trio, and a sync client, `mgnClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/mgn/](https://capo-sdk.dev/services/mgn/)

## Installation

```
pip install capo-mgn
```

## Usage

```python
from capo_mgn import AsyncmgnClient


async def main():
    async with AsyncmgnClient() as mgn:
        # Example: call the initialize_service operation
        response = await mgn.initialize_service()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_mgn import AsyncmgnClient


async def main():
    async with AsyncmgnClient() as mgn:
        # Example: paginate over list_import_file_enrichments
        async for item in mgn.iter_list_import_file_enrichments():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_mgn import AsyncmgnClient
from capo_mgn.error import AccessDeniedException


async def main():
    async with AsyncmgnClient() as mgn:
        try:
            await mgn.initialize_service()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_mgn import AsyncmgnClient


async def main():
    async with AsyncmgnClient() as mgn:
        # Default: 3 attempts for every operation
        response = await mgn.initialize_service()

        # Override per operation
        response = await mgn.initialize_service(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await mgn.initialize_service(config_overrides={"retry_max_attempts": 1})
```
