# capo-neptunedata: typed, async Python SDK for AWS Neptunedata

`capo-neptunedata` is a typed Python SDK for AWS Neptunedata. It has an async client, `AsyncneptunedataClient`, for asyncio and trio, and a sync client, `neptunedataClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/neptunedata/](https://capo-sdk.dev/services/neptunedata/)

## Installation

```
pip install capo-neptunedata
```

## Usage

```python
from capo_neptunedata import AsyncneptunedataClient


async def main():
    async with AsyncneptunedataClient() as neptunedata:
        # Example: call the cancel_gremlin_query operation
        response = await neptunedata.cancel_gremlin_query()
        print(response["status"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_neptunedata import AsyncneptunedataClient
from capo_neptunedata.error import BadRequestException


async def main():
    async with AsyncneptunedataClient() as neptunedata:
        try:
            await neptunedata.cancel_gremlin_query()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_neptunedata import AsyncneptunedataClient


async def main():
    async with AsyncneptunedataClient() as neptunedata:
        # Default: 3 attempts for every operation
        response = await neptunedata.cancel_gremlin_query()

        # Override per operation
        response = await neptunedata.cancel_gremlin_query(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await neptunedata.cancel_gremlin_query(config_overrides={"retry_max_attempts": 1})
```
