# capo-dataexchange: typed, async Python SDK for AWS Dataexchange

`capo-dataexchange` is a typed Python SDK for AWS Dataexchange. It has an async client, `AsyncDataExchangeClient`, for asyncio and trio, and a sync client, `DataExchangeClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/dataexchange/](https://capo-sdk.dev/services/dataexchange/)

## Installation

```
pip install capo-dataexchange
```

## Usage

```python
from capo_dataexchange import AsyncDataExchangeClient


async def main():
    async with AsyncDataExchangeClient() as data_exchange:
        # Example: call the accept_data_grant operation
        response = await data_exchange.accept_data_grant()
        print(response["name"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_dataexchange import AsyncDataExchangeClient


async def main():
    async with AsyncDataExchangeClient() as data_exchange:
        # Example: paginate over list_data_grants
        async for item in data_exchange.iter_list_data_grants():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_dataexchange import AsyncDataExchangeClient
from capo_dataexchange.error import AccessDeniedException


async def main():
    async with AsyncDataExchangeClient() as data_exchange:
        try:
            await data_exchange.accept_data_grant()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_dataexchange import AsyncDataExchangeClient


async def main():
    async with AsyncDataExchangeClient() as data_exchange:
        # Default: 3 attempts for every operation
        response = await data_exchange.accept_data_grant()

        # Override per operation
        response = await data_exchange.accept_data_grant(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await data_exchange.accept_data_grant(config_overrides={"retry_max_attempts": 1})
```
