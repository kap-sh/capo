# capo-wellarchitected: typed, async Python SDK for AWS Wellarchitected

`capo-wellarchitected` is a typed Python SDK for AWS Wellarchitected. It has an async client, `AsyncWellArchitectedClient`, for asyncio and trio, and a sync client, `WellArchitectedClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/wellarchitected/](https://capo-sdk.dev/services/wellarchitected/)

## Installation

```
pip install capo-wellarchitected
```

## Usage

```python
from capo_wellarchitected import AsyncWellArchitectedClient


async def main():
    async with AsyncWellArchitectedClient() as well_architected:
        # Example: call the associate_lenses operation
        response = await well_architected.associate_lenses()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_wellarchitected import AsyncWellArchitectedClient


async def main():
    async with AsyncWellArchitectedClient() as well_architected:
        # Example: paginate over get_consolidated_report
        async for item in well_architected.iter_get_consolidated_report():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_wellarchitected import AsyncWellArchitectedClient
from capo_wellarchitected.error import AccessDeniedException


async def main():
    async with AsyncWellArchitectedClient() as well_architected:
        try:
            await well_architected.associate_lenses()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_wellarchitected import AsyncWellArchitectedClient


async def main():
    async with AsyncWellArchitectedClient() as well_architected:
        # Default: 3 attempts for every operation
        response = await well_architected.associate_lenses()

        # Override per operation
        response = await well_architected.associate_lenses(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await well_architected.associate_lenses(config_overrides={"retry_max_attempts": 1})
```
