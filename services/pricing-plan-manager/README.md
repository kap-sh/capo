# Getting Started

## Installation

```
pip install capo-pricing-plan-manager
```

## Usage

```python
from capo_pricing_plan_manager import AsyncPricingPlanManagerClient


async def main():
    async with AsyncPricingPlanManagerClient() as pricing_plan_manager:
        # Example: call the approve_paid_subscription operation
        response = await pricing_plan_manager.approve_paid_subscription()
        print(response["subscription"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_pricing_plan_manager import AsyncPricingPlanManagerClient


async def main():
    async with AsyncPricingPlanManagerClient() as pricing_plan_manager:
        # Example: paginate over list_subscriptions
        async for item in pricing_plan_manager.iter_list_subscriptions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_pricing_plan_manager import AsyncPricingPlanManagerClient
from capo_pricing_plan_manager.error import AccessDeniedException


async def main():
    async with AsyncPricingPlanManagerClient() as pricing_plan_manager:
        try:
            await pricing_plan_manager.approve_paid_subscription()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_pricing_plan_manager import AsyncPricingPlanManagerClient


async def main():
    async with AsyncPricingPlanManagerClient() as pricing_plan_manager:
        # Default: 3 attempts for every operation
        response = await pricing_plan_manager.approve_paid_subscription()

        # Override per operation
        response = await pricing_plan_manager.approve_paid_subscription(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await pricing_plan_manager.approve_paid_subscription(config_overrides={"retry_max_attempts": 1})
```
