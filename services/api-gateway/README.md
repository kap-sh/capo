# capo-api-gateway: typed, async Python SDK for AWS API Gateway

`capo-api-gateway` is a typed Python SDK for AWS API Gateway. It has an async client, `AsyncAPIGatewayClient`, for asyncio and trio, and a sync client, `APIGatewayClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/api-gateway/](https://capo-sdk.dev/services/api-gateway/)

## Installation

```
pip install capo-api-gateway
```

## Usage

```python
from capo_api_gateway import AsyncAPIGatewayClient


async def main():
    async with AsyncAPIGatewayClient() as api_gateway:
        # Example: call the create_api_key operation
        response = await api_gateway.create_api_key()
        print(response["id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_api_gateway import AsyncAPIGatewayClient


async def main():
    async with AsyncAPIGatewayClient() as api_gateway:
        # Example: paginate over get_api_keys
        async for item in api_gateway.iter_get_api_keys():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_api_gateway import AsyncAPIGatewayClient
from capo_api_gateway.error import BadRequestException


async def main():
    async with AsyncAPIGatewayClient() as api_gateway:
        try:
            await api_gateway.create_api_key()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_api_gateway import AsyncAPIGatewayClient


async def main():
    async with AsyncAPIGatewayClient() as api_gateway:
        # Default: 3 attempts for every operation
        response = await api_gateway.create_api_key()

        # Override per operation
        response = await api_gateway.create_api_key(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await api_gateway.create_api_key(config_overrides={"retry_max_attempts": 1})
```
