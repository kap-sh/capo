# capo-managedblockchain: typed, async Python SDK for AWS Managedblockchain

`capo-managedblockchain` is a typed Python SDK for AWS Managedblockchain. It has an async client, `AsyncManagedBlockchainClient`, for asyncio and trio, and a sync client, `ManagedBlockchainClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/managedblockchain/](https://capo-sdk.dev/services/managedblockchain/)

## Installation

```
pip install capo-managedblockchain
```

## Usage

```python
from capo_managedblockchain import AsyncManagedBlockchainClient


async def main():
    async with AsyncManagedBlockchainClient() as managed_blockchain:
        # Example: call the create_accessor operation
        response = await managed_blockchain.create_accessor()
        print(response["accessor_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_managedblockchain import AsyncManagedBlockchainClient


async def main():
    async with AsyncManagedBlockchainClient() as managed_blockchain:
        # Example: paginate over list_accessors
        async for item in managed_blockchain.iter_list_accessors():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_managedblockchain import AsyncManagedBlockchainClient
from capo_managedblockchain.error import AccessDeniedException


async def main():
    async with AsyncManagedBlockchainClient() as managed_blockchain:
        try:
            await managed_blockchain.create_accessor()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_managedblockchain import AsyncManagedBlockchainClient


async def main():
    async with AsyncManagedBlockchainClient() as managed_blockchain:
        # Default: 3 attempts for every operation
        response = await managed_blockchain.create_accessor()

        # Override per operation
        response = await managed_blockchain.create_accessor(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await managed_blockchain.create_accessor(config_overrides={"retry_max_attempts": 1})
```
