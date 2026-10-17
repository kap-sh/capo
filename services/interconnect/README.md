# capo-interconnect: typed, async Python SDK for AWS Interconnect

`capo-interconnect` is a typed Python SDK for AWS Interconnect. It has an async client, `AsyncInterconnectClient`, for asyncio and trio, and a sync client, `InterconnectClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/interconnect/](https://capo-sdk.dev/services/interconnect/)

## Installation

```
pip install capo-interconnect
```

## Usage

```python
from capo_interconnect import AsyncInterconnectClient


async def main():
    async with AsyncInterconnectClient() as interconnect:
        # Example: call the accept_connection_proposal operation
        response = await interconnect.accept_connection_proposal()
        print(response["connection"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_interconnect import AsyncInterconnectClient


async def main():
    async with AsyncInterconnectClient() as interconnect:
        # Example: paginate over list_attach_points
        async for item in interconnect.iter_list_attach_points():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_interconnect import AsyncInterconnectClient
from capo_interconnect.error import AccessDeniedException


async def main():
    async with AsyncInterconnectClient() as interconnect:
        try:
            await interconnect.accept_connection_proposal()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_interconnect import AsyncInterconnectClient


async def main():
    async with AsyncInterconnectClient() as interconnect:
        # Default: 3 attempts for every operation
        response = await interconnect.accept_connection_proposal()

        # Override per operation
        response = await interconnect.accept_connection_proposal(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await interconnect.accept_connection_proposal(config_overrides={"retry_max_attempts": 1})
```
