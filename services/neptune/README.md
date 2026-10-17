# capo-neptune: typed, async Python SDK for AWS Neptune

`capo-neptune` is a typed Python SDK for AWS Neptune. It has an async client, `AsyncNeptuneClient`, for asyncio and trio, and a sync client, `NeptuneClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/neptune/](https://capo-sdk.dev/services/neptune/)

## Installation

```
pip install capo-neptune
```

## Usage

```python
from capo_neptune import AsyncNeptuneClient


async def main():
    async with AsyncNeptuneClient() as neptune:
        # Example: call the add_role_to_db_cluster operation
        response = await neptune.add_role_to_db_cluster()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_neptune import AsyncNeptuneClient


async def main():
    async with AsyncNeptuneClient() as neptune:
        # Example: paginate over describe_db_cluster_endpoints
        async for item in neptune.iter_describe_db_cluster_endpoints():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_neptune import AsyncNeptuneClient
from capo_neptune.error import DBClusterNotFoundFault


async def main():
    async with AsyncNeptuneClient() as neptune:
        try:
            await neptune.add_role_to_db_cluster()
        except DBClusterNotFoundFault as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_neptune import AsyncNeptuneClient


async def main():
    async with AsyncNeptuneClient() as neptune:
        # Default: 3 attempts for every operation
        response = await neptune.add_role_to_db_cluster()

        # Override per operation
        response = await neptune.add_role_to_db_cluster(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await neptune.add_role_to_db_cluster(config_overrides={"retry_max_attempts": 1})
```
