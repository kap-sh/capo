# capo-bcm-pricing-calculator: typed, async Python SDK for AWS BCM Pricing Calculator

`capo-bcm-pricing-calculator` is a typed Python SDK for AWS BCM Pricing Calculator. It has an async client, `AsyncBCMPricingCalculatorClient`, for asyncio and trio, and a sync client, `BCMPricingCalculatorClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/bcm-pricing-calculator/](https://capo-sdk.dev/services/bcm-pricing-calculator/)

## Installation

```
pip install capo-bcm-pricing-calculator
```

## Usage

```python
from capo_bcm_pricing_calculator import AsyncBCMPricingCalculatorClient


async def main():
    async with AsyncBCMPricingCalculatorClient() as bcm_pricing_calculator:
        # Example: call the get_preferences operation
        response = await bcm_pricing_calculator.get_preferences()
        print(response["management_account_rate_type_selections"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_bcm_pricing_calculator import AsyncBCMPricingCalculatorClient


async def main():
    async with AsyncBCMPricingCalculatorClient() as bcm_pricing_calculator:
        # Example: paginate over list_bill_estimates
        async for item in bcm_pricing_calculator.iter_list_bill_estimates():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_bcm_pricing_calculator import AsyncBCMPricingCalculatorClient
from capo_bcm_pricing_calculator.error import AccessDeniedException


async def main():
    async with AsyncBCMPricingCalculatorClient() as bcm_pricing_calculator:
        try:
            await bcm_pricing_calculator.get_preferences()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_bcm_pricing_calculator import AsyncBCMPricingCalculatorClient


async def main():
    async with AsyncBCMPricingCalculatorClient() as bcm_pricing_calculator:
        # Default: 3 attempts for every operation
        response = await bcm_pricing_calculator.get_preferences()

        # Override per operation
        response = await bcm_pricing_calculator.get_preferences(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await bcm_pricing_calculator.get_preferences(config_overrides={"retry_max_attempts": 1})
```
