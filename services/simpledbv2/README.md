# capo-simpledbv2: typed, async Python SDK for AWS Simpledbv2

`capo-simpledbv2` is a typed Python SDK for AWS Simpledbv2. It has an async client, `AsyncSimpleDBv2Client`, for asyncio and trio, and a sync client, `SimpleDBv2Client`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/simpledbv2/](https://capo-sdk.dev/services/simpledbv2/)

## Installation

```
pip install capo-simpledbv2
```

## Usage

```python
from capo_simpledbv2 import AsyncSimpleDBv2Client


async def main():
    async with AsyncSimpleDBv2Client() as simple_d_bv2:
        # Example: call the get_export operation
        response = await simple_d_bv2.get_export()
        print(response["export_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_simpledbv2 import AsyncSimpleDBv2Client


async def main():
    async with AsyncSimpleDBv2Client() as simple_d_bv2:
        # Example: paginate over list_exports
        async for item in simple_d_bv2.iter_list_exports():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_simpledbv2 import AsyncSimpleDBv2Client
from capo_simpledbv2.error import InvalidParameterValueException


async def main():
    async with AsyncSimpleDBv2Client() as simple_d_bv2:
        try:
            await simple_d_bv2.get_export()
        except InvalidParameterValueException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_simpledbv2 import AsyncSimpleDBv2Client


async def main():
    async with AsyncSimpleDBv2Client() as simple_d_bv2:
        # Default: 3 attempts for every operation
        response = await simple_d_bv2.get_export()

        # Override per operation
        response = await simple_d_bv2.get_export(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await simple_d_bv2.get_export(config_overrides={"retry_max_attempts": 1})
```
