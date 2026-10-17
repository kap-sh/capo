# capo-codestar-connections: typed, async Python SDK for AWS Codestar Connections

`capo-codestar-connections` is a typed Python SDK for AWS Codestar Connections. It has an async client, `AsyncCodeStarconnectionsClient`, for asyncio and trio, and a sync client, `CodeStarconnectionsClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/codestar-connections/](https://capo-sdk.dev/services/codestar-connections/)

## Installation

```
pip install capo-codestar-connections
```

## Usage

```python
from capo_codestar_connections import AsyncCodeStarconnectionsClient


async def main():
    async with AsyncCodeStarconnectionsClient() as code_starconnections:
        # Example: call the create_connection operation
        response = await code_starconnections.create_connection()
        print(response["connection_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_codestar_connections import AsyncCodeStarconnectionsClient


async def main():
    async with AsyncCodeStarconnectionsClient() as code_starconnections:
        # Example: paginate over list_connections
        async for item in code_starconnections.iter_list_connections():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_codestar_connections import AsyncCodeStarconnectionsClient
from capo_codestar_connections.error import LimitExceededException


async def main():
    async with AsyncCodeStarconnectionsClient() as code_starconnections:
        try:
            await code_starconnections.create_connection()
        except LimitExceededException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_codestar_connections import AsyncCodeStarconnectionsClient


async def main():
    async with AsyncCodeStarconnectionsClient() as code_starconnections:
        # Default: 3 attempts for every operation
        response = await code_starconnections.create_connection()

        # Override per operation
        response = await code_starconnections.create_connection(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await code_starconnections.create_connection(config_overrides={"retry_max_attempts": 1})
```
