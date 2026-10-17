# capo-odb: typed, async Python SDK for AWS ODB

`capo-odb` is a typed Python SDK for AWS ODB. It has an async client, `AsyncodbClient`, for asyncio and trio, and a sync client, `odbClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/odb/](https://capo-sdk.dev/services/odb/)

## Installation

```
pip install capo-odb
```

## Usage

```python
from capo_odb import AsyncodbClient


async def main():
    async with AsyncodbClient() as odb:
        # Example: call the accept_marketplace_registration operation
        response = await odb.accept_marketplace_registration()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_odb import AsyncodbClient


async def main():
    async with AsyncodbClient() as odb:
        # Example: paginate over list_autonomous_database_character_sets
        async for item in odb.iter_list_autonomous_database_character_sets():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_odb import AsyncodbClient
from capo_odb.error import AccessDeniedException


async def main():
    async with AsyncodbClient() as odb:
        try:
            await odb.accept_marketplace_registration()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_odb import AsyncodbClient


async def main():
    async with AsyncodbClient() as odb:
        # Default: 3 attempts for every operation
        response = await odb.accept_marketplace_registration()

        # Override per operation
        response = await odb.accept_marketplace_registration(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await odb.accept_marketplace_registration(config_overrides={"retry_max_attempts": 1})
```
