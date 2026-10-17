# capo-mpa: typed, async Python SDK for AWS MPA

`capo-mpa` is a typed Python SDK for AWS MPA. It has an async client, `AsyncMPAClient`, for asyncio and trio, and a sync client, `MPAClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/mpa/](https://capo-sdk.dev/services/mpa/)

## Installation

```
pip install capo-mpa
```

## Usage

```python
from capo_mpa import AsyncMPAClient


async def main():
    async with AsyncMPAClient() as mpa:
        # Example: call the get_policy_version operation
        response = await mpa.get_policy_version()
        print(response["policy_version"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_mpa import AsyncMPAClient


async def main():
    async with AsyncMPAClient() as mpa:
        # Example: paginate over list_policies
        async for item in mpa.iter_list_policies():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_mpa import AsyncMPAClient
from capo_mpa.error import AccessDeniedException


async def main():
    async with AsyncMPAClient() as mpa:
        try:
            await mpa.get_policy_version()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_mpa import AsyncMPAClient


async def main():
    async with AsyncMPAClient() as mpa:
        # Default: 3 attempts for every operation
        response = await mpa.get_policy_version()

        # Override per operation
        response = await mpa.get_policy_version(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await mpa.get_policy_version(config_overrides={"retry_max_attempts": 1})
```
