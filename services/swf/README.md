# capo-swf: typed, async Python SDK for AWS SWF

`capo-swf` is a typed Python SDK for AWS SWF. It has an async client, `AsyncSWFClient`, for asyncio and trio, and a sync client, `SWFClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/swf/](https://capo-sdk.dev/services/swf/)

## Installation

```
pip install capo-swf
```

## Usage

```python
from capo_swf import AsyncSWFClient


async def main():
    async with AsyncSWFClient() as swf:
        # Example: call the count_closed_workflow_executions operation
        response = await swf.count_closed_workflow_executions()
        print(response["count"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_swf import AsyncSWFClient


async def main():
    async with AsyncSWFClient() as swf:
        # Example: paginate over get_workflow_execution_history
        async for item in swf.iter_get_workflow_execution_history():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_swf import AsyncSWFClient
from capo_swf.error import OperationNotPermittedFault


async def main():
    async with AsyncSWFClient() as swf:
        try:
            await swf.count_closed_workflow_executions()
        except OperationNotPermittedFault as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_swf import AsyncSWFClient


async def main():
    async with AsyncSWFClient() as swf:
        # Default: 3 attempts for every operation
        response = await swf.count_closed_workflow_executions()

        # Override per operation
        response = await swf.count_closed_workflow_executions(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await swf.count_closed_workflow_executions(config_overrides={"retry_max_attempts": 1})
```
