# capo-billing: typed, async Python SDK for AWS Billing

`capo-billing` is a typed Python SDK for AWS Billing. It has an async client, `AsyncBillingClient`, for asyncio and trio, and a sync client, `BillingClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/billing/](https://capo-sdk.dev/services/billing/)

## Installation

```
pip install capo-billing
```

## Usage

```python
from capo_billing import AsyncBillingClient


async def main():
    async with AsyncBillingClient() as billing:
        # Example: call the associate_source_views operation
        response = await billing.associate_source_views()
        print(response["arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_billing import AsyncBillingClient


async def main():
    async with AsyncBillingClient() as billing:
        # Example: paginate over get_credit_allocation_history
        async for item in billing.iter_get_credit_allocation_history():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_billing import AsyncBillingClient
from capo_billing.error import AccessDeniedException


async def main():
    async with AsyncBillingClient() as billing:
        try:
            await billing.associate_source_views()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_billing import AsyncBillingClient


async def main():
    async with AsyncBillingClient() as billing:
        # Default: 3 attempts for every operation
        response = await billing.associate_source_views()

        # Override per operation
        response = await billing.associate_source_views(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await billing.associate_source_views(config_overrides={"retry_max_attempts": 1})
```
