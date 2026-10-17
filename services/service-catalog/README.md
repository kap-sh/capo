# capo-service-catalog: typed, async Python SDK for AWS Service Catalog

`capo-service-catalog` is a typed Python SDK for AWS Service Catalog. It has an async client, `AsyncServiceCatalogClient`, for asyncio and trio, and a sync client, `ServiceCatalogClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/service-catalog/](https://capo-sdk.dev/services/service-catalog/)

## Installation

```
pip install capo-service-catalog
```

## Usage

```python
from capo_service_catalog import AsyncServiceCatalogClient


async def main():
    async with AsyncServiceCatalogClient() as service_catalog:
        # Example: call the accept_portfolio_share operation
        response = await service_catalog.accept_portfolio_share()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_service_catalog import AsyncServiceCatalogClient


async def main():
    async with AsyncServiceCatalogClient() as service_catalog:
        # Example: paginate over describe_portfolio_shares
        async for item in service_catalog.iter_describe_portfolio_shares():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_service_catalog import AsyncServiceCatalogClient
from capo_service_catalog.error import InvalidParametersException


async def main():
    async with AsyncServiceCatalogClient() as service_catalog:
        try:
            await service_catalog.accept_portfolio_share()
        except InvalidParametersException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_service_catalog import AsyncServiceCatalogClient


async def main():
    async with AsyncServiceCatalogClient() as service_catalog:
        # Default: 3 attempts for every operation
        response = await service_catalog.accept_portfolio_share()

        # Override per operation
        response = await service_catalog.accept_portfolio_share(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await service_catalog.accept_portfolio_share(config_overrides={"retry_max_attempts": 1})
```
