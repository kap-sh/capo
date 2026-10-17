# capo-greengrassv2: typed, async Python SDK for AWS Greengrassv2

`capo-greengrassv2` is a typed Python SDK for AWS Greengrassv2. It has an async client, `AsyncGreengrassV2Client`, for asyncio and trio, and a sync client, `GreengrassV2Client`, with the same methods. Requests and responses are typed with TypedDicts, so your editor and type checker know every field.

It is part of [capo](https://capo-sdk.dev/), a community-driven alternative to boto3 and aioboto3, built on its own HTTP stack instead of botocore and generated from the official AWS Smithy models. Documentation: [https://capo-sdk.dev/services/greengrassv2/](https://capo-sdk.dev/services/greengrassv2/)

## Installation

```
pip install capo-greengrassv2
```

## Usage

```python
from capo_greengrassv2 import AsyncGreengrassV2Client


async def main():
    async with AsyncGreengrassV2Client() as greengrass_v2:
        # Example: call the associate_service_role_to_account operation
        response = await greengrass_v2.associate_service_role_to_account()
        print(response["associated_at"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_greengrassv2 import AsyncGreengrassV2Client


async def main():
    async with AsyncGreengrassV2Client() as greengrass_v2:
        # Example: paginate over list_client_devices_associated_with_core_device
        async for item in greengrass_v2.iter_list_client_devices_associated_with_core_device():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_greengrassv2 import AsyncGreengrassV2Client
from capo_greengrassv2.error import InternalServerException


async def main():
    async with AsyncGreengrassV2Client() as greengrass_v2:
        try:
            await greengrass_v2.associate_service_role_to_account()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_greengrassv2 import AsyncGreengrassV2Client


async def main():
    async with AsyncGreengrassV2Client() as greengrass_v2:
        # Default: 3 attempts for every operation
        response = await greengrass_v2.associate_service_role_to_account()

        # Override per operation
        response = await greengrass_v2.associate_service_role_to_account(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await greengrass_v2.associate_service_role_to_account(config_overrides={"retry_max_attempts": 1})
```
