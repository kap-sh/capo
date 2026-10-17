# capo-direct-connect: typed, async Python SDK for AWS Direct Connect

`capo-direct-connect` is a typed Python SDK for AWS Direct Connect. It has an async client, `AsyncDirectConnectClient`, for asyncio and trio, and a sync client, `DirectConnectClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/direct-connect/](https://capo-sdk.dev/services/direct-connect/)

## Installation

```
pip install capo-direct-connect
```

## Usage

```python
from capo_direct_connect import AsyncDirectConnectClient


async def main():
    async with AsyncDirectConnectClient() as direct_connect:
        # Example: call the accept_direct_connect_gateway_association_proposal operation
        response = await direct_connect.accept_direct_connect_gateway_association_proposal()
        print(response["direct_connect_gateway_association"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_direct_connect import AsyncDirectConnectClient
from capo_direct_connect.error import DirectConnectClientException


async def main():
    async with AsyncDirectConnectClient() as direct_connect:
        try:
            await direct_connect.accept_direct_connect_gateway_association_proposal()
        except DirectConnectClientException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_direct_connect import AsyncDirectConnectClient


async def main():
    async with AsyncDirectConnectClient() as direct_connect:
        # Default: 3 attempts for every operation
        response = await direct_connect.accept_direct_connect_gateway_association_proposal()

        # Override per operation
        response = await direct_connect.accept_direct_connect_gateway_association_proposal(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await direct_connect.accept_direct_connect_gateway_association_proposal(config_overrides={"retry_max_attempts": 1})
```
