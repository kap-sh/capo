# capo-mwaa: typed, async Python SDK for AWS Mwaa

`capo-mwaa` is a typed Python SDK for AWS Mwaa. It has an async client, `AsyncMWAAClient`, for asyncio and trio, and a sync client, `MWAAClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/mwaa/](https://capo-sdk.dev/services/mwaa/)

## Installation

```
pip install capo-mwaa
```

## Usage

```python
from capo_mwaa import AsyncMWAAClient


async def main():
    async with AsyncMWAAClient() as mwaa:
        # Example: call the create_cli_token operation
        response = await mwaa.create_cli_token()
        print(response["cli_token"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_mwaa import AsyncMWAAClient


async def main():
    async with AsyncMWAAClient() as mwaa:
        # Example: paginate over list_environments
        async for item in mwaa.iter_list_environments():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_mwaa import AsyncMWAAClient
from capo_mwaa.error import ResourceNotFoundException


async def main():
    async with AsyncMWAAClient() as mwaa:
        try:
            await mwaa.create_cli_token()
        except ResourceNotFoundException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_mwaa import AsyncMWAAClient


async def main():
    async with AsyncMWAAClient() as mwaa:
        # Default: 3 attempts for every operation
        response = await mwaa.create_cli_token()

        # Override per operation
        response = await mwaa.create_cli_token(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await mwaa.create_cli_token(config_overrides={"retry_max_attempts": 1})
```
