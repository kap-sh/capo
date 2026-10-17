# capo-compute-optimizer-automation: typed, async Python SDK for AWS Compute Optimizer Automation

`capo-compute-optimizer-automation` is a typed Python SDK for AWS Compute Optimizer Automation. It has an async client, `AsyncComputeOptimizerAutomationClient`, for asyncio and trio, and a sync client, `ComputeOptimizerAutomationClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/compute-optimizer-automation/](https://capo-sdk.dev/services/compute-optimizer-automation/)

## Installation

```
pip install capo-compute-optimizer-automation
```

## Usage

```python
from capo_compute_optimizer_automation import AsyncComputeOptimizerAutomationClient


async def main():
    async with AsyncComputeOptimizerAutomationClient() as compute_optimizer_automation:
        # Example: call the associate_accounts operation
        response = await compute_optimizer_automation.associate_accounts()
        print(response["account_ids"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_compute_optimizer_automation import AsyncComputeOptimizerAutomationClient


async def main():
    async with AsyncComputeOptimizerAutomationClient() as compute_optimizer_automation:
        # Example: paginate over list_accounts
        async for item in compute_optimizer_automation.iter_list_accounts():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_compute_optimizer_automation import AsyncComputeOptimizerAutomationClient
from capo_compute_optimizer_automation.error import AccessDeniedException


async def main():
    async with AsyncComputeOptimizerAutomationClient() as compute_optimizer_automation:
        try:
            await compute_optimizer_automation.associate_accounts()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_compute_optimizer_automation import AsyncComputeOptimizerAutomationClient


async def main():
    async with AsyncComputeOptimizerAutomationClient() as compute_optimizer_automation:
        # Default: 3 attempts for every operation
        response = await compute_optimizer_automation.associate_accounts()

        # Override per operation
        response = await compute_optimizer_automation.associate_accounts(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await compute_optimizer_automation.associate_accounts(config_overrides={"retry_max_attempts": 1})
```
