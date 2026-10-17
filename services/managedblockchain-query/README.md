# capo-managedblockchain-query: typed, async Python SDK for AWS Managedblockchain Query

`capo-managedblockchain-query` is a typed Python SDK for AWS Managedblockchain Query. It has an async client, `AsyncManagedBlockchainQueryClient`, for asyncio and trio, and a sync client, `ManagedBlockchainQueryClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/managedblockchain-query/](https://capo-sdk.dev/services/managedblockchain-query/)

## Installation

```
pip install capo-managedblockchain-query
```

## Usage

```python
from capo_managedblockchain_query import AsyncManagedBlockchainQueryClient


async def main():
    async with AsyncManagedBlockchainQueryClient() as managed_blockchain_query:
        # Example: call the batch_get_token_balance operation
        response = await managed_blockchain_query.batch_get_token_balance()
        print(response["token_balances"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_managedblockchain_query import AsyncManagedBlockchainQueryClient


async def main():
    async with AsyncManagedBlockchainQueryClient() as managed_blockchain_query:
        # Example: paginate over list_asset_contracts
        async for item in managed_blockchain_query.iter_list_asset_contracts():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_managedblockchain_query import AsyncManagedBlockchainQueryClient
from capo_managedblockchain_query.error import AccessDeniedException


async def main():
    async with AsyncManagedBlockchainQueryClient() as managed_blockchain_query:
        try:
            await managed_blockchain_query.batch_get_token_balance()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_managedblockchain_query import AsyncManagedBlockchainQueryClient


async def main():
    async with AsyncManagedBlockchainQueryClient() as managed_blockchain_query:
        # Default: 3 attempts for every operation
        response = await managed_blockchain_query.batch_get_token_balance()

        # Override per operation
        response = await managed_blockchain_query.batch_get_token_balance(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await managed_blockchain_query.batch_get_token_balance(config_overrides={"retry_max_attempts": 1})
```
