# capo-partnercentral-benefits: typed, async Python SDK for AWS Partnercentral Benefits

`capo-partnercentral-benefits` is a typed Python SDK for AWS Partnercentral Benefits. It has an async client, `AsyncPartnerCentralBenefitsClient`, for asyncio and trio, and a sync client, `PartnerCentralBenefitsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/partnercentral-benefits/](https://capo-sdk.dev/services/partnercentral-benefits/)

## Installation

```
pip install capo-partnercentral-benefits
```

## Usage

```python
from capo_partnercentral_benefits import AsyncPartnerCentralBenefitsClient


async def main():
    async with AsyncPartnerCentralBenefitsClient() as partner_central_benefits:
        # Example: call the amend_benefit_application operation
        response = await partner_central_benefits.amend_benefit_application()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_partnercentral_benefits import AsyncPartnerCentralBenefitsClient


async def main():
    async with AsyncPartnerCentralBenefitsClient() as partner_central_benefits:
        # Example: paginate over list_benefit_allocations
        async for item in partner_central_benefits.iter_list_benefit_allocations():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_partnercentral_benefits import AsyncPartnerCentralBenefitsClient
from capo_partnercentral_benefits.error import AccessDeniedException


async def main():
    async with AsyncPartnerCentralBenefitsClient() as partner_central_benefits:
        try:
            await partner_central_benefits.amend_benefit_application()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_partnercentral_benefits import AsyncPartnerCentralBenefitsClient


async def main():
    async with AsyncPartnerCentralBenefitsClient() as partner_central_benefits:
        # Default: 3 attempts for every operation
        response = await partner_central_benefits.amend_benefit_application()

        # Override per operation
        response = await partner_central_benefits.amend_benefit_application(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await partner_central_benefits.amend_benefit_application(config_overrides={"retry_max_attempts": 1})
```
