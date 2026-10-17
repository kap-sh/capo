# capo-marketplace-reporting: typed, async Python SDK for AWS Marketplace Reporting

`capo-marketplace-reporting` is a typed Python SDK for AWS Marketplace Reporting. It has an async client, `AsyncMarketplaceReportingClient`, for asyncio and trio, and a sync client, `MarketplaceReportingClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/marketplace-reporting/](https://capo-sdk.dev/services/marketplace-reporting/)

## Installation

```
pip install capo-marketplace-reporting
```

## Usage

```python
from capo_marketplace_reporting import AsyncMarketplaceReportingClient


async def main():
    async with AsyncMarketplaceReportingClient() as marketplace_reporting:
        # Example: call the get_buyer_dashboard operation
        response = await marketplace_reporting.get_buyer_dashboard()
        print(response["embed_url"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_marketplace_reporting import AsyncMarketplaceReportingClient
from capo_marketplace_reporting.error import AccessDeniedException


async def main():
    async with AsyncMarketplaceReportingClient() as marketplace_reporting:
        try:
            await marketplace_reporting.get_buyer_dashboard()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_marketplace_reporting import AsyncMarketplaceReportingClient


async def main():
    async with AsyncMarketplaceReportingClient() as marketplace_reporting:
        # Default: 3 attempts for every operation
        response = await marketplace_reporting.get_buyer_dashboard()

        # Override per operation
        response = await marketplace_reporting.get_buyer_dashboard(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await marketplace_reporting.get_buyer_dashboard(config_overrides={"retry_max_attempts": 1})
```
