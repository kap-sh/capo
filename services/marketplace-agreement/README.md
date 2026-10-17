# capo-marketplace-agreement: typed, async Python SDK for AWS Marketplace Agreement

`capo-marketplace-agreement` is a typed Python SDK for AWS Marketplace Agreement. It has an async client, `AsyncMarketplaceAgreementClient`, for asyncio and trio, and a sync client, `MarketplaceAgreementClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/marketplace-agreement/](https://capo-sdk.dev/services/marketplace-agreement/)

## Installation

```
pip install capo-marketplace-agreement
```

## Usage

```python
from capo_marketplace_agreement import AsyncMarketplaceAgreementClient


async def main():
    async with AsyncMarketplaceAgreementClient() as marketplace_agreement:
        # Example: call the accept_agreement_cancellation_request operation
        response = await marketplace_agreement.accept_agreement_cancellation_request()
        print(response["agreement_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_marketplace_agreement import AsyncMarketplaceAgreementClient


async def main():
    async with AsyncMarketplaceAgreementClient() as marketplace_agreement:
        # Example: paginate over get_agreement_entitlements
        async for item in marketplace_agreement.iter_get_agreement_entitlements():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_marketplace_agreement import AsyncMarketplaceAgreementClient
from capo_marketplace_agreement.error import AccessDeniedException


async def main():
    async with AsyncMarketplaceAgreementClient() as marketplace_agreement:
        try:
            await marketplace_agreement.accept_agreement_cancellation_request()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_marketplace_agreement import AsyncMarketplaceAgreementClient


async def main():
    async with AsyncMarketplaceAgreementClient() as marketplace_agreement:
        # Default: 3 attempts for every operation
        response = await marketplace_agreement.accept_agreement_cancellation_request()

        # Override per operation
        response = await marketplace_agreement.accept_agreement_cancellation_request(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await marketplace_agreement.accept_agreement_cancellation_request(config_overrides={"retry_max_attempts": 1})
```
