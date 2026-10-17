# capo-marketplace-metering: typed, async Python SDK for AWS Marketplace Metering

`capo-marketplace-metering` is a typed Python SDK for AWS Marketplace Metering. It has an async client, `AsyncMarketplaceMeteringClient`, for asyncio and trio, and a sync client, `MarketplaceMeteringClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/marketplace-metering/](https://capo-sdk.dev/services/marketplace-metering/)

## Installation

```
pip install capo-marketplace-metering
```

## Usage

```python
from capo_marketplace_metering import AsyncMarketplaceMeteringClient


async def main():
    async with AsyncMarketplaceMeteringClient() as marketplace_metering:
        # Example: call the batch_meter_usage operation
        response = await marketplace_metering.batch_meter_usage()
        print(response["results"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_marketplace_metering import AsyncMarketplaceMeteringClient
from capo_marketplace_metering.error import DisabledApiException


async def main():
    async with AsyncMarketplaceMeteringClient() as marketplace_metering:
        try:
            await marketplace_metering.batch_meter_usage()
        except DisabledApiException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_marketplace_metering import AsyncMarketplaceMeteringClient


async def main():
    async with AsyncMarketplaceMeteringClient() as marketplace_metering:
        # Default: 3 attempts for every operation
        response = await marketplace_metering.batch_meter_usage()

        # Override per operation
        response = await marketplace_metering.batch_meter_usage(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await marketplace_metering.batch_meter_usage(config_overrides={"retry_max_attempts": 1})
```
