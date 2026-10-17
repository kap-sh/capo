# capo-rtbfabric: typed, async Python SDK for AWS Rtbfabric

`capo-rtbfabric` is a typed Python SDK for AWS Rtbfabric. It has an async client, `AsyncRTBFabricClient`, for asyncio and trio, and a sync client, `RTBFabricClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/rtbfabric/](https://capo-sdk.dev/services/rtbfabric/)

## Installation

```
pip install capo-rtbfabric
```

## Usage

```python
from capo_rtbfabric import AsyncRTBFabricClient


async def main():
    async with AsyncRTBFabricClient() as rtb_fabric:
        # Example: call the list_requester_gateways operation
        response = await rtb_fabric.list_requester_gateways()
        print(response["gateway_ids"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_rtbfabric import AsyncRTBFabricClient


async def main():
    async with AsyncRTBFabricClient() as rtb_fabric:
        # Example: paginate over list_requester_gateways
        async for item in rtb_fabric.iter_list_requester_gateways():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_rtbfabric import AsyncRTBFabricClient
from capo_rtbfabric.error import InternalServerException


async def main():
    async with AsyncRTBFabricClient() as rtb_fabric:
        try:
            await rtb_fabric.list_requester_gateways()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_rtbfabric import AsyncRTBFabricClient


async def main():
    async with AsyncRTBFabricClient() as rtb_fabric:
        # Default: 3 attempts for every operation
        response = await rtb_fabric.list_requester_gateways()

        # Override per operation
        response = await rtb_fabric.list_requester_gateways(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await rtb_fabric.list_requester_gateways(config_overrides={"retry_max_attempts": 1})
```
