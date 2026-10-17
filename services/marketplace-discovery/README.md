# capo-marketplace-discovery: typed, async Python SDK for AWS Marketplace Discovery

`capo-marketplace-discovery` is a typed Python SDK for AWS Marketplace Discovery. It has an async client, `AsyncMarketplaceDiscoveryClient`, for asyncio and trio, and a sync client, `MarketplaceDiscoveryClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/marketplace-discovery/](https://capo-sdk.dev/services/marketplace-discovery/)

## Installation

```
pip install capo-marketplace-discovery
```

## Usage

```python
from capo_marketplace_discovery import AsyncMarketplaceDiscoveryClient


async def main():
    async with AsyncMarketplaceDiscoveryClient() as marketplace_discovery:
        # Example: call the get_listing operation
        response = await marketplace_discovery.get_listing()
        print(response["locale"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_marketplace_discovery import AsyncMarketplaceDiscoveryClient


async def main():
    async with AsyncMarketplaceDiscoveryClient() as marketplace_discovery:
        # Example: paginate over get_offer_terms
        async for item in marketplace_discovery.iter_get_offer_terms():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_marketplace_discovery import AsyncMarketplaceDiscoveryClient
from capo_marketplace_discovery.error import AccessDeniedException


async def main():
    async with AsyncMarketplaceDiscoveryClient() as marketplace_discovery:
        try:
            await marketplace_discovery.get_listing()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_marketplace_discovery import AsyncMarketplaceDiscoveryClient


async def main():
    async with AsyncMarketplaceDiscoveryClient() as marketplace_discovery:
        # Default: 3 attempts for every operation
        response = await marketplace_discovery.get_listing()

        # Override per operation
        response = await marketplace_discovery.get_listing(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await marketplace_discovery.get_listing(config_overrides={"retry_max_attempts": 1})
```
