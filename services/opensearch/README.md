# capo-opensearch: typed, async Python SDK for AWS Opensearch

`capo-opensearch` is a typed Python SDK for AWS Opensearch. It has an async client, `AsyncOpenSearchClient`, for asyncio and trio, and a sync client, `OpenSearchClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/opensearch/](https://capo-sdk.dev/services/opensearch/)

## Installation

```
pip install capo-opensearch
```

## Usage

```python
from capo_opensearch import AsyncOpenSearchClient


async def main():
    async with AsyncOpenSearchClient() as open_search:
        # Example: call the accept_inbound_connection operation
        response = await open_search.accept_inbound_connection()
        print(response["connection"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_opensearch import AsyncOpenSearchClient


async def main():
    async with AsyncOpenSearchClient() as open_search:
        # Example: paginate over describe_domain_auto_tunes
        async for item in open_search.iter_describe_domain_auto_tunes():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_opensearch import AsyncOpenSearchClient
from capo_opensearch.error import DisabledOperationException


async def main():
    async with AsyncOpenSearchClient() as open_search:
        try:
            await open_search.accept_inbound_connection()
        except DisabledOperationException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_opensearch import AsyncOpenSearchClient


async def main():
    async with AsyncOpenSearchClient() as open_search:
        # Default: 3 attempts for every operation
        response = await open_search.accept_inbound_connection()

        # Override per operation
        response = await open_search.accept_inbound_connection(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await open_search.accept_inbound_connection(config_overrides={"retry_max_attempts": 1})
```
