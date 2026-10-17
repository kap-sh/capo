# capo-budgets: typed, async Python SDK for AWS Budgets

`capo-budgets` is a typed Python SDK for AWS Budgets. It has an async client, `AsyncBudgetsClient`, for asyncio and trio, and a sync client, `BudgetsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/budgets/](https://capo-sdk.dev/services/budgets/)

## Installation

```
pip install capo-budgets
```

## Usage

```python
from capo_budgets import AsyncBudgetsClient


async def main():
    async with AsyncBudgetsClient() as budgets:
        # Example: call the create_budget operation
        response = await budgets.create_budget()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_budgets import AsyncBudgetsClient


async def main():
    async with AsyncBudgetsClient() as budgets:
        # Example: paginate over describe_budget_action_histories
        async for item in budgets.iter_describe_budget_action_histories():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_budgets import AsyncBudgetsClient
from capo_budgets.error import AccessDeniedException


async def main():
    async with AsyncBudgetsClient() as budgets:
        try:
            await budgets.create_budget()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_budgets import AsyncBudgetsClient


async def main():
    async with AsyncBudgetsClient() as budgets:
        # Default: 3 attempts for every operation
        response = await budgets.create_budget()

        # Override per operation
        response = await budgets.create_budget(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await budgets.create_budget(config_overrides={"retry_max_attempts": 1})
```
