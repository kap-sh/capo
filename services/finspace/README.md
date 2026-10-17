# capo-finspace: typed, async Python SDK for AWS Finspace

`capo-finspace` is a typed Python SDK for AWS Finspace. It has an async client, `AsyncfinspaceClient`, for asyncio and trio, and a sync client, `finspaceClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/finspace/](https://capo-sdk.dev/services/finspace/)

## Installation

```
pip install capo-finspace
```

## Usage

```python
from capo_finspace import AsyncfinspaceClient


async def main():
    async with AsyncfinspaceClient() as finspace:
        # Example: call the create_environment operation
        response = await finspace.create_environment()
        print(response["environment_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_finspace import AsyncfinspaceClient


async def main():
    async with AsyncfinspaceClient() as finspace:
        # Example: paginate over list_kx_changesets
        async for item in finspace.iter_list_kx_changesets():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_finspace import AsyncfinspaceClient
from capo_finspace.error import AccessDeniedException


async def main():
    async with AsyncfinspaceClient() as finspace:
        try:
            await finspace.create_environment()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_finspace import AsyncfinspaceClient


async def main():
    async with AsyncfinspaceClient() as finspace:
        # Default: 3 attempts for every operation
        response = await finspace.create_environment()

        # Override per operation
        response = await finspace.create_environment(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await finspace.create_environment(config_overrides={"retry_max_attempts": 1})
```
