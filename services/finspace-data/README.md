# capo-finspace-data: typed, async Python SDK for AWS Finspace Data

`capo-finspace-data` is a typed Python SDK for AWS Finspace Data. It has an async client, `AsyncfinspacedataClient`, for asyncio and trio, and a sync client, `finspacedataClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/finspace-data/](https://capo-sdk.dev/services/finspace-data/)

## Installation

```
pip install capo-finspace-data
```

## Usage

```python
from capo_finspace_data import AsyncfinspacedataClient


async def main():
    async with AsyncfinspacedataClient() as finspacedata:
        # Example: call the associate_user_to_permission_group operation
        response = await finspacedata.associate_user_to_permission_group()
        print(response["status_code"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_finspace_data import AsyncfinspacedataClient


async def main():
    async with AsyncfinspacedataClient() as finspacedata:
        # Example: paginate over list_changesets
        async for item in finspacedata.iter_list_changesets():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_finspace_data import AsyncfinspacedataClient
from capo_finspace_data.error import AccessDeniedException


async def main():
    async with AsyncfinspacedataClient() as finspacedata:
        try:
            await finspacedata.associate_user_to_permission_group()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_finspace_data import AsyncfinspacedataClient


async def main():
    async with AsyncfinspacedataClient() as finspacedata:
        # Default: 3 attempts for every operation
        response = await finspacedata.associate_user_to_permission_group()

        # Override per operation
        response = await finspacedata.associate_user_to_permission_group(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await finspacedata.associate_user_to_permission_group(config_overrides={"retry_max_attempts": 1})
```
