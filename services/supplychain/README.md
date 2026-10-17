# capo-supplychain: typed, async Python SDK for AWS Supplychain

`capo-supplychain` is a typed Python SDK for AWS Supplychain. It has an async client, `AsyncSupplyChainClient`, for asyncio and trio, and a sync client, `SupplyChainClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/supplychain/](https://capo-sdk.dev/services/supplychain/)

## Installation

```
pip install capo-supplychain
```

## Usage

```python
from capo_supplychain import AsyncSupplyChainClient


async def main():
    async with AsyncSupplyChainClient() as supply_chain:
        # Example: call the get_data_integration_event operation
        response = await supply_chain.get_data_integration_event()
        print(response["event"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_supplychain import AsyncSupplyChainClient


async def main():
    async with AsyncSupplyChainClient() as supply_chain:
        # Example: paginate over list_data_integration_events
        async for item in supply_chain.iter_list_data_integration_events():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_supplychain import AsyncSupplyChainClient
from capo_supplychain.error import AccessDeniedException


async def main():
    async with AsyncSupplyChainClient() as supply_chain:
        try:
            await supply_chain.get_data_integration_event()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_supplychain import AsyncSupplyChainClient


async def main():
    async with AsyncSupplyChainClient() as supply_chain:
        # Default: 3 attempts for every operation
        response = await supply_chain.get_data_integration_event()

        # Override per operation
        response = await supply_chain.get_data_integration_event(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await supply_chain.get_data_integration_event(config_overrides={"retry_max_attempts": 1})
```
