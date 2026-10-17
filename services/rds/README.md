# capo-rds: typed, async Python SDK for AWS RDS

`capo-rds` is a typed Python SDK for AWS RDS. It has an async client, `AsyncRDSClient`, for asyncio and trio, and a sync client, `RDSClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/rds/](https://capo-sdk.dev/services/rds/)

## Installation

```
pip install capo-rds
```

## Usage

```python
from capo_rds import AsyncRDSClient


async def main():
    async with AsyncRDSClient() as rds:
        # Example: call the add_role_to_db_cluster operation
        response = await rds.add_role_to_db_cluster()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_rds import AsyncRDSClient


async def main():
    async with AsyncRDSClient() as rds:
        # Example: paginate over describe_blue_green_deployments
        async for item in rds.iter_describe_blue_green_deployments():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_rds import AsyncRDSClient
from capo_rds.error import DBClusterNotFoundFault


async def main():
    async with AsyncRDSClient() as rds:
        try:
            await rds.add_role_to_db_cluster()
        except DBClusterNotFoundFault as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_rds import AsyncRDSClient


async def main():
    async with AsyncRDSClient() as rds:
        # Default: 3 attempts for every operation
        response = await rds.add_role_to_db_cluster()

        # Override per operation
        response = await rds.add_role_to_db_cluster(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await rds.add_role_to_db_cluster(config_overrides={"retry_max_attempts": 1})
```
