# capo-storage-gateway: typed, async Python SDK for AWS Storage Gateway

`capo-storage-gateway` is a typed Python SDK for AWS Storage Gateway. It has an async client, `AsyncStorageGatewayClient`, for asyncio and trio, and a sync client, `StorageGatewayClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/storage-gateway/](https://capo-sdk.dev/services/storage-gateway/)

## Installation

```
pip install capo-storage-gateway
```

## Usage

```python
from capo_storage_gateway import AsyncStorageGatewayClient


async def main():
    async with AsyncStorageGatewayClient() as storage_gateway:
        # Example: call the activate_gateway operation
        response = await storage_gateway.activate_gateway()
        print(response["gateway_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_storage_gateway import AsyncStorageGatewayClient


async def main():
    async with AsyncStorageGatewayClient() as storage_gateway:
        # Example: paginate over describe_tape_archives
        async for item in storage_gateway.iter_describe_tape_archives():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_storage_gateway import AsyncStorageGatewayClient
from capo_storage_gateway.error import InternalServerError


async def main():
    async with AsyncStorageGatewayClient() as storage_gateway:
        try:
            await storage_gateway.activate_gateway()
        except InternalServerError as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_storage_gateway import AsyncStorageGatewayClient


async def main():
    async with AsyncStorageGatewayClient() as storage_gateway:
        # Default: 3 attempts for every operation
        response = await storage_gateway.activate_gateway()

        # Override per operation
        response = await storage_gateway.activate_gateway(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await storage_gateway.activate_gateway(config_overrides={"retry_max_attempts": 1})
```
