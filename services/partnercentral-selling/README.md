# capo-partnercentral-selling: typed, async Python SDK for AWS Partnercentral Selling

`capo-partnercentral-selling` is a typed Python SDK for AWS Partnercentral Selling. It has an async client, `AsyncPartnerCentralSellingClient`, for asyncio and trio, and a sync client, `PartnerCentralSellingClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/partnercentral-selling/](https://capo-sdk.dev/services/partnercentral-selling/)

## Installation

```
pip install capo-partnercentral-selling
```

## Usage

```python
from capo_partnercentral_selling import AsyncPartnerCentralSellingClient


async def main():
    async with AsyncPartnerCentralSellingClient() as partner_central_selling:
        # Example: call the create_engagement_context operation
        response = await partner_central_selling.create_engagement_context()
        print(response["engagement_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_partnercentral_selling import AsyncPartnerCentralSellingClient


async def main():
    async with AsyncPartnerCentralSellingClient() as partner_central_selling:
        # Example: paginate over list_engagements
        async for item in partner_central_selling.iter_list_engagements():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_partnercentral_selling import AsyncPartnerCentralSellingClient
from capo_partnercentral_selling.error import AccessDeniedException


async def main():
    async with AsyncPartnerCentralSellingClient() as partner_central_selling:
        try:
            await partner_central_selling.create_engagement_context()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_partnercentral_selling import AsyncPartnerCentralSellingClient


async def main():
    async with AsyncPartnerCentralSellingClient() as partner_central_selling:
        # Default: 3 attempts for every operation
        response = await partner_central_selling.create_engagement_context()

        # Override per operation
        response = await partner_central_selling.create_engagement_context(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await partner_central_selling.create_engagement_context(config_overrides={"retry_max_attempts": 1})
```
