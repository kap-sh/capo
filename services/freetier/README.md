# capo-freetier: typed, async Python SDK for AWS Freetier

`capo-freetier` is a typed Python SDK for AWS Freetier. It has an async client, `AsyncFreeTierClient`, for asyncio and trio, and a sync client, `FreeTierClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/freetier/](https://capo-sdk.dev/services/freetier/)

## Installation

```
pip install capo-freetier
```

## Usage

```python
from capo_freetier import AsyncFreeTierClient


async def main():
    async with AsyncFreeTierClient() as free_tier:
        # Example: call the get_account_activity operation
        response = await free_tier.get_account_activity()
        print(response["activity_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_freetier import AsyncFreeTierClient


async def main():
    async with AsyncFreeTierClient() as free_tier:
        # Example: paginate over get_free_tier_usage
        async for item in free_tier.iter_get_free_tier_usage():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_freetier import AsyncFreeTierClient
from capo_freetier.error import InternalServerException


async def main():
    async with AsyncFreeTierClient() as free_tier:
        try:
            await free_tier.get_account_activity()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_freetier import AsyncFreeTierClient


async def main():
    async with AsyncFreeTierClient() as free_tier:
        # Default: 3 attempts for every operation
        response = await free_tier.get_account_activity()

        # Override per operation
        response = await free_tier.get_account_activity(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await free_tier.get_account_activity(config_overrides={"retry_max_attempts": 1})
```
