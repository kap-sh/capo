# capo-keyspaces: typed, async Python SDK for AWS Keyspaces

`capo-keyspaces` is a typed Python SDK for AWS Keyspaces. It has an async client, `AsyncKeyspacesClient`, for asyncio and trio, and a sync client, `KeyspacesClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/keyspaces/](https://capo-sdk.dev/services/keyspaces/)

## Installation

```
pip install capo-keyspaces
```

## Usage

```python
from capo_keyspaces import AsyncKeyspacesClient


async def main():
    async with AsyncKeyspacesClient() as keyspaces:
        # Example: call the create_keyspace operation
        response = await keyspaces.create_keyspace()
        print(response["resource_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_keyspaces import AsyncKeyspacesClient


async def main():
    async with AsyncKeyspacesClient() as keyspaces:
        # Example: paginate over list_keyspaces
        async for item in keyspaces.iter_list_keyspaces():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_keyspaces import AsyncKeyspacesClient
from capo_keyspaces.error import AccessDeniedException


async def main():
    async with AsyncKeyspacesClient() as keyspaces:
        try:
            await keyspaces.create_keyspace()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_keyspaces import AsyncKeyspacesClient


async def main():
    async with AsyncKeyspacesClient() as keyspaces:
        # Default: 3 attempts for every operation
        response = await keyspaces.create_keyspace()

        # Override per operation
        response = await keyspaces.create_keyspace(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await keyspaces.create_keyspace(config_overrides={"retry_max_attempts": 1})
```
