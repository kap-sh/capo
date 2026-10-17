# capo-keyspacesstreams: typed, async Python SDK for AWS Keyspacesstreams

`capo-keyspacesstreams` is a typed Python SDK for AWS Keyspacesstreams. It has an async client, `AsyncKeyspacesStreamsClient`, for asyncio and trio, and a sync client, `KeyspacesStreamsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/keyspacesstreams/](https://capo-sdk.dev/services/keyspacesstreams/)

## Installation

```
pip install capo-keyspacesstreams
```

## Usage

```python
from capo_keyspacesstreams import AsyncKeyspacesStreamsClient


async def main():
    async with AsyncKeyspacesStreamsClient() as keyspaces_streams:
        # Example: call the get_records operation
        response = await keyspaces_streams.get_records()
        print(response["change_records"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_keyspacesstreams import AsyncKeyspacesStreamsClient


async def main():
    async with AsyncKeyspacesStreamsClient() as keyspaces_streams:
        # Example: paginate over get_stream
        async for item in keyspaces_streams.iter_get_stream():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_keyspacesstreams import AsyncKeyspacesStreamsClient
from capo_keyspacesstreams.error import AccessDeniedException


async def main():
    async with AsyncKeyspacesStreamsClient() as keyspaces_streams:
        try:
            await keyspaces_streams.get_records()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_keyspacesstreams import AsyncKeyspacesStreamsClient


async def main():
    async with AsyncKeyspacesStreamsClient() as keyspaces_streams:
        # Default: 3 attempts for every operation
        response = await keyspaces_streams.get_records()

        # Override per operation
        response = await keyspaces_streams.get_records(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await keyspaces_streams.get_records(config_overrides={"retry_max_attempts": 1})
```
