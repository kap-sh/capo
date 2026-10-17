# capo-shield: typed, async Python SDK for AWS Shield

`capo-shield` is a typed Python SDK for AWS Shield. It has an async client, `AsyncShieldClient`, for asyncio and trio, and a sync client, `ShieldClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/shield/](https://capo-sdk.dev/services/shield/)

## Installation

```
pip install capo-shield
```

## Usage

```python
from capo_shield import AsyncShieldClient


async def main():
    async with AsyncShieldClient() as shield:
        # Example: call the associate_drt_log_bucket operation
        response = await shield.associate_drt_log_bucket()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_shield import AsyncShieldClient


async def main():
    async with AsyncShieldClient() as shield:
        # Example: paginate over list_attacks
        async for item in shield.iter_list_attacks():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_shield import AsyncShieldClient
from capo_shield.error import AccessDeniedForDependencyException


async def main():
    async with AsyncShieldClient() as shield:
        try:
            await shield.associate_drt_log_bucket()
        except AccessDeniedForDependencyException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_shield import AsyncShieldClient


async def main():
    async with AsyncShieldClient() as shield:
        # Default: 3 attempts for every operation
        response = await shield.associate_drt_log_bucket()

        # Override per operation
        response = await shield.associate_drt_log_bucket(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await shield.associate_drt_log_bucket(config_overrides={"retry_max_attempts": 1})
```
