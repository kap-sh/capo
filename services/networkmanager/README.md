# capo-networkmanager: typed, async Python SDK for AWS Networkmanager

`capo-networkmanager` is a typed Python SDK for AWS Networkmanager. It has an async client, `AsyncNetworkManagerClient`, for asyncio and trio, and a sync client, `NetworkManagerClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/networkmanager/](https://capo-sdk.dev/services/networkmanager/)

## Installation

```
pip install capo-networkmanager
```

## Usage

```python
from capo_networkmanager import AsyncNetworkManagerClient


async def main():
    async with AsyncNetworkManagerClient() as network_manager:
        # Example: call the accept_attachment operation
        response = await network_manager.accept_attachment()
        print(response["attachment"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_networkmanager import AsyncNetworkManagerClient


async def main():
    async with AsyncNetworkManagerClient() as network_manager:
        # Example: paginate over describe_global_networks
        async for item in network_manager.iter_describe_global_networks():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_networkmanager import AsyncNetworkManagerClient
from capo_networkmanager.error import AccessDeniedException


async def main():
    async with AsyncNetworkManagerClient() as network_manager:
        try:
            await network_manager.accept_attachment()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_networkmanager import AsyncNetworkManagerClient


async def main():
    async with AsyncNetworkManagerClient() as network_manager:
        # Default: 3 attempts for every operation
        response = await network_manager.accept_attachment()

        # Override per operation
        response = await network_manager.accept_attachment(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await network_manager.accept_attachment(config_overrides={"retry_max_attempts": 1})
```
