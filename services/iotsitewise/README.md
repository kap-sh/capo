# capo-iotsitewise: typed, async Python SDK for AWS Iotsitewise

`capo-iotsitewise` is a typed Python SDK for AWS Iotsitewise. It has an async client, `AsyncIoTSiteWiseClient`, for asyncio and trio, and a sync client, `IoTSiteWiseClient`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/iotsitewise/](https://capo-sdk.dev/services/iotsitewise/)

## Installation

```
pip install capo-iotsitewise
```

## Usage

```python
from capo_iotsitewise import AsyncIoTSiteWiseClient


async def main():
    async with AsyncIoTSiteWiseClient() as io_t_site_wise:
        # Example: call the associate_assets operation
        response = await io_t_site_wise.associate_assets()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_iotsitewise import AsyncIoTSiteWiseClient


async def main():
    async with AsyncIoTSiteWiseClient() as io_t_site_wise:
        # Example: paginate over batch_get_asset_property_aggregates
        async for item in io_t_site_wise.iter_batch_get_asset_property_aggregates():
            print(item)
```

## Waiters

Waiters poll an operation until a resource reaches a desired state. If the operation supports waiters it will have a `wait_until_` prefixed method.

```python
from capo_iotsitewise import AsyncIoTSiteWiseClient


async def main():
    async with AsyncIoTSiteWiseClient() as io_t_site_wise:
        # Example: wait for asset_not_exists
        await io_t_site_wise.wait_until_asset_not_exists(max_wait_time=300)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_iotsitewise import AsyncIoTSiteWiseClient
from capo_iotsitewise.error import ConflictingOperationException


async def main():
    async with AsyncIoTSiteWiseClient() as io_t_site_wise:
        try:
            await io_t_site_wise.associate_assets()
        except ConflictingOperationException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_iotsitewise import AsyncIoTSiteWiseClient


async def main():
    async with AsyncIoTSiteWiseClient() as io_t_site_wise:
        # Default: 3 attempts for every operation
        response = await io_t_site_wise.associate_assets()

        # Override per operation
        response = await io_t_site_wise.associate_assets(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await io_t_site_wise.associate_assets(config_overrides={"retry_max_attempts": 1})
```
