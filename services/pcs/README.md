# capo-pcs: typed, async Python SDK for AWS PCS

`capo-pcs` is a typed Python SDK for AWS PCS. It has an async client, `AsyncPCSClient`, for asyncio and trio, and a sync client, `PCSClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/pcs/](https://capo-sdk.dev/services/pcs/)

## Installation

```
pip install capo-pcs
```

## Usage

```python
from capo_pcs import AsyncPCSClient


async def main():
    async with AsyncPCSClient() as pcs:
        # Example: call the list_tags_for_resource operation
        response = await pcs.list_tags_for_resource()
        print(response["tags"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_pcs import AsyncPCSClient


async def main():
    async with AsyncPCSClient() as pcs:
        # Example: paginate over list_clusters
        async for item in pcs.iter_list_clusters():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_pcs import AsyncPCSClient
from capo_pcs.error import ResourceNotFoundException


async def main():
    async with AsyncPCSClient() as pcs:
        try:
            await pcs.list_tags_for_resource()
        except ResourceNotFoundException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_pcs import AsyncPCSClient


async def main():
    async with AsyncPCSClient() as pcs:
        # Default: 3 attempts for every operation
        response = await pcs.list_tags_for_resource()

        # Override per operation
        response = await pcs.list_tags_for_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await pcs.list_tags_for_resource(config_overrides={"retry_max_attempts": 1})
```
