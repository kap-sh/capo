# capo-marketplace-catalog: typed, async Python SDK for AWS Marketplace Catalog

`capo-marketplace-catalog` is a typed Python SDK for AWS Marketplace Catalog. It has an async client, `AsyncMarketplaceCatalogClient`, for asyncio and trio, and a sync client, `MarketplaceCatalogClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/marketplace-catalog/](https://capo-sdk.dev/services/marketplace-catalog/)

## Installation

```
pip install capo-marketplace-catalog
```

## Usage

```python
from capo_marketplace_catalog import AsyncMarketplaceCatalogClient


async def main():
    async with AsyncMarketplaceCatalogClient() as marketplace_catalog:
        # Example: call the batch_describe_entities operation
        response = await marketplace_catalog.batch_describe_entities()
        print(response["entity_details"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_marketplace_catalog import AsyncMarketplaceCatalogClient


async def main():
    async with AsyncMarketplaceCatalogClient() as marketplace_catalog:
        # Example: paginate over describe_assessment
        async for item in marketplace_catalog.iter_describe_assessment():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_marketplace_catalog import AsyncMarketplaceCatalogClient
from capo_marketplace_catalog.error import AccessDeniedException


async def main():
    async with AsyncMarketplaceCatalogClient() as marketplace_catalog:
        try:
            await marketplace_catalog.batch_describe_entities()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_marketplace_catalog import AsyncMarketplaceCatalogClient


async def main():
    async with AsyncMarketplaceCatalogClient() as marketplace_catalog:
        # Default: 3 attempts for every operation
        response = await marketplace_catalog.batch_describe_entities()

        # Override per operation
        response = await marketplace_catalog.batch_describe_entities(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await marketplace_catalog.batch_describe_entities(config_overrides={"retry_max_attempts": 1})
```
