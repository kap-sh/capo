# capo-tnb: typed, async Python SDK for AWS TNB

`capo-tnb` is a typed Python SDK for AWS TNB. It has an async client, `AsynctnbClient`, for asyncio and trio, and a sync client, `tnbClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/tnb/](https://capo-sdk.dev/services/tnb/)

## Installation

```
pip install capo-tnb
```

## Usage

```python
from capo_tnb import AsynctnbClient


async def main():
    async with AsynctnbClient() as tnb:
        # Example: call the cancel_sol_network_operation operation
        response = await tnb.cancel_sol_network_operation()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_tnb import AsynctnbClient


async def main():
    async with AsynctnbClient() as tnb:
        # Example: paginate over list_sol_function_instances
        async for item in tnb.iter_list_sol_function_instances():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_tnb import AsynctnbClient
from capo_tnb.error import AccessDeniedException


async def main():
    async with AsynctnbClient() as tnb:
        try:
            await tnb.cancel_sol_network_operation()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_tnb import AsynctnbClient


async def main():
    async with AsynctnbClient() as tnb:
        # Default: 3 attempts for every operation
        response = await tnb.cancel_sol_network_operation()

        # Override per operation
        response = await tnb.cancel_sol_network_operation(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await tnb.cancel_sol_network_operation(config_overrides={"retry_max_attempts": 1})
```
