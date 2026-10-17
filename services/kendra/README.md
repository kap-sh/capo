# capo-kendra: typed, async Python SDK for AWS Kendra

`capo-kendra` is a typed Python SDK for AWS Kendra. It has an async client, `AsynckendraClient`, for asyncio and trio, and a sync client, `kendraClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/kendra/](https://capo-sdk.dev/services/kendra/)

## Installation

```
pip install capo-kendra
```

## Usage

```python
from capo_kendra import AsynckendraClient


async def main():
    async with AsynckendraClient() as kendra:
        # Example: call the associate_entities_to_experience operation
        response = await kendra.associate_entities_to_experience()
        print(response["failed_entity_list"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_kendra import AsynckendraClient


async def main():
    async with AsynckendraClient() as kendra:
        # Example: paginate over get_snapshots
        async for item in kendra.iter_get_snapshots():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_kendra import AsynckendraClient
from capo_kendra.error import AccessDeniedException


async def main():
    async with AsynckendraClient() as kendra:
        try:
            await kendra.associate_entities_to_experience()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_kendra import AsynckendraClient


async def main():
    async with AsynckendraClient() as kendra:
        # Default: 3 attempts for every operation
        response = await kendra.associate_entities_to_experience()

        # Override per operation
        response = await kendra.associate_entities_to_experience(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await kendra.associate_entities_to_experience(config_overrides={"retry_max_attempts": 1})
```
