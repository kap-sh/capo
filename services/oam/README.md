# capo-oam: typed, async Python SDK for AWS OAM

`capo-oam` is a typed Python SDK for AWS OAM. It has an async client, `AsyncOAMClient`, for asyncio and trio, and a sync client, `OAMClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/oam/](https://capo-sdk.dev/services/oam/)

## Installation

```
pip install capo-oam
```

## Usage

```python
from capo_oam import AsyncOAMClient


async def main():
    async with AsyncOAMClient() as oam:
        # Example: call the create_link operation
        response = await oam.create_link()
        print(response["arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_oam import AsyncOAMClient


async def main():
    async with AsyncOAMClient() as oam:
        # Example: paginate over list_attached_links
        async for item in oam.iter_list_attached_links():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_oam import AsyncOAMClient
from capo_oam.error import ConflictException


async def main():
    async with AsyncOAMClient() as oam:
        try:
            await oam.create_link()
        except ConflictException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_oam import AsyncOAMClient


async def main():
    async with AsyncOAMClient() as oam:
        # Default: 3 attempts for every operation
        response = await oam.create_link()

        # Override per operation
        response = await oam.create_link(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await oam.create_link(config_overrides={"retry_max_attempts": 1})
```
