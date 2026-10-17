# capo-location: typed, async Python SDK for AWS Location

`capo-location` is a typed Python SDK for AWS Location. It has an async client, `AsyncLocationClient`, for asyncio and trio, and a sync client, `LocationClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/location/](https://capo-sdk.dev/services/location/)

## Installation

```
pip install capo-location
```

## Usage

```python
from capo_location import AsyncLocationClient


async def main():
    async with AsyncLocationClient() as location:
        # Example: call the create_key operation
        response = await location.create_key()
        print(response["key"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_location import AsyncLocationClient


async def main():
    async with AsyncLocationClient() as location:
        # Example: paginate over list_keys
        async for item in location.iter_list_keys():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_location import AsyncLocationClient
from capo_location.error import AccessDeniedException


async def main():
    async with AsyncLocationClient() as location:
        try:
            await location.create_key()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_location import AsyncLocationClient


async def main():
    async with AsyncLocationClient() as location:
        # Default: 3 attempts for every operation
        response = await location.create_key()

        # Override per operation
        response = await location.create_key(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await location.create_key(config_overrides={"retry_max_attempts": 1})
```
