# capo-drs: typed, async Python SDK for AWS DRS

`capo-drs` is a typed Python SDK for AWS DRS. It has an async client, `AsyncdrsClient`, for asyncio and trio, and a sync client, `drsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/drs/](https://capo-sdk.dev/services/drs/)

## Installation

```
pip install capo-drs
```

## Usage

```python
from capo_drs import AsyncdrsClient


async def main():
    async with AsyncdrsClient() as drs:
        # Example: call the cancel_recovery_plan_execution operation
        response = await drs.cancel_recovery_plan_execution()
        print(response["recovery_plan_execution"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_drs import AsyncdrsClient


async def main():
    async with AsyncdrsClient() as drs:
        # Example: paginate over list_extensible_source_servers
        async for item in drs.iter_list_extensible_source_servers():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_drs import AsyncdrsClient
from capo_drs.error import AccessDeniedException


async def main():
    async with AsyncdrsClient() as drs:
        try:
            await drs.cancel_recovery_plan_execution()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_drs import AsyncdrsClient


async def main():
    async with AsyncdrsClient() as drs:
        # Default: 3 attempts for every operation
        response = await drs.cancel_recovery_plan_execution()

        # Override per operation
        response = await drs.cancel_recovery_plan_execution(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await drs.cancel_recovery_plan_execution(config_overrides={"retry_max_attempts": 1})
```
