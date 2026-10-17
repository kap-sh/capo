# capo-chime: typed, async Python SDK for AWS Chime

`capo-chime` is a typed Python SDK for AWS Chime. It has an async client, `AsyncChimeClient`, for asyncio and trio, and a sync client, `ChimeClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/chime/](https://capo-sdk.dev/services/chime/)

## Installation

```
pip install capo-chime
```

## Usage

```python
from capo_chime import AsyncChimeClient


async def main():
    async with AsyncChimeClient() as chime:
        # Example: call the associate_phone_number_with_user operation
        response = await chime.associate_phone_number_with_user()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_chime import AsyncChimeClient


async def main():
    async with AsyncChimeClient() as chime:
        # Example: paginate over list_accounts
        async for item in chime.iter_list_accounts():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_chime import AsyncChimeClient
from capo_chime.error import AccessDeniedException


async def main():
    async with AsyncChimeClient() as chime:
        try:
            await chime.associate_phone_number_with_user()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_chime import AsyncChimeClient


async def main():
    async with AsyncChimeClient() as chime:
        # Default: 3 attempts for every operation
        response = await chime.associate_phone_number_with_user()

        # Override per operation
        response = await chime.associate_phone_number_with_user(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await chime.associate_phone_number_with_user(config_overrides={"retry_max_attempts": 1})
```
