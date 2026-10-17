# capo-iotsecuretunneling: typed, async Python SDK for AWS Iotsecuretunneling

`capo-iotsecuretunneling` is a typed Python SDK for AWS Iotsecuretunneling. It has an async client, `AsyncIoTSecureTunnelingClient`, for asyncio and trio, and a sync client, `IoTSecureTunnelingClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/iotsecuretunneling/](https://capo-sdk.dev/services/iotsecuretunneling/)

## Installation

```
pip install capo-iotsecuretunneling
```

## Usage

```python
from capo_iotsecuretunneling import AsyncIoTSecureTunnelingClient


async def main():
    async with AsyncIoTSecureTunnelingClient() as io_t_secure_tunneling:
        # Example: call the close_tunnel operation
        response = await io_t_secure_tunneling.close_tunnel()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_iotsecuretunneling import AsyncIoTSecureTunnelingClient


async def main():
    async with AsyncIoTSecureTunnelingClient() as io_t_secure_tunneling:
        # Example: paginate over list_tunnels
        async for item in io_t_secure_tunneling.iter_list_tunnels():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_iotsecuretunneling import AsyncIoTSecureTunnelingClient
from capo_iotsecuretunneling.error import ResourceNotFoundException


async def main():
    async with AsyncIoTSecureTunnelingClient() as io_t_secure_tunneling:
        try:
            await io_t_secure_tunneling.close_tunnel()
        except ResourceNotFoundException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_iotsecuretunneling import AsyncIoTSecureTunnelingClient


async def main():
    async with AsyncIoTSecureTunnelingClient() as io_t_secure_tunneling:
        # Default: 3 attempts for every operation
        response = await io_t_secure_tunneling.close_tunnel()

        # Override per operation
        response = await io_t_secure_tunneling.close_tunnel(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await io_t_secure_tunneling.close_tunnel(config_overrides={"retry_max_attempts": 1})
```
