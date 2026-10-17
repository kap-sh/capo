# capo-health: typed, async Python SDK for AWS Health

`capo-health` is a typed Python SDK for AWS Health. It has an async client, `AsyncHealthClient`, for asyncio and trio, and a sync client, `HealthClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/health/](https://capo-sdk.dev/services/health/)

## Installation

```
pip install capo-health
```

## Usage

```python
from capo_health import AsyncHealthClient


async def main():
    async with AsyncHealthClient() as health:
        # Example: call the describe_affected_accounts_for_organization operation
        response = await health.describe_affected_accounts_for_organization()
        print(response["affected_accounts"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_health import AsyncHealthClient


async def main():
    async with AsyncHealthClient() as health:
        # Example: paginate over describe_affected_accounts_for_organization
        async for item in health.iter_describe_affected_accounts_for_organization():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_health import AsyncHealthClient
from capo_health.error import InvalidPaginationToken


async def main():
    async with AsyncHealthClient() as health:
        try:
            await health.describe_affected_accounts_for_organization()
        except InvalidPaginationToken as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_health import AsyncHealthClient


async def main():
    async with AsyncHealthClient() as health:
        # Default: 3 attempts for every operation
        response = await health.describe_affected_accounts_for_organization()

        # Override per operation
        response = await health.describe_affected_accounts_for_organization(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await health.describe_affected_accounts_for_organization(config_overrides={"retry_max_attempts": 1})
```
