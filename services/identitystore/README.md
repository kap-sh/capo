# capo-identitystore: typed, async Python SDK for AWS Identitystore

`capo-identitystore` is a typed Python SDK for AWS Identitystore. It has an async client, `AsyncidentitystoreClient`, for asyncio and trio, and a sync client, `identitystoreClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/identitystore/](https://capo-sdk.dev/services/identitystore/)

## Installation

```
pip install capo-identitystore
```

## Usage

```python
from capo_identitystore import AsyncidentitystoreClient


async def main():
    async with AsyncidentitystoreClient() as identitystore:
        # Example: call the create_group_membership operation
        response = await identitystore.create_group_membership()
        print(response["identity_store_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_identitystore import AsyncidentitystoreClient


async def main():
    async with AsyncidentitystoreClient() as identitystore:
        # Example: paginate over list_group_memberships
        async for item in identitystore.iter_list_group_memberships():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_identitystore import AsyncidentitystoreClient
from capo_identitystore.error import AccessDeniedException


async def main():
    async with AsyncidentitystoreClient() as identitystore:
        try:
            await identitystore.create_group_membership()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_identitystore import AsyncidentitystoreClient


async def main():
    async with AsyncidentitystoreClient() as identitystore:
        # Default: 3 attempts for every operation
        response = await identitystore.create_group_membership()

        # Override per operation
        response = await identitystore.create_group_membership(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await identitystore.create_group_membership(config_overrides={"retry_max_attempts": 1})
```
