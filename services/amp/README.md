# capo-amp: typed, async Python SDK for AWS Amp

`capo-amp` is a typed Python SDK for AWS Amp. It has an async client, `AsyncampClient`, for asyncio and trio, and a sync client, `ampClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/amp/](https://capo-sdk.dev/services/amp/)

## Installation

```
pip install capo-amp
```

## Usage

```python
from capo_amp import AsyncampClient


async def main():
    async with AsyncampClient() as amp:
        # Example: call the get_default_scraper_configuration operation
        response = await amp.get_default_scraper_configuration()
        print(response["configuration"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_amp import AsyncampClient


async def main():
    async with AsyncampClient() as amp:
        # Example: paginate over list_scrapers
        async for item in amp.iter_list_scrapers():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_amp import AsyncampClient
from capo_amp.error import AccessDeniedException


async def main():
    async with AsyncampClient() as amp:
        try:
            await amp.get_default_scraper_configuration()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_amp import AsyncampClient


async def main():
    async with AsyncampClient() as amp:
        # Default: 3 attempts for every operation
        response = await amp.get_default_scraper_configuration()

        # Override per operation
        response = await amp.get_default_scraper_configuration(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await amp.get_default_scraper_configuration(config_overrides={"retry_max_attempts": 1})
```
