# capo-evs: typed, async Python SDK for AWS EVS

`capo-evs` is a typed Python SDK for AWS EVS. It has an async client, `AsyncevsClient`, for asyncio and trio, and a sync client, `evsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/evs/](https://capo-sdk.dev/services/evs/)

## Installation

```
pip install capo-evs
```

## Usage

```python
from capo_evs import AsyncevsClient


async def main():
    async with AsyncevsClient() as evs:
        # Example: call the get_account_settings operation
        response = await evs.get_account_settings()
        print(response["settings"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_evs import AsyncevsClient


async def main():
    async with AsyncevsClient() as evs:
        # Example: paginate over list_environments
        async for item in evs.iter_list_environments():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_evs import AsyncevsClient
from capo_evs.error import InternalServerException


async def main():
    async with AsyncevsClient() as evs:
        try:
            await evs.get_account_settings()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_evs import AsyncevsClient


async def main():
    async with AsyncevsClient() as evs:
        # Default: 3 attempts for every operation
        response = await evs.get_account_settings()

        # Override per operation
        response = await evs.get_account_settings(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await evs.get_account_settings(config_overrides={"retry_max_attempts": 1})
```
