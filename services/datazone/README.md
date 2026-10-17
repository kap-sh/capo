# capo-datazone: typed, async Python SDK for AWS Datazone

`capo-datazone` is a typed Python SDK for AWS Datazone. It has an async client, `AsyncDataZoneClient`, for asyncio and trio, and a sync client, `DataZoneClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/datazone/](https://capo-sdk.dev/services/datazone/)

## Installation

```
pip install capo-datazone
```

## Usage

```python
from capo_datazone import AsyncDataZoneClient


async def main():
    async with AsyncDataZoneClient() as data_zone:
        # Example: call the accept_predictions operation
        response = await data_zone.accept_predictions()
        print(response["domain_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_datazone import AsyncDataZoneClient


async def main():
    async with AsyncDataZoneClient() as data_zone:
        # Example: paginate over list_account_pools
        async for item in data_zone.iter_list_account_pools():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_datazone import AsyncDataZoneClient
from capo_datazone.error import AccessDeniedException


async def main():
    async with AsyncDataZoneClient() as data_zone:
        try:
            await data_zone.accept_predictions()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_datazone import AsyncDataZoneClient


async def main():
    async with AsyncDataZoneClient() as data_zone:
        # Default: 3 attempts for every operation
        response = await data_zone.accept_predictions()

        # Override per operation
        response = await data_zone.accept_predictions(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await data_zone.accept_predictions(config_overrides={"retry_max_attempts": 1})
```
