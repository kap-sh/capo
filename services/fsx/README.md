# capo-fsx: typed, async Python SDK for AWS FSX

`capo-fsx` is a typed Python SDK for AWS FSX. It has an async client, `AsyncFSxClient`, for asyncio and trio, and a sync client, `FSxClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/fsx/](https://capo-sdk.dev/services/fsx/)

## Installation

```
pip install capo-fsx
```

## Usage

```python
from capo_fsx import AsyncFSxClient


async def main():
    async with AsyncFSxClient() as f_sx:
        # Example: call the associate_file_system_aliases operation
        response = await f_sx.associate_file_system_aliases()
        print(response["aliases"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_fsx import AsyncFSxClient


async def main():
    async with AsyncFSxClient() as f_sx:
        # Example: paginate over describe_backups
        async for item in f_sx.iter_describe_backups():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_fsx import AsyncFSxClient
from capo_fsx.error import BadRequest


async def main():
    async with AsyncFSxClient() as f_sx:
        try:
            await f_sx.associate_file_system_aliases()
        except BadRequest as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_fsx import AsyncFSxClient


async def main():
    async with AsyncFSxClient() as f_sx:
        # Default: 3 attempts for every operation
        response = await f_sx.associate_file_system_aliases()

        # Override per operation
        response = await f_sx.associate_file_system_aliases(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await f_sx.associate_file_system_aliases(config_overrides={"retry_max_attempts": 1})
```
